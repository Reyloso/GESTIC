# coding=utf-8
from django.contrib import admin
from .models import *
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin


# Register your models here.
class Prestamos (admin.ModelAdmin):
    def has_add_permission(self, request):
         return False

    # def get_actions(self, request):
    #     actions = super(Prestamos, self).get_actions(request) # Obtenemos todas las acciones de este modelo
    #     del actions['delete_selected'] # Deshabilitamos la opción de borrar
    #     return actions

    def Devolucion(self, instance):

        return "<a href='/admin/Prestamo/Detalle/%s'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-arrow-left' aria-hidden='true'></i>  </a>" % instance.Id_prestamo
    Devolucion.short_description = "Devolucion"
    Devolucion.allow_tags = True
    Devolucion.is_column = True

    def Reporte_Prestamo(self, instance):

        return "<a href='/admin/Prestamo/Reporte/%s'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-file-pdf-o' aria-hidden='true'></i>  </a>" % instance.Id_prestamo
    Reporte_Prestamo.short_description = "Reporte Prestamo"
    Reporte_Prestamo.allow_tags = True
    Reporte_Prestamo.is_column = True

    def add_view(self, *args, **kwargs):
        self.fields = ('Usuario_Prestatario','Persona','Estado_prestamo','Fecha_prestamo','Hora_prestamo','Fecha_devolucion','Hora_devolucion',)
        return super(Prestamos, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.fields = ('Estado_prestamo',)
        return super(Prestamos, self).change_view(*args, **kwargs)

    list_display = ['Id_prestamo','Usuario_Prestatario','Persona','Estado_prestamo','Fecha_prestamo','Hora_prestamo','Reporte_Prestamo', 'Devolucion' ]
    search_fields = ('Id_prestamo','Estado_prestamo','Usuario_Prestatario__username','Persona__Primer_Apellido','Persona__Primer_Nombre','Persona__Segundo_Apellido','Persona__Nro_Tarjeta',)
    list_filter = ('Estado_prestamo','Usuario_Prestatario__username')

    class Meta:
		model = Prestamo

class Incidentes (admin.ModelAdmin):
    def change_view(self, *args, **kwargs):
        self.fields = ('descripcion',)
        return super(Incidentes, self).change_view(*args, **kwargs)

    def has_add_permission(self, request):
        return False

    def Reporte_Incidente(self, instance):

        return "<a href='/admin/Incidente/Reporte/%s'> <i style='font-size:20px; display: flex;justify-content: center;' class='fa fa-file-pdf-o' aria-hidden='true'></i>  </a>" % instance.Id_Incidente
    Reporte_Incidente.short_description = "Reporte Incidente"
    Reporte_Incidente.allow_tags = True
    Reporte_Incidente.is_column = True

    list_display = ['Id_Incidente','usuario','Persona','Recurso','Tipo_Incidente','Estado','Fecha_Incidente','Reporte_Incidente']
    search_fields = ('Estado','Tipo_Incidente','Persona__Primer_Apellido','Persona__Primer_Nombre','Persona__Segundo_Apellido','Persona__Nro_Tarjeta','usuario__username','Recurso__Id_recurso')
    list_filter = ('Estado','Tipo_Incidente',)
    class Meta:
        model = Incidente

class DetallePrestamos (admin.ModelAdmin):
    #def has_add_permission(self, request):
    #    return False
        list_display = ['Id_detalle','Prestamo','Fecha_prestamo','Estado','Fecha_devolucion','Usuario_devolucion','Recurso_detalle']
        class Meta:
		          model = DetallePrestamo



admin.site.register(DetallePrestamo, DetallePrestamos)
admin.site.register(Prestamo, Prestamos)
admin.site.register(Incidente, Incidentes)
