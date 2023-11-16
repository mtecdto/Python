import csv
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from app.forms import keysForm
from app.models import general_keys, tabela_backup
from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import GeneralKeyForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging
import pandas as pd
from django.contrib import messages
from django.db.models import Q

from .forms import GeneralKeyForm,EstoqueWindowsForm,keysEstoqueWindowsForm,InserirChavesForm,quantidade_maquinasForm


from .models import general_keys,tabela_Estoque_WindowsKeys,tabela_Chaves_Duplicadas,quantidade_maquinas  # Importe o modelo adequado



def criar_quantidade_maquinas(request):
    registro = quantidade_maquinas.objects.get(id=1)
    if request.method == 'POST':
        form = quantidade_maquinasForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = quantidade_maquinasForm(instance=registro)
        return redirect('home')

    return render(request, 'index.html', {'form': form})

def createLogin(request):
    return render(request, 'createLogin.html')

def painel(request):
    return render(request, 'painel.html')

def logouts(request):
    logout(request)
    return redirect('/painel/')

def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request,user)
        return redirect('home')
    else:
        data['msg'] = 'Usuário ou senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request,'painel.html',data)


from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


def store(request):
    data = {}
    if request.POST['password'] != request.POST['password-conf']:
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        try:
            # Validação de senha personalizada
            min_length = 8  # Mínimo de 8 caracteres
            password = request.POST['password']

            if len(password) < min_length:
                raise ValidationError(
                    f'A senha deve ter pelo menos {min_length} caracteres.')

            if not any(char.isdigit() for char in password):
                raise ValidationError('A senha deve conter números.')

            if not any(char.isupper() for char in password):
                raise ValidationError('A senha deve conter letras maiúsculas.')

            if not any(char in "!@#$%^&*()_+[]{}?:;|'\"<>,./" for char in password):
                raise ValidationError('A senha deve conter caracteres especiais.')

            password_validation.validate_password(password)

            user = User.objects.create_user(
                request.POST['user'], request.POST['email'], password)
            user.first_name = request.POST['name']
            user.save()
            data['msg'] = 'Usuário Cadastrado com Sucesso!'
            data['class'] = 'alert-success'
        except ValidationError as e:
            # Lidar com erros de validação de senha
            data['msg'] = ', '.join(e.messages)
            data['class'] = 'alert-danger'

    return render(request, 'createLogin.html', data)


def atualizar_valores(request):
    registros = general_keys.objects.filter(keystate=2)

    for registro in registros:
        registro.keystate = 0
        registro.save()
    return redirect('home')

def estoque_keys_status_disponível(request):
    registros = general_keys.objects.filter(keystate=0)

    for registro in registros:
        novo_registro_estoque = tabela_Estoque_WindowsKeys(keystate=0, keycontent=registro.keycontent, so=registro.so,data=registro.data,Nota_Fiscal=registro.Nota_Fiscal,PeCom=registro.PeCom,uf=registro.uf)
        registro.delete()
        novo_registro_estoque.save()
    return redirect('home')

def insertKeys2(request):
    if request.method == 'POST':
        form = GeneralKeyForm(request.POST)
        if form.is_valid():
            chaves = form.cleaned_data['chaves']
            pv = form.cleaned_data['pv']


            vetor_chaves = chaves.split()
            insercoes = []


            for key in vetor_chaves:
                general_key = general_keys(keycontent=key, pv=pv,PeCom=form.cleaned_data['PeCom'],Nota_Fiscal=form.cleaned_data['Nota_Fiscal'],uf=form.cleaned_data['uf'], so=form.cleaned_data['so'], marca=form.cleaned_data['marca'],modelo=form.cleaned_data['modelo'])
                insercoes.append(general_key)

            general_keys.objects.bulk_create(insercoes)
            return redirect('home')
    else:
        form = GeneralKeyForm()

    return render(request, 'insertKeys2.html', {'form': form})

from django.contrib import messages

