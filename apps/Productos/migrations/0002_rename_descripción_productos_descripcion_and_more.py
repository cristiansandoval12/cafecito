# Generated by Django 4.2.1 on 2023-06-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='Descripción',
            new_name='Descripcion',
        ),
        migrations.AlterField(
            model_name='productos',
            name='Cantidad_Productos',
            field=models.IntegerField(),
        ),
    ]
