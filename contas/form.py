from django.forms import ModelForm
from .models import Carta


class CartaForm(ModelForm):
    class Meta:
        model = Carta
        fields = ['data', 'nome', 'imagem', 'descricao', 'valor', 'level', 'afinidade', 'exp', 'categoria']
