#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '6/9/15'
__author__ = 'deling.ma'
"""

from django.conf.urls import patterns, url
from task.views import CrontabView, CrontabListView, ExecuteCrontab

urlpatterns = patterns(
    "",
    url(r"^crontab/$", CrontabListView.as_view(), name="crontab_list"),
    url(r"^add/crontab/$", CrontabView.as_view(), name="add_crontab"),
    url(r"^crontab/(?P<id>\d+)/$", CrontabView.as_view(), name="edit_crontab"),
    url(r"^execute/crontab/$", ExecuteCrontab.as_view(), name="execute_crontab"),
)
