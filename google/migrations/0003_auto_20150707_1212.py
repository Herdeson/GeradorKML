# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0002_auto_20150626_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationhistory',
            name='dataCriacao',
            field=models.DateField(auto_now_add=True, verbose_name='Data da Cria\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='locationhistory',
            name='dataModificacao',
            field=models.DateField(auto_now=True, verbose_name='Data da Modifica\xe7\xe3o'),
        ),
    ]
