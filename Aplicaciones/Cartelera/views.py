import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from Aplicaciones.Cartelera.enviar_correo import enviar_correo_nuevo_cine
from Aplicaciones.Cartelera.models import Cine, Director, Genero, Pais, Pelicula
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "Cartelera/home.html")

# Renderizando el template listadoGeneros
def listadoGeneros(request):
    generosBdd = Genero.objects.all()
    return render(request, "Cartelera/listadoGeneros.html", {'generos': generosBdd})

def listadoPeliculas(request):
    peliculasBdd = Pelicula.objects.all()
    return render(request, "Cartelera/listadoPeliculas.html", {'peliculas': peliculasBdd})

# Renderizar listado directores
def listadoDirectores(request):
    directoresBdd = Director.objects.all()
    return render(request, "Cartelera/listadoDirectores.html", {'directores': directoresBdd})

def listadoPaises(request):
    paisesBdd = Pais.objects.all()
    return render(request, "Cartelera/listadoPaises.html", {'paises': paisesBdd})

# Eliminar un genero
def eliminarGenero(request, id):
    generoEliminar = get_object_or_404(Genero, id=id)
    generoEliminar.delete()
    messages.success(request, 'Género eliminado con éxito!')
    return redirect('listadoGeneros')

def eliminarDirector(request, id):
    directorEliminar = get_object_or_404(Director, id=id)
    directorEliminar.delete()
    messages.success(request, 'Director eliminado con éxito!')
    return redirect('listadoDirectores')

# Renderizar formulario nuevo género
def nuevoGenero(request):
    return render(request, "Cartelera/nuevoGenero.html")

# Renderizar formulario nuevo director
def nuevoDirector(request):
    return render(request, "Cartelera/nuevoDirector.html")

# Renderizar formulario nuevo país
def nuevoPais(request):
    return render(request, "Cartelera/nuevoPais.html")

# Renderizar página nueva película
def nuevaPelicula(request):
    generos = Genero.objects.all()
    directores = Director.objects.all()
    paises = Pais.objects.all()
    return render(request, 'Cartelera/nuevapelicula.html', {'generos': generos, 'directores': directores, 'paises': paises})

# Función para guardar género
def guardarGenero(request):
    nom = request.POST["nombre"]
    des = request.POST["descripcion"]
    fot = request.FILES.get("foto")
    Genero.objects.create(nombre=nom, descripcion=des, foto=fot)
    messages.success(request, 'Género registrado con éxito!')
    return redirect('listadoGeneros')

# Función para guardar director
def guardarDirector(request):
    dni = request.POST["dni"]
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    estado = 'estado' in request.POST
    foto = request.FILES.get("foto")
    Director.objects.create(dni=dni, nombre=nombre, apellido=apellido, estado=estado, foto=foto)
    return JsonResponse({
        'estado': True,
        'mensaje': 'Director registrado exitosamente'
    })

# Función para guardar país
def guardarPais(request):
    nom = request.POST["nombre"]
    cont = request.POST["continente"]
    cap = request.POST["capital"]
    Pais.objects.create(nombre=nom, continente=cont, capital=cap)
    messages.success(request, 'País registrado con éxito!')
    return redirect('listadoPaises')

# Renderizar formulario de actualización género
def editarGenero(request, id):
    generoEditar = get_object_or_404(Genero, id=id)
    return render(request, 'Cartelera/editargenero.html', {'generoEditar': generoEditar})

