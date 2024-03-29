from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from . import views

#vista personalizada prestamo
prestamo_list = views.PrestamoList.as_view({
    'get': 'list',
    'post': 'create'
})

prestamo_detail = views.PrestamoList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

Detalle_prestamo = views.PrestamoList.as_view({
    'post': 'set_detalleprestamo'
})

#vista personalizada persona
persona_list = views.PersonasList.as_view({
    'get': 'list',
    'post': 'create'
})

persona_detail = views.PersonasList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

incidente = views.PersonasList.as_view({
    'post': 'set_incidente'
})

#vista personalizada detalle pretsamo
detallep_list = views.DetallePrestamoList.as_view({
    'get': 'list',
    'post': 'create'
})

detallep_detail = views.DetallePrestamoList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

incidentep = views.DetallePrestamoList.as_view({
    'post': 'set_incidente'
})

#vista personalizada de detalle incidente
incidente_list = views.IncidenteList.as_view({
    'get': 'list',
    'post': 'create'
})

incidente_detail = views.IncidenteList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

incidentedetail = views.IncidenteList.as_view({
    'post': 'set_detalleincidente'
})

urlpatterns = [
    url(r'^api/Persona/$', persona_list),
    url(r'^api/Persona/(?P<pk>\d+)/$', persona_detail),
    url(r'^api/Persona/(?P<pk>\d+)/incidentes/$', incidente),
    url(r'^api/Persona/tipo/$', views.TipoPersonaList.as_view()),
    url(r'^api/Persona/tipo/(?P<pk>\d+)/$', views.TipoPersonaDetail.as_view()),
    url(r'^api/Prestamo/$', prestamo_list),
    url(r'^api/Prestamo/(?P<pk>\d+)/$', prestamo_detail),
    url(r'^api/Prestamo/(?P<pk>\d+)/devolucion/$', Detalle_prestamo),
    url(r'^api/Libro/Incidente/$', incidente_list),
    url(r'^api/Libro/Incidente/(?P<pk>\d+)/$', incidente_detail),
    url(r'^api/Libro/Incidente/(?P<pk>\d+)/detalle/$', incidentedetail),
    url(r'^api/Incidente/detalle/$', views.DetalleIncidenteList.as_view()),
    url(r'^api/Incidente/detalle/(?P<pk>\d+)/$', views.DetalleIncidenteDetail.as_view()),
    url(r'^api/Libro/Tipo/$', views.TipolibroList.as_view()),
    url(r'^api/Libro/Autor/$', views.AutorList.as_view()),
    url(r'^api/programa/$', views.ProgramaList.as_view()),
    url(r'^api/programa/(?P<pk>\d+)/$', views.ProgramaDetail.as_view()),
    url(r'^api/libro/$', views.LibroList.as_view()),
    url(r'^api/libro/active/$', views.LibroActiveList.as_view()),
    url(r'^api/libro/(?P<pk>\d+)/$',views.LibroDetail.as_view()),
    url(r'^api/Prestamo/Detalle/$', detallep_list),
    url(r'^api/Prestamo/Detalle/(?P<pk>\d+)/$', detallep_detail),
    url(r'^api/Prestamo/Detalle/(?P<pk>\d+)/incidentes/$', incidentep),
    url(r'^api/User/$', views.UserViewSet.as_view()),
    url(r'^api/User/(?P<pk>\d+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
