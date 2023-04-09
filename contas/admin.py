from django.contrib import admin
from django import forms
from .models import Categoria
from .models import Carta


admin.site.register(Categoria)
admin.site.register(Carta)

# Registre seus models aqui.
