# Generated by Django 5.0 on 2024-01-25 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoderApp', '0006_delete_customuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Repuestos',
            new_name='Sugerencias',
        ),
        migrations.RenameField(
            model_name='sugerencias',
            old_name='repuestorequerido',
            new_name='sugerencias',
        ),
    ]