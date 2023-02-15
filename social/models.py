from django.db import models

# Create your models here.
class Link(models.Model):
    #nuevo
    #permite trabajar con SlugField (ingresa campos alfanumericos) 
    key=models.SlugField(verbose_name="Nombre Clave",max_length=100,unique=True)
    name=models.CharField(max_length=200,verbose_name="Red Social")
    url=models.URLField(verbose_name="Enlace",max_length=200,null=True,blank=True)
    created=models.DateTimeField(
        auto_now_add=True,verbose_name="Fecha Creacion")
    updated=models.DateTimeField(
        auto_now=True,verbose_name="Fecha Edicion")


    class Meta:
        verbose_name="enlace"
        verbose_name_plural="enlaces"
        ordering=['-name']
    
    def __str__(self):
        return self.name