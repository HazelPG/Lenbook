# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now


class Tipolibro(models.Model):

    class Meta:
        verbose_name_plural = "Tipo De Libros"

    tipo_libro = models.CharField(max_length=30, null=True)
    def __str__(self):
        return str(self.tipo_libro)

class Autores(models.Model):

    class Meta:
        verbose_name_plural = "Autores"

    Nombres_A = models.CharField(max_length=80)
    Apellidos_A = models.CharField(max_length=80)
    Especialidad = models.CharField(max_length=30, null=True)
    def __str__(self):
        return str(self.Nombres_A)

class Libro(models.Model):
    ESTADO = (
        ('ACTIVO', 'ACTIVO'),
        ('EN MANTENIMIENTO', 'EN MANTENIMIENTO'),
        ('DADO DE BAJA POR PERDIDA', 'DADO DE BAJA POR PERDIDA'),
        ('DADO DE BAJA POR DAÑO TOTAL', 'DADO DE BAJA POR DAÑO TOTAL'),
    )
    class Meta:
        verbose_name_plural = "Libros"

    tipo_de_libro = models.ForeignKey(Tipolibro, null=True)
    Autor = models.ForeignKey(Autores, null=True)
    nombre_libro = models.CharField(max_length=100, null=True)
    Numero_Serie = models.CharField(max_length=100, null=True,blank=True)
    Estado_libro = models.CharField(max_length=40, choices=ESTADO,default="ACTIVO")
    fecha_registro = models.DateField(default=now)

    def __str__(self):
        return str(self.nombre_libro)
