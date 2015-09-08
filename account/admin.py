from __future__ import unicode_literals

from django.contrib import admin

from account.models import Account, SignupCode


class SignupCodeAdmin(admin.ModelAdmin):

    list_display = ["code", "max_uses", "use_count", "expiry", "created"]
    search_fields = ["code", "email"]
    list_filter = ["created"]
    raw_id_fields = ["inviter"]


class AccountAdmin(admin.ModelAdmin):

    raw_id_fields = ["user"]


admin.site.register(Account, AccountAdmin)
admin.site.register(SignupCode, SignupCodeAdmin)
