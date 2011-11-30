from django.conf.urls.defaults import patterns, include, url

from django.views.generic import ListView
from encuesta.models import Participante
from encuesta.views import ParticipanteListView, ParticipanteCreateView

urlpatterns = patterns('encuesta2.encuesta.views',
    url(r'^$', 'portada', name='portada'),
    url(r'^votar/(?P<id>[\d+])/$', 'votar', name='votar'),
    url(r'^crear/$', ParticipanteCreateView.as_view(), name='crear_participante'),
    url(r'^lista/$', ListView.as_view(model=Participante, template_name='lista.html'), name='lista'),
    url(r'^lista2/$', ParticipanteListView.as_view(template_name='lista.html',
                                       queryset=Participante.objects.filter(votos__gt=1)), name='lista2'),

    )