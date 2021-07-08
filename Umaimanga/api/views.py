from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import MangaSerializer
from core.models import Manga
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view




@api_view(['GET', 'POST'])
def apiManga(request):
    if request.method == 'GET':
        """
        lista de todos los mangas
        """
        manga = Manga.objects.all()
        serializer = MangaSerializer(manga, many= True)
        return Response (serializer.data)
    elif request.method == 'POST':
        data =  JSONParser().parse(request)
        serializer =  MangaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET', 'PUT', 'DELETE'])
def detalle_manga(request, pk):
    try:
        manga = Manga.objects.get(Nombre=pk)
    except Manga.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND) 
        "GET: Muestra  detalle de los mangas por nombre "


    if request.method =='GET':
       serializer = MangaSerializer(manga)
       return Response(serializer.data)

       "PUT: editar un manga por nombre" 


    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MangaSerializer(manga, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':

        """
        DELETE: Borrar un manga por nombre
        """

        manga.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
