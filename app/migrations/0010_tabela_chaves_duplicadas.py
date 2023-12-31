# Generated by Django 4.2.3 on 2023-09-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_general_keys_nota_fiscal_general_keys_pecom_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tabela_Chaves_Duplicadas',
            fields=[
                ('idkey', models.AutoField(primary_key=True, serialize=False)),
                ('pv', models.CharField(default='vazio', max_length=50)),
                ('keycontent', models.CharField(max_length=29)),
                ('serialcontent', models.CharField(max_length=30)),
                ('keystate', models.IntegerField(default=0)),
                ('bancada', models.CharField(max_length=2)),
                ('disco', models.IntegerField(default=0)),
                ('memoria', models.IntegerField(default=0)),
                ('data', models.DateField(auto_now_add=True)),
                ('so', models.CharField(default='vazio', max_length=100)),
                ('marca', models.CharField(default='vazio', max_length=100)),
                ('modelo', models.CharField(default='vazio', max_length=100)),
                ('Nota_Fiscal', models.CharField(max_length=100)),
                ('PeCom', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tabela_Chaves_Duplicadas',
            },
        ),
    ]
