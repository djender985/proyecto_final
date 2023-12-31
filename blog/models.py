from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articulo (models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tiles_creados', null=True)
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField()  
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='tile_img', null=True, blank=True)

    def __str__(self):
        return f"{self.titulo}, {self.subtitulo}, {self.cuerpo}"