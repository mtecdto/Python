# Generated by Django 4.2.3 on 2023-09-20 15:08

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_tabela_estoque_windowskeys_pv'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabela_estoque_windowskeys',
            name='Nota_Fiscal',
            field=models.CharField(default=datetime.datetime(2023, 9, 20, 15, 8, 17, 87876, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tabela_estoque_windowskeys',
            name='PeCom',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
