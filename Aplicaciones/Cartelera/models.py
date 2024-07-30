from django.db import models

# Create your models here.

#creando un modelo Terror, Comedia, Etc

class Genero(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    descripcion=models.CharField(max_length=150, default='')
    foto=models.FileField(upload_to='generos', null=True, blank=True)
    def __str__(self):
        fila="{0}"
        return fila.format(self.nombre)

#Creando un director
class Director(models.Model):
    id=models.AutoField(primary_key=True)
    dni=models.CharField(max_length=15)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    estado=models.BooleanField(default=True)
    foto=models.FileField(upload_to='directores', null=True, blank=True)

    def __str__(self):
        fila="{0} {1}"
        return fila.format(self.nombre, self.apellido)

class Pais(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    continente=models.CharField(max_length=50)
    capital=models.CharField(max_length=50)

    def __str__(self):
        fila="{0}"
        return fila.format(self.nombre)

class Pelicula(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=250)
    duracion=models.TimeField(null=True)    
    sinopsis=models.TextField()
    genero=models.ForeignKey(Genero, on_delete=models.CASCADE)  #CLAVE FORANEA de Genero Y CON MODELO CASCADA PARA LA ELIMINACION
    director=models.ForeignKey(Director, on_delete=models.CASCADE)
    pais=models.ForeignKey(Pais, on_delete=models.CASCADE, null=True)
    portada=models.FileField(upload_to='portadas', null=True, blank=True)
    def __str__(self):
        fila="{0}: - {1} - {2}"
        return fila.format(self.id, self.titulo, self.pais)
    
#09 JULIO |  CREANDO MODELO CINE

class Cine(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200,default='')
    telefono = models.CharField(max_length=15,default='')
    
    def __str__(self):
        fila="{0}: {1} {2}"
        return fila.format(self.id, self.nombre, self.direccion)