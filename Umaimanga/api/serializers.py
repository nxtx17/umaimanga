from django.db.models import fields
from django.db.models.fields import Field
from rest_framework import serializers
from core.models import Manga


class MangaSerializer(serializers.ModelSerializer):
    class Meta :
        model = Manga
        fields =['Nombre', 'Categoria','idioma', 'imagen']