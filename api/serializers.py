# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from configuracion.models import Programa
from libros.models import Tipolibro, Libro, Autores
from personas.models import Personas,TipoPersona
from prestamos.models import Prestamo, Incidente, DetallePrestamo, DetalleIncidente
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
import django_filters.rest_framework as filters

class TipoPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPersona
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','get_full_name', 'username')
        read_only_fields = ('get_full_name', 'email', 'username')

class Tipo_libroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipolibro
        fields = "__all__"

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autores
        fields = "__all__"

class LibroSerializer(serializers.ModelSerializer):
    Autor = AutorSerializer(read_only=True)
    AutorId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Autores.objects.all(), source='Autor')
    class Meta:
        model = Libro
        fields = ('id', 'tipo_de_libro','Autor','AutorId', 'nombre_libro', 'Numero_Serie', 'Estado_libro','fecha_registro')
        #fields = ('Id_recurso','tipo_de_recurso','Marca','nombre_recurso','referencia','Estado_Recurso','fecha_registro','Detalle_Prestamo')

class DetalleIncidenteSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    UsuarioId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='usuario')

    class Meta:
        model = DetalleIncidente
        fields =  ('id','Incidente', 'Fecha','Hora','descripcion','usuario','UsuarioId')

class IncidenteSerializer(serializers.ModelSerializer):
    detalleincidente = DetalleIncidenteSerializer(many=True,write_only=True)
    detailincidente = DetalleIncidenteSerializer(many=True, read_only=True, source='detalleincidente_set')
    class Meta:
        model = Incidente
        fields = ('Id_Incidente','usuario', 'Persona','Tipo_Incidente','Fecha_Incidente','Libro','Prestamo_detalle','Estado','detalleincidente','detailincidente')

    def create(self, validated_data):
        detalleincidente_data = validated_data.pop('detalleincidente')
        incidente = Incidente.objects.create(**validated_data)
        for Detallei_data in detalleincidente_data:
            DetalleIncidente.objects.create(Incidente=incidente,**Detallei_data)
        return incidente

class DetallePrestamoSerializer(serializers.ModelSerializer):
    Usuario_devolucion = UserSerializer(read_only=True)
    DevolucionuserId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='Usuario_devolucion', required=False, allow_null=True)
    Libro_detalle = LibroSerializer(read_only=True)
    libroid = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Libro.objects.all(), source='Libro_detalle')
    Incidentes = IncidenteSerializer(many=True, read_only=True,source='incidente_set')
    class Meta:
        model = DetallePrestamo
        fields = ('Id_detalle','Fecha_prestamo', 'Estado','Fecha_devolucion','Prestamo','Usuario_devolucion','DevolucionuserId','libroid','Libro_detalle','Incidentes')

class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = "__all__"

class PersonaSerializer(serializers.ModelSerializer):
    Tipo_Persona = TipoPersonaSerializer(read_only=True)
    Tipo_PersonaId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TipoPersona.objects.all(), source='Tipo_Persona')
    Dependencia = ProgramaSerializer(read_only=True)
    ProgramaId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Programa.objects.all(), source='Dependencia')
    Incidentes = IncidenteSerializer(many=True, read_only=True,source='incidente_set')

    class Meta:
        model = Personas
        fields = ('id','Nro_Tarjeta','Nro_Documento','Nombres','Apellidos','Estado_Tarjeta','Tipo_Persona','Tipo_PersonaId','Dependencia','Codigo_Acceso','ProgramaId','Incidentes')


class PrestamoSerializer(serializers.ModelSerializer):
    Usuario_Prestatario = UserSerializer(read_only=True)
    PrestatarioId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='Usuario_Prestatario')
    Persona = PersonaSerializer(read_only=True)
    personaId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Personas.objects.all(), source='Persona')
    detalleprestamo = DetallePrestamoSerializer(many=True,write_only=True)
    detailprestamo = DetallePrestamoSerializer(many=True,read_only=True,source='detalleprestamo_set')

    class Meta:
        model = Prestamo
        fields = ('Id_prestamo', 'Usuario_Prestatario','PrestatarioId', 'Persona', 'personaId', 'Estado_prestamo', 'Fecha_prestamo','Hora_prestamo','Fecha_devolucion','Hora_devolucion','detalleprestamo','detailprestamo')

    def create(self, validated_data):
        detalleprestamo_data = validated_data.pop('detalleprestamo')
        prestamo = Prestamo.objects.create(**validated_data)
        for Detalle_data in detalleprestamo_data:
            DetallePrestamo.objects.create(Prestamo=prestamo,**Detalle_data)
        return prestamo
