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

# Registre seus models aqui.
