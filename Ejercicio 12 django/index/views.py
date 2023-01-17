from django.shortcuts import render
from django.http import HttpResponse

from .models import peliculas, directores



# Create your views here.

def index(request):
    num_peliculas = peliculas.objects.all().count
    num_directores = directores.objects.all().count

    return render (
        request,
        'index.html',
        context = {
            'num_peliculas' : num_peliculas,
            'num_directores' : num_directores
            }

        )

