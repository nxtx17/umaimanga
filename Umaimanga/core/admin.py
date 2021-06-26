from django.contrib import admin
from .models import Manga, Categoria

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Manga)