from django import forms

class SingleForm(forms.Form):
    name=forms.CharField(label="Nombre",required=True,widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':"Escriba sus nombres y apellidos"}
    ))
    email=forms.EmailField(label="Email",required=True,widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':"Escriba su correo electronico"}
    ))
    content=forms.CharField(label="Mensaje",required=True,widget=forms.Textarea(
        attrs={'class':'form-control','rows':3,'placeholder':"Escriba su mensaje"}
    ))