# coding=utf-8
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()


urlpatterns = patterns(
    "",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^backend/', include(xadmin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r"^task/", include("task.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
