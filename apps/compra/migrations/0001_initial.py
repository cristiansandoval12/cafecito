# Generated by Django 4.2.1 on 2023-06-22 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
                ('telefono', models.CharField(max_length=1000)),
                ('direccion', models.CharField(max_length=1000)),
                ('correo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_compra', models.IntegerField()),
                ('valor', models.IntegerField()),
                ('cantidad', models.CharField(max_length=1000)),
                ('fecha_compra', models.DateField()),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compra.proveedor')),
            ],
        ),
    ]
