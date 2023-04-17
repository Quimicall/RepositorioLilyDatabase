from django.shortcuts import render
from .models import Carta
import datetime



def home(request):
    data = {'agr': datetime.datetime.now()}
    # html = "<html><body> Está é a hora DO DUELO!!! %s.</body></html>" % agr
    return render(request, "contas/home.html", data)


def listagem(request):
    data = {}
    data['Cartas'] = Carta.objects.all()
    return render(request, 'contas/listagem.html', data)

# Create your views here.
