# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0002_auto_20150208_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='razao_social',
            field=models.CharField(default='a', max_length=100, verbose_name=b'Raz\xc3\xa3o Social'),
            preserve_default=False,
        ),
    ]
