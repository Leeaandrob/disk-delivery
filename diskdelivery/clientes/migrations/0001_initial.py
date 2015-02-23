# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('pessoa_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Pessoa')),
                ('cpf', models.CharField(max_length=14, null=True, blank=True)),
                ('identidade', models.CharField(max_length=15, null=True, verbose_name=b'Identidade', blank=True)),
                ('sexo', models.CharField(blank=True, max_length=1, null=True, choices=[(b'm', b'Masculino'), (b'f', b'Feminino')])),
                ('nascimento', models.DateField(null=True, verbose_name=b'Data de Nascimento', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('core.pessoa',),
        ),
    ]
