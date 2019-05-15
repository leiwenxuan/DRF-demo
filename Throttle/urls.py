from django.conf.urls import url, include
from django.contrib import admin
from .views import TestView

urlpatterns = [
    url(r'^test', TestView.as_view()),
]