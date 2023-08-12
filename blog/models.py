from django.db import models

# Create your models here.
class Articulo (models.Model):
    titulo = models.CharField(max_length=150)
    subtítulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=80)
    fecha = models.DateField(null=True)