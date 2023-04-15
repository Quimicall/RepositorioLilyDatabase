from django.contrib import admin
from django import forms
from .models import Categoria
from .models import Carta
from .models import User
from .models import Invent
from .models import Carteira
from .models import Evento
from .models import Event_User
from .models import Batalha
from .models import Bat_Log
from .models import Minigame
from .models import Minigame_User
from .models import DateSim
from .models import CopiaCarta
from .models import Item
from .models import Tipo
from .models import Classe
from .models import Atributos
from .models import Inventario_Carta
from .models import Perfil

admin.site.register(Categoria)
admin.site.register(Carta)
admin.site.register(User)
admin.site.register(Invent)
admin.site.register(Carteira)
admin.site.register(Evento)
admin.site.register(Event_User)
admin.site.register(Batalha)
admin.site.register(Bat_Log)
admin.site.register(Minigame)
admin.site.register(Minigame_User)
admin.site.register(DateSim)
admin.site.register(CopiaCarta)
admin.site.register(Item)
admin.site.register(Tipo)
admin.site.register(Classe)
admin.site.register(Atributos)
admin.site.register(Inventario_Carta)
admin.site.register(Perfil)


# Registre seus models aqui.
