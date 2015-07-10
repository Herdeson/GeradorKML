# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0003_auto_20150707_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationhistory',
            name='turno',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
    ]
