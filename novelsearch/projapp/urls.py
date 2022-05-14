from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path(r'(?P<album_name>[a-zA-Z ]+)$', views.album, name='album')
]