from django.db import models


# Create your models here.

class Categoria(models.Model):
    nomec = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomec


class Carta(models.Model):
    data = models.DateTimeField()
    nome = models.CharField(max_length=50)
    imagem = models.CharField(max_length=500)
    descricao = models.CharField(max_length=400)
    valor = models.DecimalField(max_digits=30, decimal_places=2)
    level = models.DecimalField(max_digits=2, decimal_places=0)
    afinidade = models.DecimalField(max_digits=3, decimal_places=1)
    exp = models.DecimalField(max_digits=3, decimal_places=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    # Testando upload Github...

    def __str__(self):
        return self.nome
