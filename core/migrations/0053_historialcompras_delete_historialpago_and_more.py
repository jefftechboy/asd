# Generated by Django 5.0.6 on 2024-06-26 00:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_alter_compra_usuario_alter_cuenta_fechaingreso_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCompra', models.DateField(default=datetime.datetime(2024, 6, 25, 20, 57, 46, 515014))),
                ('Usuario', models.CharField(max_length=60)),
                ('pdf_file', models.FileField(upload_to='obra')),
            ],
        ),
        migrations.DeleteModel(
            name='HistorialPago',
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 6, 25, 20, 57, 46, 506678)),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 6, 25, 20, 57, 46, 506678)),
        ),
    ]