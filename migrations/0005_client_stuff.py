# Generated by Django 3.0.7 on 2020-07-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clilibapp', '0004_auto_20200715_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='stuff',
            field=models.BooleanField(default=False, verbose_name='Клиент для внутренних нужд'),
        ),
    ]
