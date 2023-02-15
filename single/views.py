from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import SingleForm
from django.urls import reverse

# Create your views here.
def single(request):
    singleForm=SingleForm()
    #instanciar la clase
    #print("Tipo de peticion:{}".format(request.method))
    if request.method=="POST":
        singleForm=SingleForm(data=request.POST)
        if singleForm.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            content=request.POST.get('content','')
            #envio del correo
            email=EmailMessage(
                "Web Personal: Nuevo mensaje de correo",
                "De{} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
                "no-contestar@imbox.mailtrap.io",
                ["jalvarez@itsqmet.edu.ec"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('single')+"?ok")
            except:
                return redirect(reverse('single')+"?fail")

    
    return render(request, "single/single.html",{'form':singleForm})