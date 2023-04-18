"""import os
import django
from django.db.models import Model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'controle_gastos.settings')
django.setup()

from django.contrib.auth.models import User
from contas.models import Invent, Carteira, Carta

# Crie uma instância do usuário
nome_usuario = input("Insira o nome de usuário desejado: ")
senha = input("Insira sua senha: ")
email = input("Digite seu Email: ")
user = User.objects.create_user(username=nome_usuario, email=email, password=senha)

# Defina a senha do usuário usando o método set_password
User.set_password(senha)

# Adiciona a carta, 1500 moedas e o inventário ao usuário
carta = Carta.objects.create(nome='Nome da Carta', Anime='Nome do Anime', atributo='atributo')
inventario = Invent.objects.create(usuario=User)
moedas = Carteira.objects.create(usuario=User, quantidade=1500)

# Adiciona a carta e as moedas ao inventário
inventario.cartas.add(carta)
inventario.moedas = moedas
inventario.save()

# Salve o usuário no banco de dados
User.save()
# user.save()

print("Usuário criado com sucesso!")

# ESSA PORRA TA FUNCIONANDO. SO QUE. PRECISA LOCALIZAR A TABELA DO USER DO DJANGO, E ATRIBUIR AS TABELAS A ELA. E DEPOIS
# QUE CRIAR O USUARIO, COMENTE ESSE CODIGO, E REINICIE O SERVIDOR, FUTURAMENTE N VAMOS PRECISAR DELE(OU VAMOS) E CRIAREMOS
# PELO SITE.
"""