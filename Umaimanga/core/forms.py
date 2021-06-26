from django import forms
from django.forms import ModelForm
from .models import Manga

#crear la clase del formulario manga


class MangaForm(ModelForm):

    class Meta :
        model = Manga
        fields =['Nombre', 'Categoria','idioma', 'imagen']