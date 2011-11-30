# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from models import Pareja, Participante

def portada(request):
    obj = Pareja.objects.order_by('?')[0]

    return render_to_response('portada.html', locals(), context_instance = RequestContext(request))


def votar(request, id):
    obj = Participante.objects.get(id=id)
    obj.votos += 1
    obj.save()

    return redirect('/')


def lista(request):
    obj_list = Participante.objects.all()

    return render_to_response('lista.html', locals(), context_instance = RequestContext(request))

class ParticipanteListView(ListView):
    model=Participante

    def get_context_data(self, **kwargs):
        context = super(ParticipanteListView, self).get_context_data(**kwargs)
        context['algo'] = 'foo'
        return context

class ParticipanteCreateView(CreateView):
    model=Participante

    def get_success_url(self):
        print 'hola'
        return self.object