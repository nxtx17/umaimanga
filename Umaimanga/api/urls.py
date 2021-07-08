from django.urls import path

from .views import apiManga



urlpatterns = [
    path('mangas/', apiManga, name="api_manga"),
]