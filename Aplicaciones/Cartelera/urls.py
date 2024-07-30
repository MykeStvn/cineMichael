#configurar el redireccionamiento
#importacion de path urls de python
from django.urls import path
#importar todas las vistas que hay dentro de la aplicacion CARTELERA
from . import views
#crear arreglo de urls
urlpatterns = [
    path('',views.home, name='home'),
    #agregar al path las urls
    path('listadoGeneros/',views.listadoGeneros, name='listadoGeneros'),
    path('listadoPeliculas/',views.listadoPeliculas, name='listadoPeliculas'),
    path('listadoDirectores/',views.listadoDirectores, name='listadoDirectores'),
    path('listadoPaises/',views.listadoPaises, name='listadoPaises'),
    path('eliminarGenero/<id>',views.eliminarGenero, name='eliminarGenero'), #esta linea recibe otro parámetro si llamamos a otro parámetro usamos otro slash
    path('eliminarDirector/<id>',views.eliminarDirector, name='eliminarDirector'), #esta linea recibe otro parámetro si llamamos a otro parámetro usamos otro slash
    path('eliminarPelicula/<id>',views.eliminarPelicula, name='eliminarPelicula'), #esta linea recibe otro parámetro si llamamos a otro parámetro usamos otro slash
    path('eliminarPais/<id>',views.eliminarPais, name='eliminarPais'), #esta linea recibe otro parámetro si llamamos a otro parámetro usamos otro slash
    path('nuevoGenero/',views.nuevoGenero, name='nuevoGenero'),
    path('nuevoDirector/',views.nuevoDirector, name='nuevoDirector'),
    path('nuevoPais/',views.nuevoPais, name='nuevoPais'),
    path('nuevaPelicula/',views.nuevaPelicula, name='nuevaPelicula'),
    path('guardarDirector/',views.guardarDirector,name='guardarDirector'),
    path('guardarGenero/',views.guardarGenero,name='guardarGenero'),
    path('guardarPais/',views.guardarPais,name='guardarPais'),
    path('guardarPelicula/',views.guardarPelicula,name='guardarPelicula'),
    path('editarGenero/<id>',views.editarGenero, name='editarGenero'),
    path('editarDirector/<id>',views.editarDirector, name='editarDirector'),
    path('editarPais/<id>',views.editarPais, name='editarPais'),
    path('editarPelicula/<id>',views.editarPelicula, name='editarPelicula'),
    path('procesarActualizacionGenero/',views.procesarActualizacionGenero, name='procesarActualizacionGenero'),
    path('procesarActualizacionDirector/',views.procesarActualizacionDirector, name='procesarActualizacionDirector'),
    path('procesarActualizacionPais/',views.procesarActualizacionPais, name='procesarActualizacionPais'),
    path('procesarActualizacionPelicula/',views.procesarActualizacionPelicula, name='procesarActualizacionPelicula'),
    path('gestionCines/',views.gestionCines, name='gestionCines'),
    path('guardarCine/',views.guardarCine, name='guardarCine'),
    path('listadoCines/',views.listadoCines, name='listadoCines'),    
    path('gestionDirector/',views.gestionDirector, name='gestionDirector'),
    path('listarDirectores/',views.listarDirectores, name='listarDirectores'),
     path('gestionPelicula/',views.gestionPelicula, name='gestionPelicula'),
    path('guardarPeliculaF/',views.guardarPeliculaF, name='guardarPeliculaF'),
    path('listarPeliculas/',views.listarPeliculas, name='listarPeliculas')
]