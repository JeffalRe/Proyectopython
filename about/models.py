from django.db import models

# Create your models here.
class About(models.Model):
    title=models.CharField(max_length=200, verbose_name="Certificacion")
    subtitle=models.CharField(max_length=200, verbose_name="Subtitulo Certificacion | Area")
    content=models.TextField(verbose_name="Contenido")
    image=models.ImageField(verbose_name="Imagen",upload_to="aboutm",null=True,blank=True)
    created=models.DateTimeField(
        auto_now_add=True,verbose_name="Fecha Creacion")
    updated=models.DateTimeField(
        auto_now=True,verbose_name="Fecha Edicion")

    class Meta:
        verbose_name="certificacion"
        verbose_name_plural="certificaciones"
        ordering=['-created']

    def __str__(self):
        return self.title