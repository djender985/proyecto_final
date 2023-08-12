from django.contrib import admin
from django.urls import path

from blog.views import (
    crear_tile, listar_tiles, mostrar_tile, borrar_tile, editar_tile,
)

urlpatterns = [
    # URLS de cursos
    path('wall/', listar_tiles, name="wall"),
    path('publicar_tile/', crear_tile, name="tile"),
    path('detalle_tile/<int:id>', mostrar_tile, name="mostrar_tile"),
    path('editar_tile/<int:id>', editar_tile, name='editar_tile'),
    path('borrar_tile/<int:id>', borrar_tile, name='borrar_tile'),
]