from django.urls import path

from Receitas.views import home

urlpatterns = [
    path('home/', home)
]
