# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comidas', '0001_initial'),
        ('restaurantes', '0007_auto_20150210_0037'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCardapio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100, null=True, blank=True)),
                ('preco', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('comida', models.ForeignKey(to='comidas.Comida')),
                ('restaurante', models.ForeignKey(blank=True, to='restaurantes.Restaurante', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
