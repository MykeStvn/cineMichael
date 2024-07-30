import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
 #importacion del Modelo Genero
from Aplicaciones.Cartelera.enviar_correo import enviar_correo_nuevo_cine
from Aplicaciones.Cartelera.models import Cine, Director, Genero, Pais, Pelicula

#importar contrib para controlar las alertas
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request,"home.html")

#Renderizando el template listadogeneros

def listadoGeneros(request):
    generosBdd=Genero.objects.all() #esta variable se conecta al modelo genero y trae todos los objetos
    return render(request, "listadoGeneros.html", {'generos':generosBdd}) #aqui se llama al modelo generos para mostrarlo en la tabla

def listadoPeliculas(request):
    peliculasBdd=Pelicula.objects.all()
    return render(request,"listadoPeliculas.html", {'peliculas':peliculasBdd})

#renderizar listado directores
def listadoDirectores(request):
    directoresBdd=Director.objects.all()
    return render(request, "listadoDirectores.html", {'directores':directoresBdd})

def listadoPaises(request):
    paisesBdd=Pais.objects.all()
    return render(request,"listadoPaises.html", {'paises':paisesBdd})

#Se recibe el id para eliminar un genero (parámetro)

def eliminarGenero(request,id):
    generoEliminar=Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request,'Género eliminado con éxito!')
    return redirect('listadoGeneros')

def eliminarDirector(request,id):
    directorEliminar=Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request,'Director eliminado con éxito!')
    return redirect('listadoDirectores')

#RENDERIZAR PAGINA NUEVO GENERO
def nuevoGenero(request):
    return render(request,"nuevoGenero.html")

#renderizar pagina nuevo director

def nuevoDirector(request):
    return render(request,"nuevoDirector.html")

#renderizar pagina nuevo pais

def nuevoPais(request):
    return render(request,"nuevoPais.html")

#renderizar pagina nueva pelicula

#def nuevaPelicula(request):
#    return render(request,"nuevaPelicula.html")


#FUNCION PARA GUARDAR GENEROS

def guardarGenero(request):
    nom=request.POST["nombre"] 
    des=request.POST["descripcion"]  
    fot=request.FILES.get("foto")
    nuevoGenero=Genero.objects.create(nombre=nom,descripcion=des,foto=fot) #pasar parametros segun nuestra bd y segun las variables que creamos
    #CONTROLAR ALERTAS
    messages.success(request,'Género registrado con éxito!')
    return redirect('listadoGeneros')

#FUNCION PARA GUARDAR DIRECTOR
def guardarDirector(request):
    dni=request.POST["dni"]
    nombre=request.POST["nombre"]
    apellido=request.POST["apellido"]
    estado= 'estado' in request.POST
    foto=request.FILES.get("foto")
    nuevoDirector=Director.objects.create(dni=dni,nombre=nombre,apellido=apellido,estado=estado,foto=foto)
    return JsonResponse({ #ESTE JSONRESPONSE SE IMPORTA AL INICIO
        'estado': True,
        'mensaje': 'Director registrado exitosamente'
    })
    # #CONTROLAR ALERTAS
    # messages.success(request,'Director registrado con éxito!')
    # return redirect('listadoDirectores')

#FUNCION PARA GUARDAR PAIS

def guardarPais(request):
    nom=request.POST["nombre"] 
    cont=request.POST["continente"]
    cap=request.POST["capital"]   
    nuevoPais=Pais.objects.create(nombre=nom,continente=cont,capital=cap) #pasar parametros segun nuestra bd y segun las variables que creamos
    #CONTROLAR ALERTAS
    messages.success(request,'País registrado con éxito!')
    return redirect('listadoPaises')

#Renderizar formulario de actualización genero
def editarGenero(request,id):
    generoEditar=Genero.objects.get(id=id)
    return render (request,'editargenero.html',{'generoEditar':generoEditar})



