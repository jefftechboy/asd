# Generated by Django 5.0.6 on 2024-06-19 16:00

import cloudinary.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_alter_compra_obra_alter_cuenta_fechaingreso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autentificacion',
            name='imagenAutentificacion',
            field=cloudinary.models.CloudinaryField(default=2, max_length=255, verbose_name='imagen'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 6, 19, 12, 0, 35, 257571)),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 6, 19, 12, 0, 35, 258572)),
        ),
        migrations.AlterField(
            model_name='obra',
            name='imagen',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagen'),
        ),
    ]