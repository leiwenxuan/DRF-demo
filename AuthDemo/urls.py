from django.conf.urls import url, include
from django.contrib import admin
from .views import RegisterView, LoginView, TestView, PermissionView

urlpatterns = [
    url(r'^register', RegisterView.as_view()),
    url(r'^login', LoginView.as_view()),
    url(r'^test', TestView.as_view()),
    url(r'^permission', PermissionView.as_view()),

]