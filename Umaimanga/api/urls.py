from django.urls import path

from .views import apiManga, detalle_manga



urlpatterns = [
    path('manga/', apiManga, name="api_manga"),
    path('manga/<pk>',detalle_manga,name="detalleManga" )
]