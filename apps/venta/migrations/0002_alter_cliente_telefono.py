# Generated by Django 4.2.2 on 2023-08-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.BigIntegerField(),
        ),
    ]
