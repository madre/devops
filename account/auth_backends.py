from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from account.utils import get_user_lookup_kwargs


class UsernameAuthenticationBackend(ModelBackend):

    def authenticate(self, **credentials):
        User = get_user_model()
        lookup_kwargs = get_user_lookup_kwargs({
            "{username}__iexact": credentials["username"]
        })
        try:
            user = User.objects.get(**lookup_kwargs)
        except (User.DoesNotExist, KeyError):
            return None
        else:
            try:
                if user.check_password(credentials["password"]):
                    return user
            except KeyError:
                return None


class EmailAuthenticationBackend(ModelBackend):

    def authenticate(self, **credentials):
        User = get_user_model()
        qs = User.objects.filter(verified=True)
        try:
            user_obj = qs.get(email__iexact=credentials["username"])
        except (User.DoesNotExist, KeyError):
            return None
        else:
            try:
                if user_obj.check_password(credentials["password"]):
                    return user_obj
            except KeyError:
                return None
