from .models import Link

def ctx_dict(request):
    ctx={}
    #cargar la lista de redes sociales
    links=Link.objects.all()
    #agregando en el diccionario
    for link in links:
        ctx[link.key]=link.url #llenando el diccionario
        
    return ctx