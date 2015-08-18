# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('google', '0006_locationhistory_modificador'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArqGerados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataCriacao', models.DateField(auto_now_add=True, verbose_name='Data da Cria\xe7\xe3o')),
                ('dataModificacao', models.DateField(auto_now=True, verbose_name='Data da Modifica\xe7\xe3o')),
                ('status', models.BooleanField()),
                ('ip_host', models.CharField(max_length=15, null=True, blank=True)),
                ('arquivo', models.FilePathField()),
                ('modificador', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
