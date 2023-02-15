from tabnanny import verbose
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name="Nombre")
    created = models.DateTimeField(
        auto_now_add=True,verbose_name="Fecha Creacion")
    updated = models.DateTimeField(
        auto_now=True,verbose_name="Fecha Edicion")
    
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=200,verbose_name="Titulo")
    content=models.TextField(verbose_name="Contenido")
    published=models.DateTimeField(verbose_name="Fecha de Publicacion",default=now)
    image=models.ImageField(verbose_name="Imagen",upload_to="blogs",null=True,blank=True)
    #nuevo (establece la relacion de usuarios con blogs (1:1,1:n,n:n))
    author=models.ForeignKey(
        User, verbose_name="Autor",on_delete=models.CASCADE) #relacion usuario del blog
    categories=models.ManyToManyField(Category, verbose_name="Categorias") #relacion categoria del blog
    created = models.DateTimeField(
        auto_now_add=True,verbose_name="Fecha Creacion")
    updated = models.DateTimeField(
        auto_now=True,verbose_name="Fecha de Edicion")


    class Meta:
        verbose_name="entrada"
        verbose_name_plural="entradas"
        ordering= ["-created"]

    def __str__(self):
        return self.title