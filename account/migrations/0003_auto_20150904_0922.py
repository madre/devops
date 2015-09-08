# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150904_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='portrait',
            field=models.CharField(default='', max_length=500, null=True, verbose_name='portrait'),
        ),
    ]
