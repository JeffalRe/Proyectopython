from django.shortcuts import render
from .models import About
# Create your views here.
def about(request):
    #tomar todos los objetos de about
    about=About.objects.all()
    return render(request, "about/about.html",{'about':about})