from django.shortcuts import render
from .models import Carta
from .form import CartaForm
import datetime


def home(request):
    data = {'agr': datetime.datetime.now()}
    # html = "<html><body> Está é a hora DO DUELO!!! %s.</body></html>" % agr
    return render(request, "contas/home.html", data)


def listagem(request):
    data = {}
    data['Cartas'] = Carta.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_carta(request):
    data = {}
    form = CartaForm()
    data['form'] = form
    return render(request, 'contas/form.html', data)
# Create your views here.
