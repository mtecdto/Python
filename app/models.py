from django.db import models


# Create your models here.
class general_keys(models.Model):
    OPCAO_1 = 'Windows10'
    OPCAO_2 = 'Windows11'

    OPCOES = [
        (OPCAO_1, 'Opção 1'),
        (OPCAO_2, 'Opção 2'),
    ]

    MARCA_OPCAO_1 = 'Lenovo'
    MARCA_OPCAO_2 = 'Acer'
    MARCA_OPCAO_3 = 'Samsung'
    MARCA_OPCAO_4 = 'Sony Vaio'
    MARCA_OPCAO_5 = 'Dell'

    OUTRAS_OPCOES = [
        (MARCA_OPCAO_1, 'Lenovo'),
        (MARCA_OPCAO_2, 'Acer'),
        (MARCA_OPCAO_3, 'Samsung'),
        (MARCA_OPCAO_4, 'Sony Vaio'),
        (MARCA_OPCAO_5, 'Dell'),
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
    MODELO_OPCAO_12 = 'SonyVaio'
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

    MODELO_OPCOES = [
        (MODELO_OPCAO_1, 'E-14'),
        (MODELO_OPCAO_2, 'T-14'),
        (MODELO_OPCAO_3, 'K-14'),
        (MODELO_OPCAO_4, 'IdeaPad'),
        (MODELO_OPCAO_5, 'ThinkPad'),
        (MODELO_OPCAO_6,'Nitro5'),
        (MODELO_OPCAO_7,'Aspire3'),
        (MODELO_OPCAO_8,'Aspire5'),
        (MODELO_OPCAO_9,'SamsungBook'),
        (MODELO_OPCAO_10,'GalaxyBook'),
        (MODELO_OPCAO_11,'GalaxyBook2'),
        (MODELO_OPCAO_12,'SonyVaio'),
        (MODELO_OPCAO_13,'DellVostro'),
        (MODELO_OPCAO_14,'DellInspiron'),
        (MODELO_OPCAO_15,'P-340'),
        (MODELO_OPCAO_16,'P-360'),
        (MODELO_OPCAO_17,'P-620'),
        (MODELO_OPCAO_18,'M-710S'),
        (MODELO_OPCAO_19,'M-720S'),
        (MODELO_OPCAO_20,'M-75Q'),
        (MODELO_OPCAO_21,'M-75S'),
        (MODELO_OPCAO_22,'M-70Q'),
        (MODELO_OPCAO_23,'M-80S'),
        (MODELO_OPCAO_24,'M-80Q'),
        (MODELO_OPCAO_25,'V15'),
    ]

    idkey = models.AutoField(primary_key=True)
    pv = models.CharField(max_length=50)
    Nota_Fiscal = models.CharField(max_length=100)
    PeCom = models.CharField(max_length=100)
    keycontent = models.CharField(max_length=29, unique=True)
    serialcontent = models.CharField(max_length=30)
    keystate = models.IntegerField(default=0)
    bancada = models.CharField(max_length=2)
    disco = models.IntegerField(default=0)
    memoria = models.IntegerField(default=0)
    data = models.DateField(auto_now_add=True)
    so = models.CharField(max_length=100,choices=OPCOES)
    marca = models.CharField(max_length=100,choices=OUTRAS_OPCOES,default='vazio')
    uf = models.CharField(max_length=100, default='vazio')
    modelo = models.CharField(max_length=100,choices=MODELO_OPCOES,default='vazio')

    class Meta:
        db_table = 'general_keys'

class tabela_backup(models.Model):
    idkey = models.AutoField(primary_key=True)
    pv = models.CharField(max_length=50)
    Nota_Fiscal = models.CharField(max_length=100)
    PeCom = models.CharField(max_length=100)
    keycontent = models.CharField(max_length=29, unique=True)
    serialcontent = models.CharField(max_length=30)
    keystate = models.IntegerField()
    bancada = models.CharField(max_length=2)
    disco = models.IntegerField()
    memoria = models.IntegerField()
    data = models.DateField()
    so = models.CharField(max_length=100,default='vazio')
    uf = models.CharField(max_length=100, default='vazio')
    marca = models.CharField(max_length=100, default='vazio')
    modelo = models.CharField(max_length=100, default='vazio')
    class Meta:
        db_table = 'tabela_backup'

class tabela_Estoque_WindowsKeys(models.Model):
    idkey = models.AutoField(primary_key=True)
    pv = models.CharField(max_length=50, default='vazio')
    keycontent = models.CharField(max_length=29, unique=True)
    serialcontent = models.CharField(max_length=30)
    keystate = models.IntegerField(default=0)
    bancada = models.CharField(max_length=2)
    disco = models.IntegerField(default=0)
    memoria = models.IntegerField(default=0)
    data = models.DateField(auto_now_add=True)
    so = models.CharField(max_length=100,default='vazio')
    uf = models.CharField(max_length=100, default='vazio')
    marca = models.CharField(max_length=100, default='vazio')
    modelo = models.CharField(max_length=100, default='vazio')
    Nota_Fiscal = models.CharField(max_length=100)
    PeCom = models.CharField(max_length=100)
    class Meta:
        db_table = 'tabela_Estoque_WindowsKeys'

class tabela_Chaves_Duplicadas(models.Model):
    idkey = models.AutoField(primary_key=True)
    pv = models.CharField(max_length=50, default='vazio')
    keycontent = models.CharField(max_length=29)
    serialcontent = models.CharField(max_length=30)
    keystate = models.IntegerField(default=0)
    bancada = models.CharField(max_length=2)
    disco = models.IntegerField(default=0)
    memoria = models.IntegerField(default=0)
    data = models.DateField(auto_now_add=True)
    data_duplicada = models.CharField(max_length=50, default='vazio')
    so = models.CharField(max_length=100,default='vazio')
    uf = models.CharField(max_length=100, default='vazio')
    marca = models.CharField(max_length=100, default='vazio')
    modelo = models.CharField(max_length=100, default='vazio')
    Nota_Fiscal = models.CharField(max_length=100)
    PeCom = models.CharField(max_length=100)
    class Meta:
        db_table = 'tabela_Chaves_Duplicadas'


class quantidade_maquinas(models.Model):
    id = models.AutoField(primary_key=True)
    quantidade = models.IntegerField(null=False)
    pv = models.CharField(null=False,max_length=20)
    class Meta:
        db_table = 'quantidade_maquinas'


class general_keys_office(models.Model):
    idkey = models.AutoField(primary_key=True)
    pv = models.CharField(max_length=50)
    Nota_Fiscal = models.CharField(max_length=100)
    PeCom = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=128)
    keycontent = models.CharField(max_length=29, unique=True)
    serialcontent = models.CharField(max_length=30)
    keystate = models.IntegerField()
    bancada = models.CharField(max_length=2)
    disco = models.IntegerField()
    memoria = models.IntegerField()
    data = models.DateField(auto_now_add=True)
    version_office = models.CharField(max_length=100,default='vazio')
    uf = models.CharField(max_length=100, default='vazio')
    marca = models.CharField(max_length=100, default='vazio')
    modelo = models.CharField(max_length=100, default='vazio')
    class Meta:
        db_table = 'general_keys_office'