def inserir_chaves(request):
    if request.method == 'POST':
        form = InserirChavesForm(request.POST)
        if form.is_valid():
            numero_de_chaves = form.cleaned_data['numero_de_chaves']
            novo_pv = form.cleaned_data['novo_pv']  # Valor do novo PV
            selected_so = form.cleaned_data['so']
            marca = form.cleaned_data['marca']
            modelo = form.cleaned_data['modelo']  # SO selecionado pelo usuário

            # Consulte as chaves da tabela_Estoque_WindowsKeys com uf igual a "DF" e SO selecionado
            chaves_a_inserir = tabela_Estoque_WindowsKeys.objects.filter(uf="DF", so=selected_so)[:numero_de_chaves]

            # Inicialize uma variável para contar as chaves inseridas
            chaves_inseridas = 0

            # Insira as chaves na tabela general_keys com Nota_Fiscal, PeCom, uf e novo_pv
            for chave in chaves_a_inserir:
                general_key = general_keys(
                    keycontent=chave.keycontent,
                    so=chave.so,
                    Nota_Fiscal=chave.Nota_Fiscal,
                    PeCom=chave.PeCom,
                    uf=chave.uf,
                    pv=novo_pv,
                    marca=marca,
                    modelo=modelo
                )
                general_key.save()

                # Exclua a chave da tabela original
                chave.delete()

                # Aumente o contador de chaves inseridas
                chaves_inseridas += 1

            # Use messages.success para definir uma mensagem de sucesso
            if chaves_inseridas == numero_de_chaves:
                messages.success(request, f'Sucesso! {chaves_inseridas} chave(s) foram inserida(s) com sucesso.')
            elif chaves_inseridas > 0:
                messages.error(request, f'Erro: foram inseridas {chaves_inseridas} chave(s) de {numero_de_chaves} ')
            else:
                messages.error(request, f'Erro: O banco de dados não possui os registros que deseja. Tente outras versões do Windows ou solicite mais chaves ao administrador.')

            # Redirecione para a página inicial
            return redirect('home')

    else:
        form = InserirChavesForm()

    return render(request, 'index.html', {'form': form})

from django.shortcuts import get_object_or_404


