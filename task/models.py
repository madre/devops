#!/usr/bin/env python
# coding=utf-8
"""
task 任务定制
__created__ = '6/9/15'
__author__ = 'deling.ma'
"""
from django.conf import settings
from django.db import models
# from django.utils.translation import ugettext_lazy as _

JOB_TYPE_CHOICES = []

STATUS_CHOICES = (
    (0, "待加入"),
    (1, "执行中"),
    (-1, "下线"),
)


class Project(models.Model):
    name = models.CharField("项目名称", max_length=36, unique=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, "项目责任人")

    class Meta:
        verbose_name = "业务项目"
        verbose_name_plural = "业务项目"

    def __unicode__(self):
        return self.name


class CrontabJob(models.Model):
    desc = models.CharField("简介", max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    project = models.ForeignKey(Project, blank=True, null=True,
                                help_text="所属业务/项目，若为临时脚本可不选")
    command = models.CharField("crontab命令行", max_length=1000,
                               help_text="格式：minute hour day month week command:分 时 日 月 周 命令，"
                                         "参照<a href='http://man.linuxde.net/crontab' target='_blank'>crontab命令行</a>")
    sql_ref = models.CharField("数据库依赖", blank=True, max_length=1000,
                               help_text="请填写依赖的数据库名、表名，若无则为空")
    redis_ref = models.CharField("Redis依赖", blank=True, max_length=1000,
                                 help_text="请填写依赖的redis IP、db")
    extra_ref = models.CharField("其他资源", max_length=1000, blank=True,
                                 help_text="其他资源说明")
    status = models.IntegerField("执行状态", default=0, choices=STATUS_CHOICES)
    ctime = models.DateTimeField("创建时间", auto_created=True)
    utime = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        verbose_name = "crontab"
        verbose_name_plural = "crontab"

    def __unicode__(self):
        return self.desc

    def __str__(self):
        return str(self.desc)
