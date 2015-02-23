#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('diskdelivery.restaurantes.views',

    url(r'^novo/$', 'restaurante_novo', name='restaurante_novo'),
    url(r'^editar/(?P<restaurante_id>\d+)/$', 'restaurante_editar', name='restaurante_editar'),
    url(r'^lista/$','restaurante_lista', name='restaurante_lista'),
)