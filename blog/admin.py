from django.contrib import admin
#importar la categoria
from .models import Category, Blog
#añadir las extendidas
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class BlogAdmin(admin.ModelAdmin): #configuracion extendida
    readonly_fields=('created','updated')
# Register your models here.
    list_display=('title','author','published')
    ordering=('author','published')
    #agregar busqueda
    #para buscar campos de otros modelos se debe usar el nombre del modelo y el campo dentro del modelo
    search_fields=('title','content',
    'author__username','categories__name')
    #fechas de publicacion (busqueda)
    date_hierarchy='published'
    #Filtrado de datos
    list_filter=('author__username','categories__name')
admin.site.register(Category,CategoryAdmin)
admin.site.register(Blog,BlogAdmin)