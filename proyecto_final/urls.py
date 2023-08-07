# import de funciones de django
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio')
    path('/feed', include('blog.urls')),
    path("perfil/", include("perfil.urls")),
]
