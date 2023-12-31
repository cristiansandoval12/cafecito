# Generated by Django 4.2.1 on 2023-08-01 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=12)),
                ('direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ventas', models.DateTimeField(auto_now_add=True)),
                ('valor', models.IntegerField()),
                ('cantidad', models.CharField(max_length=1000)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.cliente')),
            ],
        ),
    ]
