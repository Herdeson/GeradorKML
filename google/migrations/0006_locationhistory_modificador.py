# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('google', '0005_auto_20150713_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationhistory',
            name='modificador',
            field=models.ForeignKey(default=1, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
