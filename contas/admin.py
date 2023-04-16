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
from .models import MoedaPadrao
from .models import MoedaPaga
from .models import Deck
from .models import DeckUser
from .models import MercadoGlobal
from .models import MercadoGlobalPlayer
from .models import RecompensaDiaria
from .models import SistemaDeTroca
from .models import LootBox_Basic
from .models import LootBox_Medium
from .models import LootBox_Superior
from .models import AscensaoCarta
from .models import Metas
from .models import Talentos
from .models import Passivas
from .models import CampoDeTreinamento


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
admin.site.register(MoedaPadrao)
admin.site.register(MoedaPaga)
admin.site.register(Deck)
admin.site.register(DeckUser)
admin.site.register(MercadoGlobal)
admin.site.register(MercadoGlobalPlayer)
admin.site.register(RecompensaDiaria)
admin.site.register(SistemaDeTroca)
admin.site.register(LootBox_Basic)
admin.site.register(LootBox_Medium)
admin.site.register(LootBox_Superior)
admin.site.register(Perfil)
admin.site.register(AscensaoCarta)
admin.site.register(Metas)
admin.site.register(Talentos)
admin.site.register(Passivas)
admin.site.register(CampoDeTreinamento)


# Registre seus models aqui.
