# Generated by Django 5.0.6 on 2024-05-25 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_autentificacion_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fechaCompra',
            field=models.DateField(default=datetime.datetime(2024, 5, 25, 12, 8, 34, 416415)),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 5, 25, 12, 8, 34, 415310)),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 5, 25, 12, 8, 34, 416415)),
        ),
    ]