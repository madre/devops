# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20150906_0953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='crontabjob',
            options={'verbose_name': '\u5b9a\u65f6\u4efb\u52a1', 'verbose_name_plural': '\u5b9a\u65f6\u4efb\u52a1'},
        ),
        migrations.AddField(
            model_name='crontabjob',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 7, 9, 48, 46, 959343, tzinfo=utc), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', auto_created=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crontabjob',
            name='utime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 7, 9, 48, 52, 909638, tzinfo=utc), verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='crontabjob',
            name='command',
            field=models.CharField(help_text=b"\xe6\xa0\xbc\xe5\xbc\x8f\xef\xbc\x9aminute hour day month week command:\xe5\x88\x86 \xe6\x97\xb6 \xe6\x97\xa5 \xe6\x9c\x88 \xe5\x91\xa8 \xe5\x91\xbd\xe4\xbb\xa4\xef\xbc\x8c\xe5\x8f\x82\xe7\x85\xa7<a href='http://man.linuxde.net/crontab' target='_blank'>crontab\xe5\x91\xbd\xe4\xbb\xa4\xe8\xa1\x8c</a>", max_length=1000, verbose_name=b'crontab\xe5\x91\xbd\xe4\xbb\xa4\xe8\xa1\x8c'),
        ),
        migrations.AlterField(
            model_name='crontabjob',
            name='status',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x89\xa7\xe8\xa1\x8c\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe5\xbe\x85\xe5\x8a\xa0\xe5\x85\xa5'), (1, b'\xe6\x89\xa7\xe8\xa1\x8c\xe4\xb8\xad'), (-1, b'\xe4\xb8\x8b\xe7\xba\xbf')]),
        ),
    ]
