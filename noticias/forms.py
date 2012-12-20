from django.forms import ModelForm
from django import forms
from noticias.models import Noticia, Comentario

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
