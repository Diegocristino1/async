from django.urls import path

from .views import contador_view, home_view

urlpatterns = [
    path("", home_view, name="home"),
    path("contador/", contador_view, name="contador"),
]
