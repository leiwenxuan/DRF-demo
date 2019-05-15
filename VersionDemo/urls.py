from django.conf.urls import url, include
from django.contrib import admin
from .views import DemoView

urlpatterns = [
    url(r'^version_demo/', DemoView.as_view()),
]