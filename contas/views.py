from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Carta
import datetime


def home(request):
    data = {'agr': datetime.datetime.now()}
    # html = "<html><body> Está é a hora DO DUELO!!! %s.</body></html>" % agr
    return render(request, "contas/home.html", data)


@login_required()
def listagem(request):
    data = {}
    data['Cartas'] = Carta.objects.all()
    return render(request, 'contas/listagem.html', data)


def login(request):
    return render(request, 'registration/login.html')

    # Resto do código da view

# Create your views here.
