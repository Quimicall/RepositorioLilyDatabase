from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from contas.models import Perfil, User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['nomeUser', 'email']  # 'password' , 'password2'


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['nomeUser', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['ID', 'user', 'IMG_Perfil', 'descricao_perfil']