class estoque_office(models.Model):
    idkey = models.AutoField(primary_key=True)
    Nota_Fiscal = models.CharField(max_length=100)
    PeCom = models.CharField(max_length=100)
    keycontent = models.CharField(max_length=29, unique=True)
    data = models.DateField(auto_now_add=True)
    uf = models.CharField(max_length=100, default='vazio')
    class Meta:
        db_table = 'estoque_office'



class tabela_backup_office(models.Model):
    idkey = models.AutoField(primary_key=True)
    pv = models.CharField(max_length=50)
    Nota_Fiscal = models.CharField(max_length=100)
    PeCom = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=128)
    keycontent = models.CharField(max_length=29, unique=True)
    serialcontent = models.CharField(max_length=30)
    keystate = models.IntegerField()
    bancada = models.CharField(max_length=2)
    disco = models.IntegerField()
    memoria = models.IntegerField()
    data = models.DateField()
    version_office = models.CharField(max_length=100,default='vazio')
    uf = models.CharField(max_length=100, default='vazio')
    marca = models.CharField(max_length=100, default='vazio')
    modelo = models.CharField(max_length=100, default='vazio')
    class Meta:
        db_table = 'tabela_backup_office'

class tabela_Chaves_Duplicadas_Office(models.Model):
    idkey = models.AutoField(primary_key=True)
    pv = models.CharField(max_length=50, default='vazio')
    keycontent = models.CharField(max_length=29)
    serialcontent = models.CharField(max_length=30)
    keystate = models.IntegerField(default=0)
    bancada = models.CharField(max_length=2)
    disco = models.IntegerField(default=0)
    memoria = models.IntegerField(default=0)
    data = models.DateField(auto_now_add=True)
    data_duplicada = models.CharField(max_length=50, default='vazio')
    so = models.CharField(max_length=100,default='vazio')
    uf = models.CharField(max_length=100, default='vazio')
    marca = models.CharField(max_length=100, default='vazio')
    modelo = models.CharField(max_length=100, default='vazio')
    Nota_Fiscal = models.CharField(max_length=100)
    PeCom = models.CharField(max_length=100)
    class Meta:
        db_table = 'tabela_Chaves_Duplicadas_Office'





