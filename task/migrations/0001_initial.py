# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CrontabJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.CharField(max_length=500, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
                ('command', models.CharField(help_text=b'\xe6\xa0\xbc\xe5\xbc\x8f\xef\xbc\x9a f1 f2 f3 f4 f5 program\xef\xbc\x8c\xe5\x8f\x82\xe7\x85\xa7crontab\xe5\x91\xbd\xe4\xbb\xa4\xe8\xa1\x8c', max_length=1000, verbose_name=b'crontab\xe5\x91\xbd\xe4\xbb\xa4\xe8\xa1\x8c')),
                ('sql_ref', models.CharField(help_text=b'\xe8\xaf\xb7\xe5\xa1\xab\xe5\x86\x99\xe4\xbe\x9d\xe8\xb5\x96\xe7\x9a\x84\xe6\x95\xb0\xe6\x8d\xae\xe5\xba\x93\xe5\x90\x8d\xe3\x80\x81\xe8\xa1\xa8\xe5\x90\x8d\xef\xbc\x8c\xe8\x8b\xa5\xe6\x97\xa0\xe5\x88\x99\xe4\xb8\xba\xe7\xa9\xba', max_length=1000, verbose_name=b'\xe6\x95\xb0\xe6\x8d\xae\xe5\xba\x93\xe4\xbe\x9d\xe8\xb5\x96', blank=True)),
                ('redis_ref', models.CharField(help_text=b'\xe8\xaf\xb7\xe5\xa1\xab\xe5\x86\x99\xe4\xbe\x9d\xe8\xb5\x96\xe7\x9a\x84redis IP\xe3\x80\x81db', max_length=1000, verbose_name=b'Redis\xe4\xbe\x9d\xe8\xb5\x96', blank=True)),
                ('extra_ref', models.CharField(help_text=b'\xe5\x85\xb6\xe4\xbb\x96\xe8\xb5\x84\xe6\xba\x90\xe8\xaf\xb4\xe6\x98\x8e', max_length=1000, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96\xe8\xb5\x84\xe6\xba\x90', blank=True)),
                ('status', models.IntegerField(default=0, verbose_name=b'\xe6\x89\xa7\xe8\xa1\x8c\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe4\xb8\x8b\xe7\xba\xbf'), (1, b'\xe5\xbe\x85\xe5\x8a\xa0\xe5\x85\xa5'), (2, b'\xe6\x89\xa7\xe8\xa1\x8c\xe4\xb8\xad')])),
            ],
            options={
                'verbose_name': '\u5468\u671f\u4efb\u52a1',
                'verbose_name_plural': '\u5468\u671f\u4efb\u52a1',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=36, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('user', models.ManyToManyField(db_constraint=b'\xe9\xa1\xb9\xe7\x9b\xae\xe8\xb4\xa3\xe4\xbb\xbb\xe4\xba\xba', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'project',
            },
        ),
        migrations.AddField(
            model_name='crontabjob',
            name='project',
            field=models.ForeignKey(blank=True, to='task.Project', help_text=b'\xe6\x89\x80\xe5\xb1\x9e\xe4\xb8\x9a\xe5\x8a\xa1/\xe9\xa1\xb9\xe7\x9b\xae\xef\xbc\x8c\xe8\x8b\xa5\xe4\xb8\xba\xe4\xb8\xb4\xe6\x97\xb6\xe8\x84\x9a\xe6\x9c\xac\xe5\x8f\xaf\xe4\xb8\x8d\xe9\x80\x89'),
        ),
        migrations.AddField(
            model_name='crontabjob',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
