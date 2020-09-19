from django.db import models

# Create your models here.
class Estudiante(models.Model):
    publicacion= (
        ('T','TECNOLOGIA'),
        ('E','ENTRETENIMIENTO'),
        ('N','NOTICIAS'),

    )
    nombre =models.CharField(max_length=50) 
    apellido =models.CharField(max_length=50) 
    Telefono =models.CharField(max_length=200)
    Email =models.CharField(max_length=200,default="")
    Fecha = models.DateField()
    tipo = models.ForeignKey(
        'TipoEstudiante',
        on_delete= models.CASCADE,
        default=1
        
     )
    publicacion =models.CharField(
        max_length=20,
        choices=publicacion,
        default='E') 
    creacion =models.DateField(auto_now_add=True)
    actualizacion =models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombre,self.apellido)

class TipoEstudiante(models.Model):
    tipo = models.CharField(max_length=30) 
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)


    def __str__(self):
           return '%s' % (self.tipo)

class Curso(models.Model):
    Cursos= (
        ('I','INTELIGENCIA ARTIFICIAL'),
        ('T','TELECOMUNICACIONES'),
        ('D','DESARROLLO WEB'),
        ('E','ETICA'),

    )
    
    Estudiante = models.ManyToManyField(Estudiante)
    Cursos =models.CharField(
        max_length=20,
        choices=Cursos,
        default='E') 
    creacion =models.DateField(auto_now_add=True)
    actualizacion =models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.Cursos)

class Catedraticos(models.Model):
    Nombre =models.CharField(max_length=200,default="")
    apellido =models.CharField(max_length=200,default="")
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __str__(self):
           return '%s' % (self.Nombre)
