from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver, Signal
from contas.models import Perfil, Invent, Carteira, Carta, Item


@receiver(post_save, sender=Perfil)
def created_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    pass


@receiver(post_save, sender=Perfil)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    pass


@receiver(post_save, sender=Invent)
def save_invent(sender, instance, **kwargs):
    instance.invent.save()


"""from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from contas.models import Invent, Carteira, Perfil, MoedaPadrao, MoedaPaga

lotus_paga = MoedaPaga(user_id=User.id)
lotus_paga.save()

Sakura_padrao = MoedaPadrao(Sakuras=User)
Sakura_padrao.save()


@receiver(post_save, sender=User)
def criar_inventario_carteira_perfil(sender, instance, created, **kwargs):
    if created:
        # Cria um objeto Inventario, Carteira e Perfil associados ao novo usuário
        inventario = Invent.objects.create(NomeUsuarios=instance, ID_USER_inv=instance)
        carteira = Carteira.objects.create(ID_USER_carteira=instance)
        perfil = Perfil.objects.create(user=instance)
        print("Inventario, Carteira e Perfil criados para o usuário:", instance.username)"""