# Actualizar los nuevos datos en la BDD
def procesarActualizacionGenero(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    generoConsultado = get_object_or_404(Genero, id=id)
    generoConsultado.nombre = nombre
    generoConsultado.descripcion = descripcion
    generoConsultado.save()
    messages.success(request, 'Género actualizado exitosamente')
    return redirect('listadoGeneros')

# Renderizar formulario de actualización director
def editarDirector(request, id):
    directorEditar = get_object_or_404(Director, id=id)
    return render(request, 'Cartelera/editarDirector.html', {'directorEditar': directorEditar})

def procesarActualizacionDirector(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        dni = request.POST.get("dni")
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        estado = 'estado' in request.POST
        directorConsultado = get_object_or_404(Director, id=id)
        directorConsultado.dni = dni
        directorConsultado.nombre = nombre
        directorConsultado.apellido = apellido
        directorConsultado.estado = estado
        if 'foto' in request.FILES:
            if directorConsultado.foto:
                directorConsultado.foto.delete()
            directorConsultado.foto = request.FILES['foto']
        directorConsultado.save()
        messages.success(request, 'Director actualizado exitosamente')
        return redirect('listadoDirectores')
    else:
        return redirect('listadoDirectores')

# Renderizar formulario de actualización de país
def editarPais(request, id):
    paisEditar = get_object_or_404(Pais, id=id)
    return render(request, 'Cartelera/editarpais.html', {'paisEditar': paisEditar})

# Actualizar los datos de país
def procesarActualizacionPais(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    continente = request.POST["continente"]
    capital = request.POST["capital"]
    paisConsultado = get_object_or_404(Pais, id=id)
    paisConsultado.nombre = nombre
    paisConsultado.continente = continente
    paisConsultado.capital = capital
    paisConsultado.save()
    messages.success(request, 'País actualizado exitosamente')
    return redirect('listadoPaises')

# Eliminar país
def eliminarPais(request, id):
    paisEliminar = get_object_or_404(Pais, id=id)
    paisEliminar.delete()
    messages.success(request, 'País eliminado con éxito!')
    return redirect('listadoPaises')

# Página nueva película
def nuevaPelicula(request):
    generos = Genero.objects.all()
    directores = Director.objects.all()
    paises = Pais.objects.all()
    return render(request, 'Cartelera/nuevapelicula.html', {'generos': generos, 'directores': directores, 'paises': paises})

def guardarPelicula(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        duracion = request.POST.get('duracion', None)
        sinopsis = request.POST['sinopsis']
        genero_id = request.POST['genero']
        director_id = request.POST['director']
        pais_id = request.POST.get('pais', None)
        
        Pelicula.objects.create(
            titulo=titulo,
            duracion=duracion,
            sinopsis=sinopsis,
            genero_id=genero_id,
            director_id=director_id,
            pais_id=pais_id
        )
        messages.success(request, 'Película agregada exitosamente!')
        return redirect('listadoPeliculas')
    
    return redirect('nuevaPelicula') 

# Editar película
def editarPelicula(request, id):
    peliculaEditar = get_object_or_404(Pelicula, id=id)
    generos = Genero.objects.all()
    directores = Director.objects.all()
    paises = Pais.objects.all()
    
    return render(request, 'Cartelera/editarpelicula.html', {'peliculaEditar': peliculaEditar, 'generos': generos, 'directores': directores, 'paises': paises})

def procesarActualizacionPelicula(request):
    if request.method == 'POST':
        id = request.POST["id"]
        titulo = request.POST["titulo"]
        duracion = request.POST["duracion"]
        sinopsis = request.POST["sinopsis"]
        genero_id = request.POST["genero"]
        director_id = request.POST["director"]
        pais_id = request.POST["pais"] if "pais" in request.POST else None
        
        peliculaConsultada = get_object_or_404(Pelicula, id=id)
        peliculaConsultada.titulo = titulo
        peliculaConsultada.duracion = duracion
        peliculaConsultada.sinopsis = sinopsis
        peliculaConsultada.genero_id = genero_id
        peliculaConsultada.director_id = director_id
        peliculaConsultada.pais_id = pais_id
        
        peliculaConsultada.save()
        messages.success(request, 'Película actualizada exitosamente.')
        return redirect('listadoPeliculas')
    else:
        messages.error(request, 'Error al procesar la actualización de la película.')
        return redirect('listadoPeliculas')
    
# Eliminar película
def eliminarPelicula(request, id):
    peliculaEliminar = get_object_or_404(Pelicula, id=id)
    peliculaEliminar.delete()
    messages.success(request, 'Película eliminada con éxito!')
    return redirect('listadoPeliculas')

# Función para gestionar cines
def gestionCines(request):
    return render(request, 'Cartelera/gestionCines.html')

# Guardar cine con notificación por correo
def guardarCine(request):
    nom = request.POST["nombre"]
    dir = request.POST["direccion"]
    tel = request.POST["telefono"]
    nuevoCine = Cine.objects.create(nombre=nom, direccion=dir, telefono=tel)
    
    enviar_correo_nuevo_cine(
        nombre_cine=nuevoCine.nombre,
        direccion_cine=nuevoCine.direccion,
        telefono_cine=nuevoCine.telefono
    )
    
    return JsonResponse({
        'estado': True,
        'mensaje': 'Cine registrado exitosamente'
    })

# Listado de cines
def listadoCines(request):
    cinesBdd = Cine.objects.all()
    return render(request, "Cartelera/listadoCines.html", {'cines': cinesBdd})

# Función para gestionar directores
def gestionDirector(request):
    return render(request, 'Cartelera/gestionDirector.html')

# Listar directores
def listarDirectores(request):
    directoresBdd = Director.objects.all()
    return render(request, "Cartelera/listarDirectores.html", {'directores': directoresBdd})

# Manejar creación de película con fetch (asíncrono)
def guardarPeliculaF(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        duracion = request.POST.get('duracion', None)
        sinopsis = request.POST['sinopsis']
        genero_id = request.POST['genero']
        director_id = request.POST['director']
        pais_id = request.POST.get('pais', None)
        
        Pelicula.objects.create(
            titulo=titulo,
            duracion=duracion,
            sinopsis=sinopsis,
            genero_id=genero_id,
            director_id=director_id,
            pais_id=pais_id
        )
        return JsonResponse({
            'estado': True,
            'mensaje': 'Película registrada exitosamente'
        })
    
    return redirect('gestionPelicula')

# Página de gestión de películas
def gestionPelicula(request):
    generos = Genero.objects.all()
    directores = Director.objects.all()
    paises = Pais.objects.all()
    return render(request, 'Cartelera/gestionpelicula.html', {'generos': generos, 'directores': directores, 'paises': paises})

# Listar películas
def listarPeliculas(request):
    peliculasBdd = Pelicula.objects.all()
    return render(request, "Cartelera/listarPeliculas.html", {'peliculas': peliculasBdd})
