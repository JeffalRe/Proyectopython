from django.db import models

# Create your models here.
class Homes(models.Model):
    title=models.CharField(max_length=200, verbose_name="Titulo")
    subtitle=models.CharField(max_length=200, verbose_name="Subtitulo Servicio")
    content=models.TextField(verbose_name="Contenido")
    image=models.ImageField(verbose_name="Imagen Ultimo Trabajo",upload_to="Services")
    client=models.CharField(max_length=200, verbose_name="Cliente")
    created=models.DateTimeField(
        auto_now_add=True,verbose_name="Fecha Creacion")
    updated=models.DateTimeField(
        auto_now=True,verbose_name="Fecha Edicion")

    class Meta:
        verbose_name="inicio"
        verbose_name_plural="inicios"
        ordering=['-created']

    def __str__(self):
        return self.title