# Generated by Django 4.2.2 on 2023-08-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_alter_cliente_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.BigIntegerField(),
        ),
    ]
