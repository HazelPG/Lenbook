from django.contrib import admin
from .models import *
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export import fields
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class librosResource(resources.ModelResource):
    tipo_de_libro = fields.Field(attribute='tipo_de_libro',
                                   widget=ForeignKeyWidget(Tipolibro, 'tipo_libro'))

    Autor = fields.Field(attribute='Autor',
                                   widget=ForeignKeyWidget(Autores, 'Autor'))
    class Meta:
        # import_id_fields = ('id',)
        model = Libro
        export_order = ('id','nombre_libro','tipo_de_libro','Autor','Numero_Serie','Estado_libro')
        fields =  ('id','nombre_libro','tipo_de_libro','Autor','Numero_Serie','Estado_libro')

class libros (ImportExportModelAdmin):
    actions = None

    def codigo_barras(self, instance):
        return "<a href='/admin/libros/codigo_barras/%s'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-barcode' aria-hidden='true'></i>  </a>" % instance.id

    codigo_barras.short_description = "Codigo De Barras"
    codigo_barras.allow_tags = True
    codigo_barras.is_column = True

    def Reporte_libro(self, instance):
        return "<a href='/admin/Libro/Reporte/%s'> <i style='font-size:17px' class='fa fa-file' aria-hidden='true'></i>   </a>" % instance.id

    Reporte_libro.short_description = "Reporte libro"
    Reporte_libro.allow_tags = True
    Reporte_libro.is_column = True

    list_filter = ('Estado_libro','tipo_de_libro','Autor')
    search_fields = ('Estado_libro','nombre_libro','Numero_Serie','tipo_de_libro__tipo_libro','Autor__Autor')
    list_display = ['id','Numero_Serie','tipo_de_libro','Autor','nombre_libro','Estado_libro','fecha_registro','codigo_barras','Reporte_libro']
    resource_class = librosResource
    class Meta:
        model = Libro


class  Autor (admin.ModelAdmin):
    actions = None

    class Meta:
        model = Autores

class  Tipo_libros (admin.ModelAdmin):
    actions = None

    class Meta:
        model = Tipolibro

admin.site.register(Tipolibro,Tipo_libros)
admin.site.register(Autores,Autor)
admin.site.register(Libro,libros)
