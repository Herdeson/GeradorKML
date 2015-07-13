# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0004_locationhistory_turno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationhistory',
            name='turno',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'1', b'Manh\xc3\xa3'), (b'2', b'Tarde'), (b'3', b'Noite'), (b'4', b'Madrugada')]),
        ),
    ]
