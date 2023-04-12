from django.db import models


# Create your models here.

class Categoria(models.Model):
    nomec = models.CharField(max_length=100, primary_key=True)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=30, decimal_places=2)
    level = models.DecimalField(max_digits=2, decimal_places=0)
    afinidade = models.DecimalField(max_digits=3, decimal_places=1)
    exp = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return self.valor


class Carta(models.Model):
    data = models.DateTimeField()
    nome = models.CharField(max_length=50)
    imagem = models.CharField(max_length=500)
    descricao = models.CharField(max_length=400)
    observacoes = models.TextField(null=True, blank=True)

    # Testando upload Github...

    def __str__(self):
        return self.nome


class CopiaCarta(models.Model):
    ID_CCARD = models.DecimalField(max_digits=999, decimal_places=0, primary_key=True)
    idcard = models.ForeignKey(Carta, on_delete=models.CASCADE)
    nome = models.ForeignKey(Carta, on_delete=models.CASCADE, related_name="nome2")
    imagem = models.ForeignKey(Carta, on_delete=models.CASCADE, related_name="imagem2")
    valor = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="valor2")
    level = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="level2")
    afinidade = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="afinidade2")
    exp = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="exp2")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="categoria2")
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


class User(models.Model):
    ID_USER = models.DecimalField(max_digits=999, decimal_places=0, primary_key=True)
    NOME_USER = models.CharField(max_length=34)

    def __str__(self):
        return self.ID_USER


class Invent(models.Model):
    ID_INV = models.DecimalField(max_digits=999, decimal_places=0, primary_key=True)
    ID_USER_inv = models.ForeignKey(User, on_delete=models.CASCADE)
    id_card_copy = models.ForeignKey(CopiaCarta, on_delete=models.CASCADE)

    def __str__(self):
        return self.ID_USER_inv


class Carteira(models.Model):
    ID_CARTEIRA = models.DecimalField(max_digits=999, decimal_places=0, primary_key=True)
    ID_USER_carteira = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ID_USER_carteira


class Evento(models.Model):
    ID_EVENT = models.DecimalField(max_digits=999, decimal_places=0, primary_key=True)
    NOME_EVENT = models.CharField(max_length=99)

    def __str__(self):
        return self.NOME_EVENT


class Event_User(models.Model):
    ID_EVENT_USER = models.DecimalField(max_digits=999, decimal_places=0, primary_key=True)
    ID_EVENT = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="ID_EVENT2")
    NOME_EVENT_user = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="NOME_EVENT2")
    ID_USER_evt = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.NOME_EVENT_user


class DateSim(models.Model):
    ID_DATE_SIM = models.DecimalField(max_digits=999, decimal_places=0, primary_key=True)
    ID_CARD_DATE = models.ForeignKey(Carta, on_delete=models.CASCADE)
    PERGUNTA = models.CharField(max_length=99)
    RESPOSTA = models.CharField(max_length=99)

    def __str__(self):
        return self.ID_DATE_SIM


class Batalha(models.Model):
    ID_BAT = models.DecimalField(max_digits=999, decimal_places=0, primary_key=True)
    NOME_BAT = models.CharField(max_length=99)

    def __str__(self):
        return self.NOME_BAT


class Bat_Log(models.Model):
    ID_BAT_LOG = models.DecimalField(max_digits=999, decimal_places=0, primary_key=True)
    ID_BAT = models.ForeignKey(Batalha, on_delete=models.CASCADE, related_name="ID_BAT2")
    NOME_BAT_log = models.ForeignKey(Batalha, on_delete=models.CASCADE, related_name="NOME_BAT2")
    ID_USER_log = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.NOME_BAT_log


class Minigame(models.Model):
    ID_MINIG = models.DecimalField(max_digits=999, decimal_places=0, primary_key=True)
    NOME_MINIG = models.CharField(max_length=99)

    def __str__(self):
        return self.NOME_MINIG


class Minigame_User(models.Model):
    ID_MINIG_USER = models.DecimalField(max_digits=999, decimal_places=0, primary_key=True)
    ID_MINIGAME = models.ForeignKey(Minigame, on_delete=models.CASCADE, related_name="ID_MINIG2")
    NOME_MINIG_LOG = models.ForeignKey(Minigame, on_delete=models.CASCADE)
    ID_USER_minig = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.NOME_MINIG_LOG

# ME LEIA!!!!
# Perguntar para o professor sobre o retorno do def, se pode puxar duas ForeignKey para mostrar o nome nos logs.
# E perguntar sobre o ID das cartas, se fiz certo.
