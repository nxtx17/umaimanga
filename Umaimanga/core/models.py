from django.db import models

# Create your models here.

#modelo para categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id Categoria")
    nombreCategoria = models.CharField(max_length=60, verbose_name="Nombre de la Categoria")


    def __str__(self):
        return self.nombreCategoria


class Manga(models.Model):
    Nombre = models.CharField(max_length=60, primary_key=True, verbose_name="Nombre del manga ")
    Categoria = models.ForeignKey(Categoria , on_delete=models.CASCADE)
    idioma = models.CharField(max_length=20, verbose_name="Idioma del Manga")
    imagen = models.ImageField(null = True, blank = True)

    def __str__(self): 
        return self.Nombre