from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("privacy/", views.privacy, name="privacy"),
    path(
        "app-ads.txt", RedirectView.as_view(url=staticfiles_storage.url("app-ads.txt")),
    ),
]
