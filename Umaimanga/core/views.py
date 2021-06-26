
from .forms import MangaForm
from django.shortcuts import render, redirect
from .models import Categoria, Manga


# Create your views here.
def UMAIMANGA(request):
    return render (request, 'core/UMAIMANGA.html')


def login(request):
    return render (request, 'core/login2.0.html')    



def register(request):
    return render (request, 'core/register.html')


def listado_Manga (request):
    mangas = Manga.objects.all()

    datos = {'mangas': mangas}
    
    return render(request, 'core/listado_Manga.html', datos)


def agregar_Manga(request):
    if request.method == 'POST':
        formulario = MangaForm(request.POST)
        if  formulario.is_valid:
            formulario.save()
            
            return redirect(to="listadoManga")
    else:
        datos = {'form': MangaForm()}        
        return render(request, 'core/agregar_Manga.html', datos)    



def editar_Manga (request, pk):
    manga = Manga.objects.get(Nombre=pk)

    if request.method == 'POST':
        formulario_edit = MangaForm(data=request.POST, instance=manga)
        if formulario_edit.is_valid:
            formulario_edit.save()
            
            return redirect(to="listadoManga")

    else:
        datos = {
        'form':MangaForm(instance=manga)
    }
        return render (request, 'core/editar_manga.html', datos)


def delete_Manga(request,pk):
    manga = Manga.objects.get(Nombre=pk)
    manga.delete()
    return redirect(to="listadoManga")

    



