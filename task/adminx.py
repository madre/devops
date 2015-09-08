#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '6/9/15'
__author__ = 'deling.ma'
"""
import xadmin
from models import CrontabJob, Project


class ProjectAdmin(object):
    list_display = ["id", "name"]

xadmin.site.register(Project, ProjectAdmin)


class CrontabJobAdmin(object):
    list_display = ["id", "desc", "user", "project", "status"]
    # search_fields = ["code", "email"]
    list_filter = ["user", "project", "status"]
    raw_id_fields = ["desc"]

xadmin.site.register(CrontabJob, CrontabJobAdmin)
