from django.test import TestCase
from blog.models import Articulo
from django.contrib.auth.models import User
import datetime
from datetime import timezone

class ArticuloTests(TestCase):
    def test_creacion_articulo(self):
        
        user = User(
            username = 'pedro55',
            first_name = 'Pedro',
            last_name = 'Rojas',
            email = 'pedrorojas@hotmail.com',
        )
        user.save()

        expectedDate = datetime.datetime.now(timezone.utc)

        articulo = Articulo(
            autor = user,
            titulo = 'Curiosidades del mundo',
            subtitulo = 'Como es posible que sucedan estas cosas?',
            cuerpo = 'Alguna vez que has preguntado como fue que construyeron las piramides, o como es que a veces hay relampago sin trueno?',
            imagen = 'tile_img/oppenhaimer_pic_zbxA844.jpg',
        )
        articulo.save()

        # Compruebo que el curso fue creado y la data fue guardad correctamente
        self.assertEqual(Articulo.objects.count(), 1)
        self.assertEqual(articulo.autor.username, 'pedro55')
        self.assertEqual(articulo.titulo, 'Curiosidades del mundo')
        self.assertEqual(articulo.subtitulo, 'Como es posible que sucedan estas cosas?')
        self.assertEqual(articulo.cuerpo, 'Alguna vez que has preguntado como fue que construyeron las piramides, o como es que a veces hay relampago sin trueno?')
        self.assertEqual(articulo.fecha, expectedDate)
        self.assertEqual(articulo.imagen, 'tile_img/oppenhaimer_pic_zbxA844.jpg')

    def test_articulo_str(self):
        user = User(
            username = 'pedro55',
            first_name = 'Pedro',
            last_name = 'Rojas',
            email = 'pedrorojas@hotmail.com',
        )
        user.save()

        expectedDate = datetime.datetime.now()

        articulo = Articulo(
            autor=user,
            titulo='Curiosidades del mundo',
            subtitulo='Como es posible que sucedan estas cosas?',
            cuerpo='Alguna vez que has preguntado como fue que construyeron las piramides, o como es que a veces hay relampago sin trueno?',
            fecha=expectedDate,
            imagen='tile_img/oppenhaimer_pic_zbxA844.jpg'
            )
        articulo.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(articulo.__str__(), "Curiosidades del mundo, Como es posible que sucedan estas cosas?, Alguna vez que has preguntado como fue que construyeron las piramides, o como es que a veces hay relampago sin trueno?")