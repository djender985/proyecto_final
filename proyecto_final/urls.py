# import de funciones de django
from django.contrib import admin
from django.urls import path, include
from proyecto_final.views import bienvenida_tiles, acerca_de
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenida_tiles, name='inicio'),
    path('tiles/', include('blog.urls')),
    path('perfil/', include('perfiles.urls')),
    path('about/', acerca_de, name='about'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
