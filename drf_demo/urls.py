from django.contrib import admin
from django.urls import path, include
from demo import views
urlpatterns = [
    path('', views.demo_api, name='home'),
]
