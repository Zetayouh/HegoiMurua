from django.db import models

# Create your models here.

class Proyecto(models.Model):
    titulo=models.CharField(max_length=50)
    imagen_1=models.ImageField(upload_to='proyectos')
    imagen_2=models.ImageField(upload_to='proyectos', null=True, blank=True)
    imagen_3=models.ImageField(upload_to='proyectos', null=True, blank=True)
    imagen_4=models.ImageField(upload_to='proyectos', null=True, blank=True)
    fecha=models.DateField()
    descripcion=models.TextField()
    lenguaje=models.CharField(max_length=50)
    herramientas=models.CharField(max_length=50)

    class Meta:
        verbose_name="proyecto"
        verbose_name_plural="proyectos"

    def __str__(self):
        return self.titulo
    
