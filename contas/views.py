from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .models import Carta, Perfil, Carteira
from django.views.generic import TemplateView
from controle_gastos.forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
import datetime


class UsuarioCreate(CreateView):
    template_name = "contas/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Usuarios')

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url

    """def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"""


class PerfilUpdate(UpdateView):
    template_name = 'contas/form-upload.html'  # Fazer um HTML para o perfil. AMÉM FUNCIONOU IRMÃOS !!!
    model = Perfil
    fields = ["nome_completo", "IMG_Perfil", "descricao_perfil"]
    success_url = reverse_lazy("perfil")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    """def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar
        return context"""


class CarteiraCreate(CreateView):
    model = Carteira
    fields = ["ID_USER_carteira", "Sakuras_user", "LotusPaga_user"]

    """def form_valid(self, form):
        self.object.save()
        Carteira.objects.create(ID_USER_carteira=self.object)"""


class CarteiraUpdate(UpdateView):
    template_name = 'contas/form-upload.html'  # Fazer um HTML para o perfil. AMÉM FUNCIONOU IRMÃOS !!!
    model = Carteira
    fields = ["ID_USER_carteira", "Sakuras_user", "LotusPaga_user"]

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Carteira, ID_USER_carteira=self.request.user)
        return self.object


class Perfiluser(UpdateView):
    template_name = 'contas/perfil.html'  # Fazer um HTML para o perfil. AMÉM FUNCIONOU IRMÃOS !!!
    model = Perfil
    fields = ["nome_completo", "IMG_Perfil", "descricao_perfil"]
    success_url = reverse_lazy("perfil")

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object


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
