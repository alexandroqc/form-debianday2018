# Generated by Django 2.0.4 on 2018-04-15 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participante',
            old_name='conoce_sofware_libre',
            new_name='conoce_software_libre',
        ),
    ]
