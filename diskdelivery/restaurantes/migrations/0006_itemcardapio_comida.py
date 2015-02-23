# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comidas', '0001_initial'),
        ('restaurantes', '0005_itemcardapio'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcardapio',
            name='comida',
            field=models.ForeignKey(default=1, to='comidas.Comida'),
            preserve_default=False,
        ),
    ]
