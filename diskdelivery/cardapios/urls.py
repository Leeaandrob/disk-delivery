#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('diskdelivery.cardapios.views',

    url(r'^novo/$', 'itemcardapio_novo', name='itemcardapio_novo'),
    url(r'^editar/(?P<item_id>\d+)/$', 'itemcardapio_editar', name='itemcardapio_editar'),
    url(r'^meu_cardapio/$','cardapio_lista', name='cardapio_lista'),

)