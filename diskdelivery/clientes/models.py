#coding:utf-8
from django.db import models
from diskdelivery.core.models import Pessoa
# Create your models here.

SEXO = (
    ('m','Masculino'),
    ('f','Feminino'),
    )

class Cliente(Pessoa):
	sexo            = models.CharField(max_length=1,blank=True,null=True,choices=SEXO)
	nascimento  	= models.DateField(verbose_name='Data de Nascimento',blank=True,null=True)