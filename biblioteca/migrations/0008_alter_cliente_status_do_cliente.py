# Generated by Django 5.0.6 on 2024-05-28 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0007_alter_cliente_status_do_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Status_do_Cliente',
            field=models.CharField(blank=True, choices=[('pago', 'Pago'), ('em debito', 'Em Débito')], max_length=50, null=True),
        ),
    ]
