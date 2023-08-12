from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articulo (models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField()    
    fecha = models.DateTimeField(auto_now_add=True)
