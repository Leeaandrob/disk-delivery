#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('diskdelivery.comidas.views',

    url(r'^novo/$', 'comida_nova', name='comida_nova'),
    url(r'^editar/(?P<comida_id>\d+)/$', 'comida_editar', name='comida_editar'),
    url(r'^lista/$','comida_lista', name='comida_lista'),

)