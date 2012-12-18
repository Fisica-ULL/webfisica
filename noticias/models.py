from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User)    

    class Meta:
        ordering = ['-fecha']

    def __unicode__(self):
        return self.titulo
