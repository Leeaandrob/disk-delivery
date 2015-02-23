#coding:utf-8
from django.db import models
from diskdelivery.core.models import Pessoa
from diskdelivery.comidas.models import Comida
# Create your models here.

class Restaurante(Pessoa):
	razao_social = models.CharField(max_length=100,verbose_name="Razão Social")
	cnpj = models.CharField(max_length=14,blank=True,null=True)
	comidas = models.ManyToManyField(Comida)

	def __unicode__(self):
		return self.razao_social
