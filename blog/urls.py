from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from blog.views import (
    crear_tile, listar_tiles, mostrar_tile, borrar_tile, editar_tile,
)

urlpatterns = [
    # URLS de cursos
    path('wall/', listar_tiles, name="wall"),
    path('publicar_tile/', crear_tile, name="crear_tile"),
    path('detalle_tile/<int:id>', mostrar_tile, name="mostrar_tile"),
    path('editar_tile/<int:id>', editar_tile, name='editar_tile'),
    path('borrar_tile/<int:id>', borrar_tile, name='borrar_tile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)