from django.contrib import admin
#importacion de app Homes en admin
from .models import Homes
#configuracion extendida para mostrar mas valores
class HomesAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
# Register your models here.
admin.site.register(Homes, HomesAdmin)