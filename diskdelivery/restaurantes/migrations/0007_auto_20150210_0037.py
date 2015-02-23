# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0006_itemcardapio_comida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcardapio',
            name='comida',
        ),
        migrations.RemoveField(
            model_name='itemcardapio',
            name='restaurante',
        ),
        migrations.DeleteModel(
            name='ItemCardapio',
        ),
    ]
