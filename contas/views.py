from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from controle_gastos.forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import login
from .models import Carta
import datetime


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # substitua 'home' pela URL desejada para redirecionar após o registro
    else:
        form = UserCreationForm()

    return render(request, 'contas/register.html', {'form': form})


"""def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Sua conta foi criada! Você está logado agora.')
            return redirect('login')

        else:
            form = UserRegisterForm()
        return render(request, 'contas/register.html', {'form': form})"""


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Sua conta foi atualizada!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'contas/profile.html', context)


def home(request):
    data = {'agr': datetime.datetime.now()}
    # html = "<html><body> Está é a hora DO DUELO!!! %s.</body></html>" % agr
    return render(request, "contas/home.html", data)


def listagem(request):
    data = {}
    data['Cartas'] = Carta.objects.all()
    return render(request, 'contas/listagem.html', data)

# Create your views here.
