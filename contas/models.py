from django.db import models


# Create your models here.
# criar uma consulta para buscar o nome dos itens da tabela.

# Depois mudar os nomes das váriaveis das tabelas, 'nomec' == Tier E, D, C, B, A, S, SS.

# Perguntar para o professor se a Ascensao está correta, para puxar uma ascensao daquela para varias cartas.


class MoedaPadrao(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='IDMoedaPadrao')

    Sakuras = models.DecimalField(max_digits=999, decimal_places=2, default=0)

    objects = models.Manager()

    def __str__(self):
        return str(f'{self.ID} {self.Sakuras}')


class MoedaPaga(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='IDMoedaPaga')

    Lotus_Gold = models.DecimalField(max_digits=999, decimal_places=2, default=0)

    def __str__(self):
        return str(f'{self.ID} {self.Lotus_Gold}')


class Passivas(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_PASSIVAS')

    NomeElemento = models.CharField(max_length=99)

    Passiva = models.CharField(max_length=999)

    DescricaoPassiva = models.TextField(max_length=999)

    def __str__(self):
        return str(f'{self.ID} {self.NomeElemento} {self.Passiva}')


class Talentos(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_TALENTOS')

    talento = models.CharField(max_length=999)

    descricao_talento = models.TextField(max_length=999)

    def __str__(self):
        return str(f'{self.ID} {self.talento}')


class Metas(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_METAS')

    Nome_Carta_Meta = models.CharField(max_length=999)

    meta_Um = models.CharField(max_length=999)

    descricao_meta_um = models.TextField(max_length=999)

    lv_meta_um = models.DecimalField(max_digits=999, decimal_places=0)

    meta_Dois = models.CharField(max_length=999)

    descricao_meta_Dois = models.TextField(max_length=999)

    lv_meta_dois = models.DecimalField(max_digits=999, decimal_places=0)

    meta_Tres = models.CharField(max_length=999)

    descricao_meta_Tres = models.TextField(max_length=999)

    lv_meta_tres = models.DecimalField(max_digits=999, decimal_places=0)

    def __str__(self):
        return str(f'{self.ID} {self.Nome_Carta_Meta}')


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

    img_item = models.CharField(max_length=999)

    HP_Item = models.DecimalField(max_digits=999, decimal_places=0, default=0)

    MP_Item = models.DecimalField(max_digits=999, decimal_places=0, default=0)

    ATK_Item = models.DecimalField(max_digits=999, decimal_places=0, default=0)

    ATK_M_Item = models.DecimalField(max_digits=999, decimal_places=0, default=0)

    DEF_Item = models.DecimalField(max_digits=999, decimal_places=0, default=0)

    DEF_M_Item = models.DecimalField(max_digits=999, decimal_places=0, default=0)

    SPEED_Item = models.DecimalField(max_digits=999, decimal_places=0, default=0)

    QUEIMADURA_Item = models.DecimalField(max_digits=999, decimal_places=2, default=0)

    ENVENENAR_Item = models.DecimalField(max_digits=999, decimal_places=2, default=0)

    SANGRAMENTO_Item = models.DecimalField(max_digits=999, decimal_places=2, default=0)

    PEN_ARM_Item = models.DecimalField(max_digits=999, decimal_places=2, default=0)

    ROUBO_VIDA_Item = models.DecimalField(max_digits=999, decimal_places=2, default=0)

    ACERTO_CRIT_Item = models.DecimalField(max_digits=999, decimal_places=2, default=0)

    ESCUDO_Item = models.DecimalField(max_digits=999, decimal_places=2, default=0)

    DMG_VERDADEIRO_Item = models.DecimalField(max_digits=999, decimal_places=2, default=0)

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


'''class SubClasse(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_SUBCLASSE')

    ClassePrincipal = models.ForeignKey(Classe, on_delete=models.CASCADE)
    
    subclasse = models.CharField(max_length=999)
    
    temSubclasse = models.DecimalField(max_digits=2, decimal_places=0)'''


class Tipo(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_TIPO')

    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

    tipo = models.CharField(max_length=999)

    ATK_T = models.DecimalField(max_digits=999, decimal_places=0, default=0)

    ATKM_T = models.DecimalField(max_digits=999, decimal_places=0, default=0)

    DEFM_T = models.DecimalField(max_digits=999, decimal_places=0, default=0)

    DEF_T = models.DecimalField(max_digits=999, decimal_places=0, default=0)

    FORTE_CONTRA = models.CharField(max_length=999)

    FRACO_CONTRA = models.CharField(max_length=999)

    PASSIVA_TIPO = models.ForeignKey(Passivas, on_delete=models.CASCADE)

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

    talentoCartas = models.ForeignKey(Talentos, on_delete=models.CASCADE)

    metasCartas = models.ForeignKey(Metas, on_delete=models.CASCADE)

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

    objects = models.Manager()

    def __str__(self):
        return str(f'{self.ID_CCARD} {self.idcard}')


class User(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_USER')

    NOME_USER = models.CharField(max_length=34)

    def __str__(self):
        return str(f'{self.ID} {self.NOME_USER}')


# Inventario não deveria ter um espaço para armazenar os itens?
class Invent(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_INV.')

    ID_USER_inv = models.ForeignKey(User, on_delete=models.CASCADE)

    carta_inventario = models.ForeignKey(Carta, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return str(f'{self.ID_USER_inv}')


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

    ID_USER_carteira = models.OneToOneField(User, on_delete=models.CASCADE)

    Sakuras_user = models.ForeignKey(MoedaPadrao, on_delete=models.CASCADE)

    LotusPaga_user = models.ForeignKey(MoedaPaga, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.ID_USER_carteira} {self.Sakuras_user}')


class Evento(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_EVENT')

    NOME_EVENT = models.CharField(max_length=99)

    Limite = models.DecimalField(max_digits=10, decimal_places=0, default=10)

    def __str__(self):
        return self.NOME_EVENT


class Event_User(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_EVENT_USER')

    ID_EVENT = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="ID_EVENT2")

    NOME_EVENT_user = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="NOME_EVENT2")

    ID_USER_evt = models.ForeignKey(User, on_delete=models.CASCADE)

    Event_Limites = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.NOME_EVENT_user}')


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
        return str(f'{self.NOME_BAT_log}')


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
        return str(f'{self.NOME_MINIG_LOG}')


class Perfil(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_PERFIL_USER')

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ID_USER_PERFIL')

    IMG_Perfil = models.CharField(max_length=999)

    descricao_perfil = models.CharField(max_length=999)

    objects = models.Manager()

    def __str__(self):
        return str(f'{self.user}')


class MercadoGlobal(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_MERCADOGLOBAL')

    ID_User = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ID_USER_MARKET')

    itens = models.ForeignKey(Invent, on_delete=models.CASCADE, verbose_name='ITENS_LOJA')

    preco_Item = models.DecimalField(max_digits=999, decimal_places=2, default=0)

    def __str__(self):
        return str(f'{self.ID_User} {self.itens} {self.preco_Item}')


class MercadoGlobalPlayer(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                             verbose_name='ID_MERCADO_GLOBAL_PLAYER')

    ID_User = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ID_USER_MARKET')

    itens = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='ITENS_LOJA_PLAYER')

    preco_Item = models.DecimalField(max_digits=999, decimal_places=2, default=0)

    def __str__(self):
        return str(f'{self.ID_User} {self.itens} {self.preco_Item}')


class RecompensaDiaria(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_RECOMP_DIARIA')

    # Por agora ele vai puxar so o ID, vamos pensar depois o que colocar e como colocar aqui dentro, para fazer a recompensa funcionar.

    def __str__(self):
        return str(f'')


class Deck(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_DECK')

    NomeDeck = models.CharField(max_length=999)

    quantidadeCartas = models.DecimalField(max_digits=64, decimal_places=0, default=64)

    cartas = models.ForeignKey(Carta, on_delete=models.CASCADE)

    precoDeck = models.DecimalField(max_digits=999, decimal_places=2, default=0)

    def __str__(self):
        return str(f'{self.ID} | {self.NomeDeck} | {self.quantidadeCartas} | {self.precoDeck}')


# O USUARIO PODE CRIAR MAIS DE UM DECK, PERGUNTAR SE ESTÁ CERTO.
class DeckUser(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_DECK')
    # Perguntar se é assim que cria varios decks para um usuario, atribuindo o ID dele no deck ou se atribui o ID do DECK ao user.
    IDUserDeck = models.ForeignKey(User, on_delete=models.CASCADE)

    NomeDeckUser = models.CharField(max_length=500)

    QuantidadeDeCartaUser = models.DecimalField(max_digits=999, decimal_places=0, default=64)

    cartasDeckUser = models.ForeignKey(Carta, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.ID} | {self.IDUserDeck} | {self.NomeDeckUser} | {self.QuantidadeDeCartaUser}')


class SistemaDeTroca(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_SIS_TROCA')

    ID_USER = models.ForeignKey(User, on_delete=models.CASCADE)

    ID_TROCA = models.ForeignKey(Carta, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.ID} {self.ID_USER} {self.ID_TROCA}')


class LootBox_Basic(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_LootBox_Basic')

    PrecoBasic = models.DecimalField(max_digits=999, decimal_places=2)

    PrecoPago = models.DecimalField(max_digits=999, decimal_places=2)

    sakuraBasica = models.ForeignKey(MoedaPadrao, on_delete=models.CASCADE)

    LotusPaga = models.ForeignKey(MoedaPaga, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.ID} {self.PrecoBasic} {self.PrecoPago}')


class LootBox_Medium(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_LootBox_Medium')

    PrecoMedium = models.DecimalField(max_digits=999, decimal_places=2)

    PrecoPagoMedium = models.DecimalField(max_digits=999, decimal_places=2)

    sakuraBasicaMedium = models.ForeignKey(MoedaPadrao, on_delete=models.CASCADE)

    LotusPagaMedium = models.ForeignKey(MoedaPaga, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.ID} {self.PrecoMedium} {self.PrecoPagoMedium}')


# As loot box precisam de um sistema pra randomificar a quantidade de itens, raridade, e Cartas.
class LootBox_Superior(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_LootBox_Superior')

    PrecoSuperior = models.DecimalField(max_digits=999, decimal_places=2)

    PrecoPagoSuperior = models.DecimalField(max_digits=999, decimal_places=2)

    sakuraBasicaSuperior = models.ForeignKey(MoedaPadrao, on_delete=models.CASCADE)

    LotusPagaSuperior = models.ForeignKey(MoedaPaga, on_delete=models.CASCADE)

    ItemLootBox = models.ForeignKey(Carta, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.ID} {self.PrecoSuperior} {self.PrecoPagoSuperior}')


class AscensaoCarta(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_LootBox_Superior')

    classeCartaASC = models.ForeignKey(Classe, on_delete=models.CASCADE)

    Primeira_Ascensao = models.DecimalField(max_digits=99, decimal_places=0)

    Segunda_Ascensao = models.DecimalField(max_digits=99, decimal_places=0)

    Terceira_Ascensao = models.DecimalField(max_digits=99, decimal_places=0)

    def __str__(self):
        return str(
            f'{self.ID} {self.classeCartaASC} {self.Primeira_Ascensao} {self.Segunda_Ascensao} {self.Terceira_Ascensao}')


# Ele tem que puxar o inventario do usuario para treinar a carta? Perguntar para o professor.
class CampoDeTreinamento(models.Model):
    ID = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                             verbose_name='ID_CAMPO_DE_TREINAMENTO')

    CartaParaUpar = models.ForeignKey(Carta, on_delete=models.CASCADE)

    Limite = models.DecimalField(max_digits=2, decimal_places=0)

    tempo = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(f'{self.ID} {self.CartaParaUpar} {self.Limite}')

# ME LEIA!!!!
# Perguntar para o professor sobre o retorno do def, se pode puxar duas ForeignKey para mostrar o nome nos logs.(COMPLETE)
# E perguntar sobre o ID das cartas, se fiz certo.
