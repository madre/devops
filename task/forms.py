#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '6/9/15'
__author__ = 'deling.ma'
"""
from django import forms
from models import CrontabJob


class CrontabForm(forms.ModelForm):
    class Meta:
        model = CrontabJob
        fields = ['id', 'desc', 'project', 'command', 'sql_ref',
                  'redis_ref', 'extra_ref']
