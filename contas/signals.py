from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Carteira, Invent


@receiver(post_save, sender=User)
def criar_carteira(sender, instance, created, **kwargs):
    if created:
        Carteira.objects.create(ID_USER_carteira=instance)


# Ideia de criar deck automatico

"""@receiver(post_save, sender=User)
def criar_deck(sender, instance, created, **kwargs):
    if created:
        deck = DeckUser.objects.create(IDUserDeck=instance)

        # Adicionar as cartas ao deck
        cartas = Carta.objects.all()[:64]  # Obtenha as 64 primeiras cartas (ou ajuste para sua necessidade)
        deck.cartas.set(cartas)"""


@receiver(post_save, sender=User)
def criar_inventario(sender, instance, created, **kwargs):
    if created:
        Invent.objects.create(ID_USER_inv=instance)
