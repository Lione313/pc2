from django.db import models

class Semestre(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.CharField(max_length=50)
    fecha_inicio = models.DateField(null=True, blank=True) 
    fecha_fin = models.DateField(null=True, blank=True)    
    def __str__(self):
        return self.titulo

class Curso(models.Model):
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, related_name='cursos')  
    nombre = models.CharField(max_length=100)
    duracion = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)  
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)  
    creditos = models.PositiveIntegerField(null=True, blank=True)  

    def __str__(self):
        return self.nombre
