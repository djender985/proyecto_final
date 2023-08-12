from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from blog.models import Articulo
from blog.forms import FormTile
# Create your views here.


def listar_tiles(request):
    articulos = Articulo.objects.all()
    articulos_modificados = [
        {
            "autor": a.autor,
            "titulo": a.titulo,
            "subtitulo": a.subtitulo,
            "cuerpo": a.cuerpo.replace(a.cuerpo, a.cuerpo[:30]),
            "imagen": a.imagen
        }
        for a in articulos
    ]
    contexto = {
        "articulos": articulos_modificados,
    }
    http_response = render(
        request=request,
        template_name='blog/tiles.html',
        context=contexto,
    )
    return http_response



@login_required
def crear_tile(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = FormTile(request.POST, request.FILES)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            autor = request.user
            titulo = data["titulo"]
            subtitulo = data["subtitulo"]
            cuerpo = data["cuerpo"]
            imagen = data["imagen"]
            # creo un articulo en memoria RAM
            articulo = Articulo(autor=autor, titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, imagen=imagen)
            # Lo guardan en la Base de datos
            articulo.save()

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('tiles')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = FormTile()
    
    http_response = render(
        request=request,
        template_name='blog/formulario_tile.html',
        context={'formulario': formulario}
    )
    return http_response

def mostrar_tile (request, id):
    articulo = Articulo.objects.get(id=id)
    contexto = { "articulos": articulo}
    http_response = render(
        request=request,
        template_name='blog/detalle_tile.html',
        context=contexto,
    )
    return http_response

def editar_tile (request,id):
    articulo = Articulo.objects.get(id=id)
    if request.method == "POST":
        formulario = FormTile(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            autor = request.user
            titulo = data["titulo"]
            subtitulo = data["subtitulo"]
            cuerpo = data["cuerpo"]
            imagen = data["imagen"]
            # creo un articulo en memoria RAM
            articulo = Articulo(autor=autor, titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, imagen=imagen)
            articulo.save()

            url_exitosa = reverse('detalle_tile')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {           
            'titulo' : articulo.titulo,
            'subtitulo' : articulo.subtitulo,
            'cuerpo' : articulo.cuerpo,
            'imagen' : articulo.imagen
        }
        formulario = FormTile(initial=inicial)
    return render(
        request=request,
        template_name='blog/formulario_tile.html',
        context={'formulario': formulario},
    )

@login_required
def borrar_tile (request,id):
    # obtienes el curso de la base de datos
    articulo = Articulo.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        articulo.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('tiles')
        return redirect(url_exitosa)