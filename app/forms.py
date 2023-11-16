from django.forms import ModelForm
from app.models import general_keys,tabela_Estoque_WindowsKeys,quantidade_maquinas

from django import forms

class quantidade_maquinasForm(ModelForm):
    class Meta:
        model = quantidade_maquinas
        fields = ['quantidade']


class keysForm(ModelForm):
    class Meta:
        model = general_keys
        fields = ['pv','serialcontent','keystate']

class keysEstoqueWindowsForm(ModelForm):
    class Meta:
        model = tabela_Estoque_WindowsKeys
        fields = ['idkey','pv','keycontent','serialcontent','keystate','bancada','disco','memoria','uf','Nota_Fiscal','PeCom']

class GeneralKeyForm(forms.Form):
    OPCAO_1 = 'Windows10'
    OPCAO_2 = 'Windows11'

    OPCOES = [
        (OPCAO_1, 'Windows10'),
        (OPCAO_2, 'Windows11'),
    ]
    MODELO_OPCAO_1 = 'E-14'
    MODELO_OPCAO_2 = 'T-14'
    MODELO_OPCAO_3 = 'K-14'
    MODELO_OPCAO_4 = 'IdeaPad'
    MODELO_OPCAO_5 = 'ThinkPad'
    MODELO_OPCAO_6 = 'Nitro5'
    MODELO_OPCAO_7 = 'Aspire3'
    MODELO_OPCAO_8 = 'Aspire5'
    MODELO_OPCAO_9 = 'SamsungBook'
    MODELO_OPCAO_10 = 'GalaxyBook'
    MODELO_OPCAO_11 = 'GalaxyBook2'
    MODELO_OPCAO_12 = 'Vaio'
    MODELO_OPCAO_13 = 'DellVostro'
    MODELO_OPCAO_14 = 'DellInspiron'
    MODELO_OPCAO_15 = 'P-340'
    MODELO_OPCAO_16 = 'P-360	'
    MODELO_OPCAO_17 = 'P-620'
    MODELO_OPCAO_18 = 'M-710S'
    MODELO_OPCAO_19 = 'M-720S'
    MODELO_OPCAO_20 = 'M-75Q'
    MODELO_OPCAO_21 = 'M-75S'
    MODELO_OPCAO_22 = 'M-70Q'
    MODELO_OPCAO_23 = 'M-80S'
    MODELO_OPCAO_24 = 'M-80Q'
    MODELO_OPCAO_25 = 'V15'
    MODELO_OPCAO_26 = 'FE14'
    MODELO_OPCAO_27 = 'FE15'
    MODELO_OPCAO_28 = 'AllInOneConcordia'


    MODELO_OPCOES = [
        (MODELO_OPCAO_1, 'E-14'),
        (MODELO_OPCAO_2, 'T-14'),
        (MODELO_OPCAO_3, 'K-14'),
        (MODELO_OPCAO_4, 'IdeaPad'),
        (MODELO_OPCAO_5, 'ThinkPad'),
        (MODELO_OPCAO_6, 'Nitro5'),
        (MODELO_OPCAO_7, 'Aspire3'),
        (MODELO_OPCAO_8, 'Aspire5'),
        (MODELO_OPCAO_9, 'SamsungBook'),
        (MODELO_OPCAO_10, 'GalaxyBook'),
        (MODELO_OPCAO_11, 'GalaxyBook2'),
        (MODELO_OPCAO_12, 'Vaio'),
        (MODELO_OPCAO_13, 'DellVostro'),
        (MODELO_OPCAO_14, 'DellInspiron'),
        (MODELO_OPCAO_15, 'P-340'),
        (MODELO_OPCAO_16, 'P-360'),
        (MODELO_OPCAO_17, 'P-620'),
        (MODELO_OPCAO_18, 'M-710S'),
        (MODELO_OPCAO_19, 'M-720S'),
        (MODELO_OPCAO_20, 'M-75Q'),
        (MODELO_OPCAO_21, 'M-75S'),
        (MODELO_OPCAO_22, 'M-70Q'),
        (MODELO_OPCAO_23, 'M-80S'),
        (MODELO_OPCAO_24, 'M-80Q'),
        (MODELO_OPCAO_25, 'V15'),
        (MODELO_OPCAO_26, 'FE14'),
        (MODELO_OPCAO_27, 'FE15'),
        (MODELO_OPCAO_28, 'AllInOneConcordia'),
    ]

    MARCA_OPCAO_1 = 'Lenovo'
    MARCA_OPCAO_2 = 'Acer'
    MARCA_OPCAO_3 = 'Samsung'
    MARCA_OPCAO_4 = 'Vaio'
    MARCA_OPCAO_5 = 'Dell'
    MARCA_OPCAO_6 = 'Asus'
    MARCA_OPCAO_7 = 'Compaq'
    MARCA_OPCAO_8 = 'Concordia'
    MARCA_OPCAO_9 = 'Intel'
    MARCA_OPCAO_10 = 'LG'
    MARCA_OPCAO_11 = 'Positivo'
    MARCA_OPCAO_12 = 'Teravix'

    MARCA_OPCOES = [
        (MARCA_OPCAO_1, 'Lenovo'),
        (MARCA_OPCAO_2, 'Acer'),
        (MARCA_OPCAO_3, 'Samsung'),
        (MARCA_OPCAO_4, 'Vaio'),
        (MARCA_OPCAO_5, 'Dell'),
        (MARCA_OPCAO_6, 'Asus'),
        (MARCA_OPCAO_7, 'Compaq'),
        (MARCA_OPCAO_8, 'Concordia'),
        (MARCA_OPCAO_9, 'Intel'),
        (MARCA_OPCAO_10, 'LG'),
        (MARCA_OPCAO_11, 'Positivo'),
        (MARCA_OPCAO_12, 'Teravix'),

    ]

    UF_1 = 'DF'
    UF_2 = 'ES'

    OPCOESUF = [
        (UF_1, 'DF'),
        (UF_2, 'ES'),
    ]

    chaves = forms.CharField(widget=forms.Textarea)
    pv = forms.CharField(max_length=100)
    Nota_Fiscal = forms.CharField(max_length=100)
    PeCom = forms.CharField(max_length=100)
    so = forms.ChoiceField(choices=OPCOES)
    uf = forms.ChoiceField(choices=OPCOESUF)
    marca = forms.ChoiceField(choices=MARCA_OPCOES)
    modelo = forms.ChoiceField(choices=MODELO_OPCOES)

