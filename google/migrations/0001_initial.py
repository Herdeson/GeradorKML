# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocalizaImport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data da Cria\xe7\xe3o')),
                ('dataModificacao', models.DateTimeField(auto_now=True, verbose_name='Data da Modifica\xe7\xe3o')),
                ('status', models.BooleanField()),
                ('ip_host', models.CharField(max_length=15, null=True, blank=True)),
                ('conta', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('raio_mapa', models.IntegerField()),
                ('origem', models.CharField(max_length=10)),
                ('device_tag', models.IntegerField()),
                ('plataforma', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
