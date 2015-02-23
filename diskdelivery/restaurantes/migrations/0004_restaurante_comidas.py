# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comidas', '0001_initial'),
        ('restaurantes', '0003_restaurante_razao_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='comidas',
            field=models.ManyToManyField(to='comidas.Comida'),
            preserve_default=True,
        ),
    ]
