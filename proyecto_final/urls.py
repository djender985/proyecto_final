# import de funciones de django
from django.contrib import admin
from django.urls import path, include
from proyecto_final.views import bienvenida_tiles


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenida_tiles, name='inicio'),
    path('tiles/', include('blog.urls')),
    path('perfil/', include("perfiles.urls")),
]
