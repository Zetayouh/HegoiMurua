from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=30)

    class Meta:
        verbose_name="categoria"
        verbose_name_plural="categorias"

    def __str__(self):
        return self.nombre
    
class Aptitud(models.Model):
    titulo=models.CharField(max_length=30)
    imagen=models.ImageField(upload_to='aptitudes')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name="aptitud"
        verbose_name_plural="aptitudes"

    def __str__(self):
        return self.titulo