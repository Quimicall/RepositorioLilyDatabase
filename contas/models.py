from django.db import models


# Create your models here.
# criar uma consulta para buscar o nome dos itens da tabela.

# Depois mudar os nomes das váriaveis das tabelas, 'nomec' == Tier E, D, C, B, A, S, SS.
class Categoria(models.Model):
    Tier = models.CharField(max_length=100, primary_key=True)

    dt_criacao = models.DateTimeField(auto_now_add=True)

    valor = models.DecimalField(max_digits=30, decimal_places=2)
    vl = str(valor)

    level = models.DecimalField(max_digits=2, decimal_places=0)

    afinidade = models.DecimalField(max_digits=3, decimal_places=1)

    exp = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return self.Tier


class Atributos(models.Model):
    nom_classe = models.CharField(max_length=100)

    HP = models.DecimalField(max_digits=999, decimal_places=2)

    ATK = models.DecimalField(max_digits=999, decimal_places=2)

    ATK_M = models.DecimalField(max_digits=999, decimal_places=0)

    DEF = models.DecimalField(max_digits=999, decimal_places=2)

    DEF_M = models.DecimalField(max_digits=999, decimal_places=0)

    SPEED = models.DecimalField(max_digits=999, decimal_places=2)

    PM = models.DecimalField(max_digits=999, decimal_places=2)

    TOTAL = models.DecimalField(max_digits=999, decimal_places=2)

    def __str__(self):
        return str(f'{self.nom_classe}')


class Item(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='IDItem')

    Data = models.DateTimeField(auto_now_add=True)

    Item_Nome = models.CharField(max_length=999)

    HP_Item = models.DecimalField(max_digits=999, decimal_places=0)

    MP_Item = models.DecimalField(max_digits=999, decimal_places=0)

    ATK_Item = models.DecimalField(max_digits=999, decimal_places=0)

    ATK_M_Item = models.DecimalField(max_digits=999, decimal_places=0)

    DEF_Item = models.DecimalField(max_digits=999, decimal_places=0)

    DEF_M_Item = models.DecimalField(max_digits=999, decimal_places=0)

    SPEED_Item = models.DecimalField(max_digits=999, decimal_places=0)

    QUEIMADURA_Item = models.DecimalField(max_digits=999, decimal_places=2)

    ENVENENAR_Item = models.DecimalField(max_digits=999, decimal_places=2)

    SANGRAMENTO_Item = models.DecimalField(max_digits=999, decimal_places=2)

    PEN_ARM_Item = models.DecimalField(max_digits=999, decimal_places=2)

    ROUBO_VIDA_Item = models.DecimalField(max_digits=999, decimal_places=2)

    ACERTO_CRIT_Item = models.DecimalField(max_digits=999, decimal_places=2)

    ESCUDO_Item = models.DecimalField(max_digits=999, decimal_places=2)

    DMG_VERDADEIRO_Item = models.DecimalField(max_digits=999, decimal_places=2)

    Descricao_Item = models.TextField(null=False, blank=True)

    observacoes_Item = models.TextField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return str(f'{self.Item_Nome}')


class Classe(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_CLASSE')

    Tier = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    classe_Carta = models.CharField(max_length=999)

    def __str__(self):
        return str(f'{self.Tier} {self.classe_Carta}')


class Tipo(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_TIPO')

    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

    tipo = models.CharField(max_length=999)

    ATK_T = models.DecimalField(max_digits=999, decimal_places=0)

    ATKM_T = models.DecimalField(max_digits=999, decimal_places=0)

    DEFM_T = models.DecimalField(max_digits=999, decimal_places=0)

    DEF_T = models.DecimalField(max_digits=999, decimal_places=0)

    def __str__(self):
        return str(f'{self.ID} {self.tipo}')


# VSF SARA
class Carta(models.Model):
    data = models.DateTimeField(auto_now_add=True)

    nome = models.CharField(max_length=50)

    imagem = models.CharField(max_length=500)

    Anime = models.CharField(max_length=400)

    tipos = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    atributo = models.ForeignKey(Atributos, on_delete=models.CASCADE)

    # classes = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    talento = models.CharField(max_length=500)

    observacoes = models.TextField(null=True, blank=True)

    # Testando upload Github...

    def __str__(self):
        return str(f'{self.nome}')


class CopiaCarta(models.Model):
    ID_CCARD = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_COPIACARTA')

    idcard = models.ForeignKey(Carta, on_delete=models.CASCADE)

    # imagem = models.ForeignKey(Carta, on_delete=models.CASCADE, related_name="imagem2")

    # valor = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name="valor2")

    # level = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="level2")

    # afinidade = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="afinidade2")

    # exp = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="exp2")

    # categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="categoria2")

    def __str__(self):
        return str(f'{self.ID_CCARD} {self.idcard}')


class User(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_USER')

    NOME_USER = models.CharField(max_length=34)

    def __str__(self):
        return self.ID


class Invent(models.Model):
    ID_INV = models.DecimalField(max_digits=999, decimal_places=0, primary_key=True)

    ID_USER_inv = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ID_USER_inv


class Inventario_Carta(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_INV._CARD')

    CARTA_INV = models.ForeignKey(Carta, on_delete=models.CASCADE)

    ID_USER_INV_CARD = models.ForeignKey(User, on_delete=models.CASCADE)

    ITEM = models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return str(f'{self.ID} {self.ID_USER_INV_CARD} {self.CARTA_INV}')


class Carteira(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_CARTEIRA')

    ID_USER_carteira = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ID_USER_carteira


class Evento(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_EVENT')

    NOME_EVENT = models.CharField(max_length=99)

    def __str__(self):
        return self.NOME_EVENT


class Event_User(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_EVENT_USER')

    ID_EVENT = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="ID_EVENT2")

    NOME_EVENT_user = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="NOME_EVENT2")

    ID_USER_evt = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.NOME_EVENT_user


class DateSim(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_DATE_SIM')

    # 'idds = str(ID_DATE_SIM)'

    ID_CARD_DATE = models.ForeignKey(Carta, on_delete=models.CASCADE)
    idcd = str(ID_CARD_DATE)

    PERGUNTA = models.CharField(max_length=99)

    RESPOSTA = models.CharField(max_length=99)

    ''' def __str__(self):
        return str(self.ID_DATE_SIM)'''

    def __str__(self):
        return str(f'{self.ID} {self.ID_CARD_DATE}')


class Batalha(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_BAT')

    NOME_BAT = models.CharField(max_length=99)

    def __str__(self):
        return self.NOME_BAT


class Bat_Log(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_BAT_LOG')

    ID_BAT = models.ForeignKey(Batalha, on_delete=models.CASCADE, related_name="ID_BAT2")

    NOME_BAT_log = models.ForeignKey(Batalha, on_delete=models.CASCADE, related_name="NOME_BAT2")

    ID_USER_log = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.NOME_BAT_log


class Minigame(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_MINIG')

    NOME_MINIG = models.CharField(max_length=99)

    def __str__(self):
        return self.NOME_MINIG


class Minigame_User(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_MINIG_USER')

    ID_MINIGAME = models.ForeignKey(Minigame, on_delete=models.CASCADE, related_name="ID_MINIG2")

    NOME_MINIG_LOG = models.ForeignKey(Minigame, on_delete=models.CASCADE)

    ID_USER_minig = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.NOME_MINIG_LOG

# ME LEIA!!!!
# Perguntar para o professor sobre o retorno do def, se pode puxar duas ForeignKey para mostrar o nome nos logs.(COMPLETE)
# E perguntar sobre o ID das cartas, se fiz certo.
