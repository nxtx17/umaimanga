from django.urls import path
from .views import UMAIMANGA, login , register ,listado_Manga, agregar_Manga ,editar_Manga,delete_Manga

urlpatterns = [
    path('', UMAIMANGA , name="UMAIMANGA"),
    path('login/',login, name="login"),
    path ('register/',register, name="register" ),
    path ('listadoManga/', listado_Manga, name="listadoManga"),
    path('agregar_Manga/', agregar_Manga, name="agregar_Manga"),
    path('editar-manga/<pk>', editar_Manga, name="editarManga"),
    path('eliminar-manga/<pk>', delete_Manga, name="deleteManga")
   

]