# Generated by Django 4.1.1 on 2022-09-12 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaAPI', '0010_rename_longitude_paciente_longitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='birthday',
            field=models.CharField(max_length=20),
        ),
    ]
