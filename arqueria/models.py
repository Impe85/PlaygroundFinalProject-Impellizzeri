from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_de_publicacion = models.DateTimeField(auto_now_add=True)
    imagen_destacada = models.ImageField(upload_to='imagenes/')
