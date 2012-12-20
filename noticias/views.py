# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from noticias.models import Noticia, Comentario
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from noticias.forms import ComentarioForm, NoticiaForm

def lista_noticias(request):
    noticias = Noticia.objects.all()
    return render_to_response('lista_noticias.html',{'lista':noticias})

def noticia_completa(request, id_noticia):
    dato = get_object_or_404(Noticia, pk=id_noticia)
    comentarios = Comentario.objects.filter(noticia=dato)
    return render_to_response('noticia.html', {'noticia':dato, 'comentarios':comentarios}, context_instance=RequestContext(request))

def nueva_noticia(request):
    if request.method == 'POST':
        formulario = NoticiaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = NoticiaForm()

    return render_to_response('noticiaform.html', {'formulario':formulario}, context_instance=RequestContext(request))

def nuevo_comentario(request):
    if request.method == 'POST':
        formulario = ComentarioForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = ComentarioForm()

    return render_to_response('comentarioform.html', {'formulario':formulario}, context_instance=RequestContext(request))
