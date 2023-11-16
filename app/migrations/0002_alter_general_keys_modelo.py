# Generated by Django 4.2.3 on 2023-08-28 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general_keys',
            name='modelo',
            field=models.CharField(choices=[('E-14', 'E-14'), ('T-14', 'T-14'), ('K-14', 'K-14'), ('IdeaPad', 'IdeaPad'), ('ThinkPad', 'ThinkPad'), ('Nitro5', 'Nitro5'), ('Aspire3', 'Aspire3'), ('Aspire5', 'Aspire5'), ('SamsungBook', 'SamsungBook'), ('GalaxyBook', 'GalaxyBook'), ('GalaxyBook2', 'GalaxyBook2'), ('SonyVaio', 'SonyVaio'), ('DellVostro', 'DellVostro'), ('DellInspiron', 'DellInspiron'), ('P-340', 'P-340'), ('P-360\t', 'P-360'), ('P-620', 'P-620'), ('M-710S', 'M-710S'), ('M-720S', 'M-720S'), ('M-75Q', 'M-75Q'), ('M-75S', 'M-75S'), ('M-70Q', 'M-70Q'), ('M-80S', 'M-80S'), ('M-80Q', 'M-80Q'), ('V15', 'V15')], default='vazio', max_length=100),
        ),
    ]
