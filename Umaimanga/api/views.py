
from django.shortcuts import render
from rest_framework.response import Response
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
        data =  JSONParser.parse(request)
        serializer =  MangaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
