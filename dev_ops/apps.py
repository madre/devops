from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "dev_ops"

    def ready(self):
        import_module("dev_ops.receivers")
