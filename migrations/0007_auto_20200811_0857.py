# Generated by Django 3.0.7 on 2020-08-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clilibapp', '0006_auto_20200804_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contract_number',
            field=models.CharField(default=0, max_length=100, null=True, verbose_name='Номер контракта'),
        ),
        migrations.AlterField(
            model_name='client',
            name='orgname',
            field=models.CharField(default='OrgName', max_length=50, verbose_name='Название организации в vCloud'),
        ),
    ]
