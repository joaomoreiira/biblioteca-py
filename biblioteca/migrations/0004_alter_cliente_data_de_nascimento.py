# Generated by Django 5.0.6 on 2024-05-28 00:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_cliente_data_de_cadastro_cliente_data_de_devolução_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Data_de_Nascimento',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]