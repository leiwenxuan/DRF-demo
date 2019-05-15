from django.conf.urls import url, include
from django.contrib import admin
from .views import BookView


urlpatterns = [
    url(r'^book', BookView.as_view()),
    
]