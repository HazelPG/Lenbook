# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-29 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombres_A', models.CharField(max_length=80)),
                ('Apellidos_A', models.CharField(max_length=80)),
                ('Especialidad', models.CharField(max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_libro', models.CharField(max_length=100, null=True)),
                ('Numero_Serie', models.CharField(blank=True, max_length=100, null=True)),
                ('Estado_libro', models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('EN MANTENIMIENTO', 'EN MANTENIMIENTO'), ('DADO DE BAJA POR PERDIDA', 'DADO DE BAJA POR PERDIDA'), ('DADO DE BAJA POR DAÑO TOTAL', 'DADO DE BAJA POR DAÑO TOTAL')], default='ACTIVO', max_length=40)),
                ('fecha_registro', models.DateField(default=django.utils.timezone.now)),
                ('Autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='libros.Autores')),
            ],
            options={
                'verbose_name_plural': 'Libros',
            },
        ),
        migrations.CreateModel(
            name='Tipolibro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_libro', models.CharField(max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tipo De Libros',
            },
        ),
        migrations.AddField(
            model_name='libro',
            name='tipo_de_libro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='libros.Tipolibro'),
        ),
    ]