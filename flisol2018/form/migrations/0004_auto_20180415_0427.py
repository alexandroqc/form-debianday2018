# Generated by Django 2.0.4 on 2018-04-15 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20180415_0425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participante',
            old_name='conoce_flisol',
            new_name='conoce_el_flisol',
        ),
        migrations.RenameField(
            model_name='participante',
            old_name='conoce_software_libre',
            new_name='conoce_el_software_libre',
        ),
        migrations.RenameField(
            model_name='participante',
            old_name='tipo_participacion',
            new_name='tipo_de_participacion',
        ),
    ]