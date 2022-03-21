# django
from django.urls import path

from base import views

urlpatterns = [
    path("ping", views.PingApiView.as_view(), name="ping"),
]
