from django.db import models

from django.contrib.auth.models import AbstractUser, User

# Create your models here.


# usuarios con atributos nuevos
class User(AbstractUser):
    icono = models.ImageField(upload_to="media/usuarios",  default='media/usuarios/default.png', null=True, blank=True)
    descripcion = models.TextField(max_length=350)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Categorias(models.Model):  # nombreapp_nombreclase
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "Categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Posts(models.Model):  # nombreapp_nombreclase
    titulo = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Titulo"
    )
    encabezado = models.TextField(verbose_name="Encabezado")
    contenido = models.TextField(verbose_name="Contenido")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, )
    imagen1 = models.ImageField(upload_to="media/posts", null=False, blank=False, default='media/posts/default.png')
    imagen2 = models.ImageField(upload_to="media/posts", null=False, blank=False, default='media/posts/default.png')

    class Meta:
        db_table = "Posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo


# class Imagenes(models.Model):
#     imagen = models.ImageField(upload_to="/media/Posts")
#     post = models.ForeignKey(Posts, on_delete=models.CASCADE)


class Comentarios(models.Model):
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField(max_length=250, verbose_name="Contenido")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
   
    class Meta:
        db_table = "Contacto"
        verbose_name = "Contacto"
        verbose_name_plural = "Contacto"

    def __str__(self):
        return self.nombre

# class Imagenes(models.Model):
#     imagen = models.ImageField(upload_to="/media/Posts")
#     post = models.ForeignKey(Posts, on_delete=models.CASCADE)


