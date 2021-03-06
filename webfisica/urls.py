from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webfisica.views.home', name='home'),
    # url(r'^webfisica/', include('webfisica.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'noticias.views.lista_noticias'),
    url(r'^noticia/(?P<id_noticia>\d+)$', 'noticias.views.noticia_completa'),
    url(r'^noticia/comentarioform/$', 'noticias.views.nuevo_comentario'),
    url(r'^noticiaform/$', 'noticias.views.nueva_noticia'),
)
