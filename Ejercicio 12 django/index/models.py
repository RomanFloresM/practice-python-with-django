from django.db import models

# Create your models here.

class peliculas(models.Model):
    nombre = models.CharField(max_length = 100, help_text = 'Nombre')
    resumen = models.CharField(max_length = 100, help_text = 'Resumen')

    def __str__(self):
        return self.nombre
        

class directores(models.Model):
    nombre = models.CharField(max_length = 64, help_text = 'nombre')
    peliculas = models.ManyToManyField(peliculas)

    def __str__(self):
        return self.nombre
