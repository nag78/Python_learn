"""Определяет схемы URL для пользователей"""
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'
urlpatterns = [
    # Страница входа
    url(r'^login/$', LoginView.as_view(), name='login'),

    # Страница выхода
    url(r'^logout/$', views.logout_view, name='logout'),
]
