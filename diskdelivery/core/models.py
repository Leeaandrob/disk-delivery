#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User,Group


class Pessoa(User):
    '''
        @Pessoa: Modelo para uma nova pessoa
    ''' 
    telefone            = models.CharField(max_length=11,blank=True,null=True)
    endereco            = models.CharField(max_length=30,blank=True,null=True,verbose_name='Endereço')
    bairro              = models.CharField(max_length=20,blank=True,null=True)
    municipio           = models.CharField(max_length=20,blank=True,null=True)
    estado              = models.CharField(max_length=20,blank=True,null=True)
    grupo               = models.ForeignKey(Group,blank=True,null=True)

    def __unicode__(self):
        return self.first_name

