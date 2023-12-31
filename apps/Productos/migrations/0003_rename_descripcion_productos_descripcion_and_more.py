# Generated by Django 4.2.2 on 2023-08-01 16:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0002_rename_descripción_productos_descripcion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='Descripcion',
            new_name='descripcion',
        ),
        migrations.RemoveField(
            model_name='productos',
            name='Cantidad_Productos',
        ),
        migrations.RemoveField(
            model_name='productos',
            name='Valor',
        ),
        migrations.AddField(
            model_name='productos',
            name='cantidad_productos',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productos',
            name='valor',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
