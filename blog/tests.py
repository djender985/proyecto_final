from django.test import TestCase
from blog.models import Articulo


class ArticuloTests(TestCase):
    def test_creacion_articulo(self):
        # caso uso esperado
        articulo = Articulo(
            autor = 'Pedro Rojas',
            titulo = 'Curiosidades del mundo',
            subtitulo = 'Como es posible que sucedan estas cosas?',
            cuerpo = 'Alguna vez que has preguntado como fue que construyeron las piramides, o como es que a veces hay relampago sin trueno?' ,
            fecha = '2023-08-13 18:06:43.622106',
            imagen = 'tile_img/oppenhaimer_pic_zbxA844.jpg',
        )
        articulo.save()

        # Compruebo que el curso fue creado y la data fue guardad correctamente
        self.assertEqual(Articulo.objects.count(), 1)
        self.assertEqual(Articulo.autor, 'Pedro Rojas')
        self.assertEqual(Articulo.titulo, 'Curiosidades del mundo')
        self.assertEqual(Articulo.subtitulo, 'Como es posible que sucedan estas cosas?')
        self.assertEqual(Articulo.cuerpo, 'Alguna vez que has preguntado como fue que construyeron las piramides, o como es que a veces hay relampago sin trueno?')
        self.assertEqual(Articulo.fecha, '2023-08-13 18:06:43.622106')
        self.assertEqual(Articulo.imagen, 'tile_img/oppenhaimer_pic_zbxA844.jpg')

    def test_curso_str(self):
        articulo = Articulo(
            autor="Pedro Rojas", 
            titulo='Curiosidades del mundo', 
            subtitulo='Como es posible que sucedan estas cosas?',
            cuerpo='Alguna vez que has preguntado como fue que construyeron las piramides, o como es que a veces hay relampago sin trueno?',
            fecha='2023-08-13 18:06:43.622106',
            imagen='tile_img/oppenhaimer_pic_zbxA844.jpg'
            )
        articulo.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(articulo.__str__(), "Pedro Rojas, Curiosidades del mundo, Como es posible que sucedan estas cosas?, Alguna vez que has preguntado como fue que construyeron las piramides, o como es que a veces hay relampago sin trueno?, 2023-08-13 18:06:43.622106, tile_img/oppenhaimer_pic_zbxA844.jpg")