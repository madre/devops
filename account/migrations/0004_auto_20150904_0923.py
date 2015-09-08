# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20150904_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='portrait',
            field=models.CharField(default='', max_length=500, verbose_name='portrait', blank=True),
        ),
    ]
