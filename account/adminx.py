# coding=utf-8
from django.contrib.sites.models import Site
import xadmin
from xadmin import views
from account.models import Account, SignupCode
from pinax.eventlog.models import Log
from task.models import CrontabJob


class SiteAdmin(object):
    list_display = ["id", "domain", "name"]

xadmin.site.register(Site, SiteAdmin)


class LogAdmin(object):
    list_display = ["id", "user", "action", "content_type", "timestamp"]
    search_fields = ["action", "user"]

xadmin.site.register(Log, LogAdmin)


class SignupCodeAdmin(object):

    list_display = ["code", "max_uses", "use_count", "expiry", "created"]
    search_fields = ["code", "email"]
    list_filter = ["created"]
    raw_id_fields = ["inviter"]

xadmin.site.register(SignupCode, SignupCodeAdmin)


class AccountAdmin(object):
    list_display = ["id", "user", "nickname", "email_verified", ]
    search_fields = ["user", "nickname"]
    list_filter = ["email_verified"]

xadmin.site.register(Account, AccountAdmin)


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSetting(object):
    global_search_models = [Log, Account, CrontabJob]
    global_models_icon = {
        Account: 'fa fa-cloud'
    }
    menu_style = 'accordion'  # 'default'
    site_title = u'dianjoy devops'
    site_footer = u"Copyright © 2015 点乐"
    # menu_template = 'xadmin/includes/sitemenu_accordion.html'


xadmin.site.register(views.CommAdminView, GlobalSetting)

