"""import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'controle_gastos.settings')
django.setup()

from django.contrib.auth.models import User
from contas.models import CopiaCarta, Invent, Carteira

# Crie uma instância do usuário
nome_usuario = input("Insira o nome de usuário desejado: ")
senha = input("Insira sua senha: ")
email = input("Digite seu Email: ")
user = User.objects.create_user(username=nome_usuario, email=email, password=senha)

# Defina a senha do usuário usando o método set_password
user.set_password(senha)

# Adiciona a carta, 1500 moedas e o inventário ao usuário
carta = CopiaCarta.objects.create(titulo="Minha Carta", descricao="Descrição da minha carta")
inventario = Invent.objects.create(usuario=user)
moedas = Carteira.objects.create(usuario=user, quantidade=1500)

# Adiciona a carta e as moedas ao inventário
inventario.cartas.add(carta)
inventario.moedas = moedas
inventario.save()

# Salve o usuário no banco de dados
user.save()
print("Usuário criado com sucesso!")"""

# ESSA PORRA TA FUNCIONANDO. SO QUE. PRECISA LOCALIZAR A TABELA DO USER DO DJANGO, E ATRIBUIR AS TABELAS A ELA. E DEPOIS
# QUE CRIAR O USUARIO, COMENTE ESSE CODIGO, E REINICIE O SERVIDOR, FUTURAMENTE N VAMOS PRECISAR DELE(OU VAMOS) E CRIAREMOS
# PELO SITE.
