# Generated by Django 4.2.3 on 2023-09-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_tabela_estoque_windowskeys_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabela_estoque_windowskeys',
            name='pv',
            field=models.CharField(default='vazio', max_length=50),
        ),
    ]
