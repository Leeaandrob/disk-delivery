# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telefone', models.CharField(max_length=11, null=True, blank=True)),
                ('endereco', models.CharField(max_length=30, null=True, verbose_name=b'Endere\xc3\xa7o', blank=True)),
                ('bairro', models.CharField(max_length=20, null=True, blank=True)),
                ('municipio', models.CharField(max_length=20, null=True, blank=True)),
                ('estado', models.CharField(max_length=20, null=True, blank=True)),
                ('grupo', models.ForeignKey(blank=True, to='auth.Group', null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
    ]
