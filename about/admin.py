from django.contrib import admin
#llamar a la libreria about
from .models import About
# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
#Registro en el admin
admin.site.register(About,AboutAdmin)