#Actualizar los nuevos datos en la bdd
def procesarActualizacionGenero(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    descripcion=request.POST["descripcion"]
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nombre
    generoConsultado.descripcion=descripcion
    generoConsultado.save()
    messages.success(request,'Genero Actualizado Exitosamente')
    return redirect(listadoGeneros)

#renderizar formulario de actualizacion director
def editarDirector(request,id):
    directorEditar=Director.objects.get(id=id)
    return render (request,'editarDirector.html',{'directorEditar':directorEditar})

def procesarActualizacionDirector(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        dni = request.POST.get("dni")
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        estado = 'estado' in request.POST
        # Obtener el director actual
        directorConsultado = get_object_or_404(Director, id=id)
        # Actualizar los campos del director
        directorConsultado.dni = dni
        directorConsultado.nombre = nombre
        directorConsultado.apellido = apellido
        directorConsultado.estado = estado
        # Actualizar la foto solo si se ha subido una nueva
        if 'foto' in request.FILES:
            if directorConsultado.foto:
                directorConsultado.foto.delete()  # Eliminar la foto antigua
            directorConsultado.foto = request.FILES['foto']
        # Guardar los cambios
        directorConsultado.save()
        # Mostrar mensaje de éxito
        messages.success(request, 'Director Actualizado Exitosamente')
        return redirect('listadoDirectores')
    else:
        return redirect('listadoDirectores')

#Renderizar formulario de actualización de pais
def editarPais(request,id):
    paisEditar=Pais.objects.get(id=id)
    return render (request,'editarpais.html',{'paisEditar':paisEditar})

#actualizar los datos de pais
def procesarActualizacionPais(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    continente=request.POST["continente"]
    capital=request.POST["capital"]
    paisConsultado=Pais.objects.get(id=id)
    paisConsultado.nombre=nombre
    paisConsultado.continente=continente
    paisConsultado.capital=capital
    paisConsultado.save()
    messages.success(request,'Pais Actualizado Exitosamente')
    return redirect(listadoPaises)

#eliminarPais
def eliminarPais(request,id):
    paisEliminar=Pais.objects.get(id=id)
    paisEliminar.delete()
    messages.success(request,'País eliminado con éxito!')
    return redirect('listadoPaises')


#nueva pelicula
def nuevaPelicula(request):
    generos = Genero.objects.all()
    directores = Director.objects.all()
    paises = Pais.objects.all()
    return render(request, 'nuevapelicula.html', {'generos': generos, 'directores': directores, 'paises': paises})

def guardarPelicula(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        duracion = request.POST.get('duracion', None)
        sinopsis = request.POST['sinopsis']
        genero_id = request.POST['genero']
        director_id = request.POST['director']
        pais_id = request.POST.get('pais', None)
        
        nueva_pelicula = Pelicula.objects.create(
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


#editar pelicula
def editarPelicula(request, id):
    peliculaEditar = get_object_or_404(Pelicula, id=id)
    generos = Genero.objects.all()
    directores = Director.objects.all()
    paises = Pais.objects.all()
    
    return render(request, 'editarpelicula.html', {'peliculaEditar': peliculaEditar, 'generos': generos, 'directores': directores, 'paises': paises})

def procesarActualizacionPelicula(request):
    if request.method == 'POST':
        id = request.POST["id"]
        titulo = request.POST["titulo"]
        duracion = request.POST["duracion"]
        sinopsis = request.POST["sinopsis"]
        genero_id = request.POST["genero"]
        director_id = request.POST["director"]
        pais_id = request.POST["pais"] if "pais" in request.POST else None
        
        peliculaConsultada = Pelicula.objects.get(id=id)
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
        return redirect('listadoPeliculas')  # O redireccionar a donde sea necesario en caso de error
    
#eliminarPelicula
def eliminarPelicula(request,id):
    peliculaEliminar=Pelicula.objects.get(id=id)
    peliculaEliminar.delete()
    messages.success(request,'Película eliminada con éxito!')
    return redirect('listadoPeliculas')


#FUNCION PARA GESTIONAR CRUD CINE (9-JUL-2024)
def gestionCines(request):
    return render (request,'gestionCines.html')



# #Insertando cines mediante AJAX en la Base de Datos
# def guardarCine(request):
#     nom=request.POST["nombre"]
#     dir=request.POST["direccion"]
#     tel=request.POST["telefono"]
#     nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel)    
#     return JsonResponse({
#         'estado': True,
#         'mensaje': 'Género registrado exitosamente.',
#         'cine':nuevoCine
#     })

def guardarCine(request):
    nom=request.POST["nombre"]
    dir=request.POST["direccion"]
    tel=request.POST["telefono"]
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel) #se importa el CINE

    enviar_correo_nuevo_cine(
        nombre_cine=nuevoCine.nombre,
        direccion_cine=nuevoCine.direccion,
        telefono_cine=nuevoCine.telefono
    )
    return JsonResponse({ #ESTE JSONRESPONSE SE IMPORTA AL INICIO
        'estado': True,
        'mensaje': 'Cine registrado exitosamente'
    })

#INSERTAR UN CINES CON AJAX
# @csrf_exempt
# def guardarCine(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             nom = data.get('nombre')
#             dir = data.get('direccion')
#             tel = data.get('telefono')
            
#             nuevoCine = Cine.objects.create(nombre=nom, direccion=dir, telefono=tel)
#             return JsonResponse({
#                 'estado': True,
#                 'mensaje': 'Cine registrado exitosamente',
#                 'cine': {
#                     'nombre': nuevoCine.nombre,
#                     'direccion': nuevoCine.direccion,
#                     'telefono': nuevoCine.telefono
#                 }
#             }, status=201)
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'JSON mal formado'}, status=400)
#     else:
#         return JsonResponse({'error': 'Método no permitido'}, status=405)

def listadoCines(request):
    cinesBdd=Cine.objects.all()
    return render(request,"listadoCines.html", {'cines':cinesBdd})

def gestionDirector(request):
    return render (request,'gestionDirector.html')

def listarDirectores(request):
    directoresBdd=Director.objects.all()
    return render(request,"listarDirectores.html", {'directores':directoresBdd})

#MANEJAR ASINCRONA CON FETCH

def guardarPeliculaF(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        duracion = request.POST.get('duracion', None)
        sinopsis = request.POST['sinopsis']
        genero_id = request.POST['genero']
        director_id = request.POST['director']
        pais_id = request.POST.get('pais', None)
        
        nueva_pelicula = Pelicula.objects.create(
            titulo=titulo,
            duracion=duracion,
            sinopsis=sinopsis,
            genero_id=genero_id,
            director_id=director_id,
            pais_id=pais_id
        )
        return JsonResponse({ #ESTE JSONRESPONSE SE IMPORTA AL INICIO
        'estado': True,
        'mensaje': 'Película registrada exitosamente'
    })
    
    return redirect('gestionPelicula') 

def gestionPelicula(request):
    generos = Genero.objects.all()
    directores = Director.objects.all()
    paises = Pais.objects.all()
    return render(request, 'gestionpelicula.html', {'generos': generos, 'directores': directores, 'paises': paises})
    

def listarPeliculas(request):
    peliculasBdd=Pelicula.objects.all()
    return render(request,"listarPeliculas.html", {'peliculas':peliculasBdd})