from django.shortcuts import render
from .models import Homes
# Create your views here.
def home(request):
    #pone todos los objetos guardados en el admin (consulta)
    homes=Homes.objects.all()
    return render(request, "homes/home.html",{'homes':homes}) 