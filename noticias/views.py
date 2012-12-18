# Create your views here.

from noticias.models import Noticia
from django.shortcuts import render_to_response

def lista_noticias(request):
    noticias = Noticia.objects.all()
    return render_to_response('lista_noticias.html',{'lista':noticias})