def insertkeys3(request):
    data = {}
    all_items = tabela_Estoque_WindowsKeys.objects.all().order_by('-idkey')

    # Aplicar a busca (se existir)
    search = request.GET.get('search')
    if search:
        all_items = all_items.filter(
            Q(pv__icontains=search) | Q(keycontent__icontains=search) | Q(PeCom__icontains=search) | Q(
                Nota_Fiscal__icontains=search) | Q(serialcontent__icontains=search))

    # Aplicar a paginação
    paginator = Paginator(all_items, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data['db'] = page_obj
    if request.method == 'POST':
        form = EstoqueWindowsForm(request.POST)
        if form.is_valid():
            chaves = form.cleaned_data['chaves']
            vetor_chaves = chaves.split()
            insercoes = []
            insercoes_duplicadas = []
            duplicado_vetor = []  # Inicialize o vetor de duplicados

            for key in vetor_chaves:
                existing_key_tb_estoque = tabela_Estoque_WindowsKeys.objects.filter(keycontent=key).first()
                existing_key_tb_backup = tabela_backup.objects.filter(keycontent=key).first()
                existing_key_tb_general = general_keys.objects.filter(keycontent=key).first()

                if existing_key_tb_estoque:
                    # Chave existe, crie uma duplicata com base nas informações existentes
                    chave_duplicada_estoque = tabela_Chaves_Duplicadas(
                        keycontent=key,
                        so=existing_key_tb_estoque.so,
                        serialcontent=existing_key_tb_estoque.serialcontent,
                        PeCom=existing_key_tb_estoque.PeCom,
                        pv=existing_key_tb_estoque.pv,
                        data_duplicada=existing_key_tb_estoque.data,
                        Nota_Fiscal=existing_key_tb_estoque.Nota_Fiscal,
                        uf=existing_key_tb_estoque.uf
                    )
                    insercoes_duplicadas.append(chave_duplicada_estoque)

                    # Verifique se a chave já está no vetor de duplicados
                    if key not in duplicado_vetor:
                        duplicado_vetor.append(key)  # Adicione à lista de duplicados

                elif existing_key_tb_backup:
                    chave_duplicada_backup = tabela_Chaves_Duplicadas(
                        keycontent=key,
                        so=existing_key_tb_backup.so,
                        serialcontent=existing_key_tb_backup.serialcontent,
                        PeCom=existing_key_tb_backup.PeCom,
                        pv=existing_key_tb_backup.pv,
                        data_duplicada=existing_key_tb_backup.data,
                        Nota_Fiscal=existing_key_tb_backup.Nota_Fiscal,
                        uf=existing_key_tb_backup.uf
                    )
                    insercoes_duplicadas.append(chave_duplicada_backup)

                    if key not in duplicado_vetor:
                        duplicado_vetor.append(key)

                elif existing_key_tb_general:
                    chave_duplicada_general = tabela_Chaves_Duplicadas(
                        keycontent=key,
                        so=existing_key_tb_general.so,
                        serialcontent=existing_key_tb_general.serialcontent,
                        PeCom=existing_key_tb_general.PeCom,
                        pv=existing_key_tb_general.pv,
                        data_duplicada=existing_key_tb_general.data,
                        Nota_Fiscal=existing_key_tb_general.Nota_Fiscal,
                        uf=existing_key_tb_general.uf
                    )
                    insercoes_duplicadas.append(chave_duplicada_general)

                    if key not in duplicado_vetor:
                        duplicado_vetor.append(key)

                else:
                    # Chave não existe, crie um novo registro com base nos dados do formulário
                    chave_nova = tabela_Estoque_WindowsKeys(
                        keycontent=key,
                        so=form.cleaned_data['so'],
                        PeCom=form.cleaned_data['PeCom'],
                        Nota_Fiscal=form.cleaned_data['Nota_Fiscal'],
                        uf=form.cleaned_data['uf']
                    )
                    insercoes.append(chave_nova)

            # Faça as inserções nas tabelas correspondentes
            tabela_Estoque_WindowsKeys.objects.bulk_create(insercoes)
            tabela_Chaves_Duplicadas.objects.bulk_create(insercoes_duplicadas)

            if duplicado_vetor:
                # Se houver chaves duplicadas, defina uma mensagem de erro única
                messages.error(request,
                               f'ATENÇÃO Foram encontradas {len(duplicado_vetor)} chaves duplicadas, e {len(insercoes)} foram inseridas com sucesso.')
            else:
                # Se não houver chaves duplicadas, defina uma mensagem de sucesso
                messages.success(request, f'SUCESSO Todas as {len(insercoes)} chaves foram inseridas com sucesso.')

            return redirect('insertkeys3')
    else:
        form = EstoqueWindowsForm()

    data['form'] = form
    quantidade_registros = all_items.count()
    quantidade_registros_w11 = tabela_Estoque_WindowsKeys.objects.filter(so__icontains='Windows11').count()
    quantidade_registros_w10 = tabela_Estoque_WindowsKeys.objects.filter(so__icontains='Windows10').count()

    data['quantidade_registros_w10'] = quantidade_registros_w10
    data['quantidade_registros_w11'] = quantidade_registros_w11
    data['quantidade_registros'] = quantidade_registros

    return render(request, 'insertkeys3.html', data)

def home(request):
    data = {}
    all_items = general_keys.objects.all().order_by('-data')

    # Aplicar a busca (se existir)
    search = request.GET.get('search')
    if search:
        all_items = all_items.filter(Q(pv__icontains=search) | Q(keycontent__icontains=search) | Q(PeCom__icontains=search) | Q(Nota_Fiscal__icontains=search) | Q(serialcontent__icontains=search))

    # Aplicar a paginação
    paginator = Paginator(all_items, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data['db'] = page_obj

    if request.method == 'POST':
        form = InserirChavesForm(request.POST)
        if form.is_valid():
            numero_de_chaves = form.cleaned_data['numero_de_chaves']

            # Consulte as chaves da tabela_Estoque_WindowsKeys com uf igual a "DF"
            chaves_a_inserir = tabela_Estoque_WindowsKeys.objects.filter(uf="DF")[:numero_de_chaves]

            # Insira as chaves na tabela general_keys com Nota_Fiscal, PeCom e uf
            for chave in chaves_a_inserir:
                general_key = general_keys(
                    keycontent=chave.keycontent,
                    so=chave.so,
                    Nota_Fiscal=chave.Nota_Fiscal,
                    PeCom=chave.PeCom,
                    uf=chave.uf,

                )
                general_key.save()

                # Exclua a chave da tabela original
                chave.delete()
            return redirect('home')
    else:
        form = InserirChavesForm()

    data['form'] = form

    quantidade_registros = all_items.count()
    quantidade_registros_w11 = general_keys.objects.filter(so__icontains='Windows11')
    quantidade_registros_w11 = quantidade_registros_w11.count()
    quantidade_keystate_3 = general_keys.objects.filter(keystate=3).count()
    quantidade_keystate_2 = general_keys.objects.filter(keystate=2).count()
    quantidade_keystate_1 = general_keys.objects.filter(keystate=1).count()
    quantidade_keystate_0 = general_keys.objects.filter(keystate=0).count()


    quantidade_registros_w10 = general_keys.objects.filter(so__icontains='Windows10')
    quantidade_registros_w10 = quantidade_registros_w10.count()

    data['quantidade_registros_w10'] = quantidade_registros_w10
    data['quantidade_registros_w11'] = quantidade_registros_w11
    data['quantidade_registros'] = quantidade_registros
    data['quantidade_keystate_3'] = quantidade_keystate_3
    data['quantidade_keystate_2'] = quantidade_keystate_2

    if quantidade_registros > 0:
        porcentagem_keystate_2 = round((quantidade_keystate_2 / quantidade_registros) * 100,1)
        porcentagem_keystate_3 = round((quantidade_keystate_3 / quantidade_registros) * 100,1)
        porcentagem_keystate_1 = round((quantidade_keystate_1 / quantidade_registros) * 100, 1)
        porcentagem_keystate_0 = round((quantidade_keystate_0 / quantidade_registros) * 100, 1)
    else:
        porcentagem_keystate_2 = 0
        porcentagem_keystate_3 = 0
        porcentagem_keystate_0 = 0
        porcentagem_keystate_1 = 0

    data['porcentagem_keystate_0'] = porcentagem_keystate_0
    data['porcentagem_keystate_1'] = porcentagem_keystate_1
    data['porcentagem_keystate_2'] = porcentagem_keystate_2
    data['porcentagem_keystate_3'] = porcentagem_keystate_3
    # Adicione esta linha


    return render(request, 'index.html', data)



def form(request):
    data = {}
    data['form'] = keysForm()
    return render(request, 'form.html',data)

def form2(request):
    data = {}
    data['form'] = keysEstoqueWindowsForm()
    return render(request, 'form.html',data)


def duplicadas(request):
    data = {}
    all_items = tabela_Chaves_Duplicadas.objects.all().order_by('-idkey')

    # Aplicar a busca (se existir)
    search = request.GET.get('search')
    if search:
        all_items = all_items.filter(
            Q(pv__icontains=search) | Q(keycontent__icontains=search) | Q(PeCom__icontains=search) | Q(
                Nota_Fiscal__icontains=search) | Q(serialcontent__icontains=search))

        # Atualizar a quantidade de itens por página se a pesquisa for maior que 3000
        if all_items.count() > 100:
            paginator = Paginator(all_items, 5000)
        else:
            paginator = Paginator(all_items, 100)
    else:
        paginator = Paginator(all_items, 100)

    # Restante do código para aplicar a paginação
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data['tabela_Chaves_Duplicadas'] = page_obj


    quantidade_registros = all_items.count()
    quantidade_registros_w11 = tabela_Chaves_Duplicadas.objects.filter(so__icontains='Windows11')
    quantidade_registros_w11 = quantidade_registros_w11.count()

    quantidade_registros_w10 = tabela_Chaves_Duplicadas.objects.filter(so__icontains='Windows10')
    quantidade_registros_w10 = quantidade_registros_w10.count()

    data['quantidade_registros_w10'] = quantidade_registros_w10
    data['quantidade_registros_w11'] = quantidade_registros_w11
    data['quantidade_registros'] = quantidade_registros


    return render(request, 'duplicadas.html', data)

    #teste_backup = general_keys_teste_backup.objects.all()
    #return render(request, 'backup.html',{'teste_backup': teste_backup})



def backup(request):
    data = {}
    all_items = tabela_backup.objects.all().order_by('-idkey')

    # Aplicar a busca (se existir)
    search = request.GET.get('search')
    if search:
        all_items = all_items.filter(Q(pv__icontains=search) | Q(keycontent__icontains=search) | Q(PeCom__icontains=search) | Q(Nota_Fiscal__icontains=search) | Q(serialcontent__icontains=search))

        # Atualizar a quantidade de itens por página se a pesquisa for maior que 3000
        if all_items.count() > 100:
            paginator = Paginator(all_items, 5000)
        else:
            paginator = Paginator(all_items, 100)
    else:
        paginator = Paginator(all_items, 100)

    # Restante do código para aplicar a paginação
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data['tabela_backup'] = page_obj

    quantidade_registros = all_items.count()
    quantidade_registros_w11 = tabela_backup.objects.filter(so__icontains='Windows11')
    quantidade_registros_w11 = quantidade_registros_w11.count()

    quantidade_keystate_3 = tabela_backup.objects.filter(keystate=3).count()
    quantidade_keystate_2 = tabela_backup.objects.filter(keystate=2).count()

    quantidade_registros_w10 = tabela_backup.objects.filter(so__icontains='Windows10')
    quantidade_registros_w10 = quantidade_registros_w10.count()

    data['quantidade_registros_w10'] = quantidade_registros_w10
    data['quantidade_registros_w11'] = quantidade_registros_w11
    data['quantidade_registros'] = quantidade_registros
    data['quantidade_keystate_3'] = quantidade_keystate_3
    data['quantidade_keystate_2'] = quantidade_keystate_2

    if quantidade_registros > 0:
        porcentagem_keystate_2 = round((quantidade_keystate_2 / quantidade_registros) * 100,1)
        porcentagem_keystate_3 = round((quantidade_keystate_3 / quantidade_registros) * 100,1)
    else:
        porcentagem_keystate_2 = 0
        porcentagem_keystate_3 = 0

    data['porcentagem_keystate_2'] = porcentagem_keystate_2
    data['porcentagem_keystate_3'] = porcentagem_keystate_3

    return render(request, 'backup.html', data)

    #teste_backup = general_keys_teste_backup.objects.all()
    #return render(request, 'backup.html',{'teste_backup': teste_backup})

def create(request):
    form = keysForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def deleteAll(request):
    # Filtrar registros com keystate igual a 2 ou 3
    registros_a_backup = general_keys.objects.filter(keystate__in=[2, 3])

    # Salve os registros a serem excluídos na tabela de backup
    tabela_backup.objects.bulk_create(registros_a_backup)

    # Apague os registros com keystate igual a 2 ou 3 da tabela original
    registros_a_backup.delete()

    return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = general_keys.objects.get(pk=pk)
    return render(request,'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = general_keys.objects.get(pk=pk)
    data['form'] = keysForm(instance=data['db'])
    return render(request,'form.html', data)

def insertKeys(request):
    return render(request,'insertKeys.html')

def update(request,pk):
    data = {}
    data['db'] = general_keys.objects.get(pk=pk)
    form = keysForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
def delete(request,pk):
    db = general_keys.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def export_data_to_csv(request):
    # Recupere os dados do banco de dados, substitua com seus próprios modelos e filtros
    data = general_keys.objects.all()

    # Crie uma resposta HTTP com o cabeçalho apropriado para download do CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dados.csv"'

    # Crie um objeto CSVWriter para escrever os dados na resposta
    csv_writer = csv.writer(response)
    csv_writer.writerow(['keycontent','serialcontent',])  # Cabeçalho do CSV

    # Escreva os dados no arquivo CSV
    for item in data:
        csv_writer.writerow([item.keycontent,item.serialcontent, ])  # Substitua com seus próprios campos

    return response


def export_data_to_csv_duplicados(request):
    # Recupere os dados do banco de dados, substitua com seus próprios modelos e filtros
    data = tabela_Chaves_Duplicadas.objects.all()

    # Crie uma resposta HTTP com o cabeçalho apropriado para download do CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dados.csv"'

    # Crie um objeto CSVWriter para escrever os dados na resposta
    csv_writer = csv.writer(response)
    csv_writer.writerow(['pv','keycontent','PeCom','Nota_Fiscal','data_duplicada'])  # Cabeçalho do CSV

    # Escreva os dados no arquivo CSV
    for item in data:
        csv_writer.writerow([item.keycontent,item.PeCom,item.Nota_Fiscal,item.data_duplicada])  # Substitua com seus próprios campos

    return response