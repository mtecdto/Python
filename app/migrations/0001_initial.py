# Generated by Django 4.2.3 on 2023-08-13 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='general_keys',
            fields=[
                ('idkey', models.AutoField(primary_key=True, serialize=False)),
                ('pv', models.CharField(max_length=50)),
                ('keycontent', models.CharField(max_length=29)),
                ('serialcontent', models.CharField(max_length=30)),
                ('keystate', models.IntegerField(default=0)),
                ('bancada', models.CharField(max_length=2)),
                ('disco', models.IntegerField(default=0)),
                ('memoria', models.IntegerField(default=0)),
                ('data', models.DateField(auto_now_add=True)),
                ('so', models.CharField(choices=[('Windows10', 'Opção 1'), ('Windows11', 'Opção 2')], max_length=100)),
                ('marca', models.CharField(choices=[('Lenovo', 'Lenovo'), ('Acer', 'Acer'), ('Samsung', 'Samsung'), ('Sony Vaio', 'Sony Vaio'), ('Dell', 'Dell')], default='vazio', max_length=100)),
                ('modelo', models.CharField(choices=[('E-14', 'E-14'), ('T-14', 'T-14'), ('K-14', 'K-14'), ('IdeaPad', 'IdeaPad'), ('ThinkPad', 'ThinkPad'), ('Nitro5', 'Nitro5'), ('Aspire3', 'Aspire3'), ('Aspire5', 'Aspire5'), ('SamsungBook', 'SamsungBook'), ('GalaxyBook', 'GalaxyBook'), ('GalaxyBook2', 'GalaxyBook2'), ('SonyVaio', 'SonyVaio'), ('DellVostro', 'DellVostro'), ('DellInspiron', 'DellInspiron'), ('P-340', 'P-340'), ('P-360\t', 'P-360'), ('P-620', 'P-620'), ('M-710S', 'M-710S'), ('M-720S', 'M-720S'), ('M-75Q', 'M-75Q'), ('M-75S', 'M-75S'), ('M-70Q', 'M-70Q'), ('M-80S', 'M-80S'), ('M-80Q', 'M-80Q')], default='vazio', max_length=100)),
            ],
            options={
                'db_table': 'general_keys',
            },
        ),
        migrations.CreateModel(
            name='tabela_backup',
            fields=[
                ('idkey', models.AutoField(primary_key=True, serialize=False)),
                ('pv', models.CharField(max_length=50)),
                ('keycontent', models.CharField(max_length=29)),
                ('serialcontent', models.CharField(max_length=30)),
                ('keystate', models.IntegerField()),
                ('bancada', models.CharField(max_length=2)),
                ('disco', models.IntegerField()),
                ('memoria', models.IntegerField()),
                ('data', models.DateField()),
                ('so', models.CharField(default='vazio', max_length=100)),
                ('marca', models.CharField(default='vazio', max_length=100)),
                ('modelo', models.CharField(default='vazio', max_length=100)),
            ],
            options={
                'db_table': 'tabela_backup',
            },
        ),
    ]
