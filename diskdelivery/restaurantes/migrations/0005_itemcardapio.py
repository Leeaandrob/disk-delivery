# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0004_restaurante_comidas'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCardapio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100, null=True, blank=True)),
                ('preco', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('restaurante', models.ForeignKey(blank=True, to='restaurantes.Restaurante', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
