#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '6/9/15'
__author__ = 'deling.ma'
"""
import os
from django.shortcuts import redirect
from django.views.generic import FormView, ListView, TemplateView
from django.contrib import auth, messages
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q

from account.mixins import LoginRequiredMixin, SuperUserRequiredMixin
from account.utils import default_redirect
from models import CrontabJob, STATUS_CHOICES
from task.forms import CrontabForm


class CrontabListView(LoginRequiredMixin, ListView):
    model = CrontabJob
    template_name = "crontab_list.html"
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_superuser:
            return CrontabJob.objects.order_by("-status")
        return CrontabJob.objects.filter(Q(project__user=self.request.user) |
                                         Q(user=self.request.user)).distinct().order_by("-status")


class CrontabView(LoginRequiredMixin, FormView):
    template_name = "add_crontab.html"
    form_class = CrontabForm
    redirect_field_name = "next"
    messages = {
        "add_crontab": {
            "level": messages.SUCCESS,
            "text": "add new crontab."
        },
    }

    def get_initial(self):
        initial = super(CrontabView, self).get_initial()
        if self.kwargs.get("id"):
            crontab_obj = get_object_or_404(CrontabJob, id=self.kwargs['id'])
            initial["id"] = crontab_obj.id
            initial["desc"] = crontab_obj.desc
            initial["project"] = crontab_obj.project
            initial["command"] = crontab_obj.command
            initial["sql_ref"] = crontab_obj.sql_ref
            initial["redis_ref"] = crontab_obj.redis_ref
            initial["extra_ref"] = crontab_obj.extra_ref
            initial["status"] = crontab_obj.status
        return initial

    def form_valid(self, form):
        self.add_crontab(form)
        if self.messages.get("add_crontab"):
            messages.add_message(
                self.request,
                self.messages["add_crontab"]["level"],
                self.messages["add_crontab"]["text"]
            )
        return redirect(self.get_success_url(reverse("crontab_list")))

    def add_crontab(self, form):
        fields = form.cleaned_data
        if fields:
            if not self.kwargs.get("id"):
                crontab_obj = CrontabJob()
            else:
                crontab_obj = get_object_or_404(CrontabJob, id=self.kwargs["id"])
                self.messages["add_crontab"]["text"] = "update crontab success"
            crontab_obj.user = self.request.user
            for k, v in fields.items():
                setattr(crontab_obj, k, v)
            crontab_obj.save()

    def get_context_data(self, **kwargs):
        ctx = kwargs
        redirect_field_name = self.get_redirect_field_name()
        ctx.update({
            "redirect_field_name": redirect_field_name,
            "redirect_field_value":
                self.request.POST.get(redirect_field_name,
                                      self.request.GET.get(redirect_field_name, "")),
        })
        return ctx

    def get_redirect_field_name(self):
        return self.redirect_field_name

    def get_success_url(self, fallback_url=None, **kwargs):
        kwargs.setdefault("redirect_field_name", self.get_redirect_field_name())
        return default_redirect(self.request, fallback_url, **kwargs)


class ExecuteCrontab(LoginRequiredMixin, SuperUserRequiredMixin, TemplateView):
    template_name = "execute_crontab.html"
    messages = {
        "excute_crontab": {
            "level": messages.SUCCESS,
            "text": "部署执行成功，crontab每5分钟更新一次，请5分钟后确认执行结果！"
        },
    }

    def get_context_data(self, **kwargs):
        context = super(ExecuteCrontab, self).get_context_data(**kwargs)
        queryset = CrontabJob.objects.exclude(status=-1)
        file_name = "crontab"
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
        with open(file_path, "wb") as crontab_file:
            for each in queryset:
                crontab_file.write("%s\n" % each.command.encode("utf-8"))
                each.status = 1
                each.save()
        if self.messages.get("excute_crontab"):
            messages.add_message(
                self.request,
                self.messages["excute_crontab"]["level"],
                self.messages["excute_crontab"]["text"]
            )
        return context
