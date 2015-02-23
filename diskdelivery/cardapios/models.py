#coding:utf-8
from django.db import models
from diskdelivery.comidas.models import Comida
from diskdelivery.restaurantes.models import Restaurante
# Create your models here.

class ItemCardapio(models.Model):
	restaurante = models.ForeignKey(Restaurante,blank=True,null=True)
	nome = models.CharField(max_length=100)
	descricao = models.CharField(max_length=100,blank=True,null=True)
	preco = models.DecimalField(default=0.0,max_digits=10,decimal_places=2)
	comida = models.ForeignKey(Comida)