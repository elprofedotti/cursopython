from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Director, Pelicula

def index(request):
    num_dire= Director.objects.all().count()
    num_pelis=Pelicula.objects.all().count()

    
    return render(
        request,
        'index.html',
        context={
            'num_dire': num_dire,
            'num_pelis': num_pelis
            
        }
    )

class listaPeliculas(generic.ListView):
    template_name="pelicula_list.html"
    model=Pelicula

class peliculaDetalle(generic.DetailView):
    template_name="pelicula_detalle.html"
    model=Pelicula


class listaDirectores(generic.ListView):
    template_name="directores_list.html"
    model=Director

class directorDetalle(generic.DetailView):
    template_name="director_detalle.html"
    model=Director