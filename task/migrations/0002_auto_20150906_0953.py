# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '\u4e1a\u52a1\u9879\u76ee', 'verbose_name_plural': '\u4e1a\u52a1\u9879\u76ee'},
        ),
        migrations.AlterField(
            model_name='crontabjob',
            name='project',
            field=models.ForeignKey(blank=True, to='task.Project', help_text=b'\xe6\x89\x80\xe5\xb1\x9e\xe4\xb8\x9a\xe5\x8a\xa1/\xe9\xa1\xb9\xe7\x9b\xae\xef\xbc\x8c\xe8\x8b\xa5\xe4\xb8\xba\xe4\xb8\xb4\xe6\x97\xb6\xe8\x84\x9a\xe6\x9c\xac\xe5\x8f\xaf\xe4\xb8\x8d\xe9\x80\x89', null=True),
        ),
    ]
