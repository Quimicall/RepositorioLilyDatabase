"""from .models import Item, Inventario_Carta, User

# Esse é um exemplo de como o item pode ir para o Inventario da carta. Boa sorte Ítalo do Futuro!! :)

item = Item.objects.get(id='IDItem')
inventario, created = Inventario_Carta.objects.get_or_create(usuario=User, item=Item)
if not created:
    inventario.quantidade += 1
inventario.save()"""

# Agora um comentario mais distribuido, aqui você fez o seguinte, está puxando as váriaveis item para puxar o ID do item
# Com isso você declarou o inventario pra ver se o item especificado. Se o objeto existir ele será retornado:
# (inventario, False)

# Roubado com sucesso (Lucas).

"""n1 = int(input('Digite as ativações do talento: ')
b = 160
print('O buff 1 é de 160%')
for x in range(n1 - 1):
    r = b + 60 / (b/100)
    b = r
    print('O buff {x + 2} é de {r:.0f}%')"""


# ==================================================
