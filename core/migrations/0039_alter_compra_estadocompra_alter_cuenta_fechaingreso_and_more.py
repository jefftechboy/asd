# Generated by Django 5.0.6 on 2024-06-21 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_alter_autentificacion_imagenautentificacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='estadoCompra',
            field=models.CharField(default='Carrito', max_length=60),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 6, 21, 17, 57, 31, 522333)),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 6, 21, 17, 57, 31, 522333)),
        ),
    ]
