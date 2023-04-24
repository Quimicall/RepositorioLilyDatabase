from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from controle_gastos.forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Carta, Item, Perfil, User
import datetime


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, User)
            return redirect('perfil')  # substitua 'home' pela URL desejada para redirecionar após o registro
    else:
        form = UserCreationForm()

    return render(request, 'contas/register.html', {'form': form})


"""def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            login(request, User)
            messages.success(request, f'Sua conta foi criada! Você está logado agora.')
            sucess_url = reverse_lazy('perfil')
            player, created = Perfil.objects.get_or_create(user=request.user)
    else:
        form = UserRegisterForm()
    return render(request, 'contas/register.html', {'form': form})"""


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.User)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.User.perfil)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Sua conta foi atualizada!')
            sucess_url = reverse_lazy('perfil')

    """else:
        u_form = UserUpdateForm(instance=request.User)
        p_form = ProfileUpdateForm(instance=request.User.perfil)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }"""

    return render(request, 'contas/perfil.html')  # , context"""


def home(request):
    data = {'agr': datetime.datetime.now()}
    # html = "<html><body> Está é a hora DO DUELO!!! %s.</body></html>" % agr
    return render(request, "contas/home.html", data)


@login_required
def listagem(request):
    data = {}
    data['Cartas'] = Carta.objects.all()
    return render(request, 'contas/listagem.html', data)

    # Resto do código da view

# Create your views here.