class EstoqueWindowsForm(forms.Form):
    OPCAO_1 = 'Windows10'
    OPCAO_2 = 'Windows11'
    OPCAO_3 = 'Windows10-ETQ'
    OPCAO_4 = 'Windows11-ETQ'
    OPCAO_5 = 'Office'

    OPCOES = [
        (OPCAO_1, 'Windows10'),
        (OPCAO_2, 'Windows11'),
        (OPCAO_3, 'Windows10-ETQ'),
        (OPCAO_4, 'Windows11-ETQ'),
        (OPCAO_5, 'Office'),
    ]

    UF_1 = 'DF'
    UF_2 = 'ES'

    OPCOESUF = [
        (UF_1, 'DF'),
        (UF_2, 'ES'),
    ]
    chaves = forms.CharField(widget=forms.Textarea)
    Nota_Fiscal = forms.CharField(max_length=100)
    PeCom = forms.CharField(max_length=100)
    so = forms.ChoiceField(choices=OPCOES)
    uf = forms.ChoiceField(choices=OPCOESUF)





class InserirChavesForm(forms.Form):
    OPCAO_1 = 'Windows10'
    OPCAO_2 = 'Windows11'
    OPCAO_3 = 'Windows10-ETQ'
    OPCAO_4 = 'Windows11-ETQ'
    OPCAO_5 = 'Office'

    OPCOES = [
        (OPCAO_1, 'Windows10'),
        (OPCAO_2, 'Windows11'),
        (OPCAO_3, 'Windows10-ETQ'),
        (OPCAO_4, 'Windows11-ETQ'),
        (OPCAO_5, 'Office'),
    ]
    MODELO_OPCAO_1 = 'E-14'
    MODELO_OPCAO_2 = 'T-14'
    MODELO_OPCAO_3 = 'K-14'
    MODELO_OPCAO_4 = 'IdeaPad'
    MODELO_OPCAO_5 = 'ThinkPad'
    MODELO_OPCAO_6 = 'Nitro5'
    MODELO_OPCAO_7 = 'Aspire3'
    MODELO_OPCAO_8 = 'Aspire5'
    MODELO_OPCAO_9 = 'SamsungBook'
    MODELO_OPCAO_10 = 'GalaxyBook'
    MODELO_OPCAO_11 = 'GalaxyBook2'
    MODELO_OPCAO_12 = 'Vaio'
    MODELO_OPCAO_13 = 'DellVostro'
    MODELO_OPCAO_14 = 'DellInspiron'
    MODELO_OPCAO_15 = 'P-340'
    MODELO_OPCAO_16 = 'P-360	'
    MODELO_OPCAO_17 = 'P-620'
    MODELO_OPCAO_18 = 'M-710S'
    MODELO_OPCAO_19 = 'M-720S'
    MODELO_OPCAO_20 = 'M-75Q'
    MODELO_OPCAO_21 = 'M-75S'
    MODELO_OPCAO_22 = 'M-70Q'
    MODELO_OPCAO_23 = 'M-80S'
    MODELO_OPCAO_24 = 'M-80Q'
    MODELO_OPCAO_25 = 'V15'
    MODELO_OPCAO_26 = 'FE14'
    MODELO_OPCAO_27 = 'FE15'
    MODELO_OPCAO_28 = 'AllInOneConcordia'
    MODELO_OPCAO_29 = 'Neo50'


    MODELO_OPCOES = [
        (MODELO_OPCAO_1, 'E-14'),
        (MODELO_OPCAO_2, 'T-14'),
        (MODELO_OPCAO_3, 'K-14'),
        (MODELO_OPCAO_4, 'IdeaPad'),
        (MODELO_OPCAO_5, 'ThinkPad'),
        (MODELO_OPCAO_6, 'Nitro5'),
        (MODELO_OPCAO_7, 'Aspire3'),
        (MODELO_OPCAO_8, 'Aspire5'),
        (MODELO_OPCAO_9, 'SamsungBook'),
        (MODELO_OPCAO_10, 'GalaxyBook'),
        (MODELO_OPCAO_11, 'GalaxyBook2'),
        (MODELO_OPCAO_12, 'Vaio'),
        (MODELO_OPCAO_13, 'DellVostro'),
        (MODELO_OPCAO_14, 'DellInspiron'),
        (MODELO_OPCAO_15, 'P-340'),
        (MODELO_OPCAO_16, 'P-360'),
        (MODELO_OPCAO_17, 'P-620'),
        (MODELO_OPCAO_18, 'M-710S'),
        (MODELO_OPCAO_19, 'M-720S'),
        (MODELO_OPCAO_20, 'M-75Q'),
        (MODELO_OPCAO_21, 'M-75S'),
        (MODELO_OPCAO_22, 'M-70Q'),
        (MODELO_OPCAO_23, 'M-80S'),
        (MODELO_OPCAO_24, 'M-80Q'),
        (MODELO_OPCAO_25, 'V15'),
        (MODELO_OPCAO_26, 'FE14'),
        (MODELO_OPCAO_27, 'FE15'),
        (MODELO_OPCAO_28, 'AllInOneConcordia'),
        (MODELO_OPCAO_29, 'Neo50'),
    ]

    MARCA_OPCAO_1 = 'Lenovo'
    MARCA_OPCAO_2 = 'Acer'
    MARCA_OPCAO_3 = 'Samsung'
    MARCA_OPCAO_4 = 'Vaio'
    MARCA_OPCAO_5 = 'Dell'
    MARCA_OPCAO_6 = 'Asus'
    MARCA_OPCAO_7 = 'Compaq'
    MARCA_OPCAO_8 = 'Concordia'
    MARCA_OPCAO_9 = 'Intel'
    MARCA_OPCAO_10 = 'LG'
    MARCA_OPCAO_11 = 'Positivo'
    MARCA_OPCAO_12 = 'Teravix'

    MARCA_OPCOES = [
        (MARCA_OPCAO_1, 'Lenovo'),
        (MARCA_OPCAO_2, 'Acer'),
        (MARCA_OPCAO_3, 'Samsung'),
        (MARCA_OPCAO_4, 'Vaio'),
        (MARCA_OPCAO_5, 'Dell'),
        (MARCA_OPCAO_6, 'Asus'),
        (MARCA_OPCAO_7, 'Compaq'),
        (MARCA_OPCAO_8, 'Concordia'),
        (MARCA_OPCAO_9, 'Intel'),
        (MARCA_OPCAO_10, 'LG'),
        (MARCA_OPCAO_11, 'Positivo'),
        (MARCA_OPCAO_12, 'Teravix'),

    ]
    numero_de_chaves = forms.IntegerField(min_value=1, label='Número de Chaves a Inserir')
    novo_pv = forms.CharField(max_length=50, label='Novo PV')  # Adicione este campo
    marca = forms.ChoiceField(choices=MARCA_OPCOES)
    modelo = forms.ChoiceField(choices=MODELO_OPCOES)
    so = forms.ChoiceField(choices=OPCOES)












