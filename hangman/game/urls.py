from django.urls import path
from .views import (
    home,
    CategoriaListView, CategoriaDetailView,
    DificultadListView, DificultadDetailView,
    PalabrasAhorcadoListView, PalabrasAhorcadoDetailView,
    PuntuacionesListView, PuntuacionesDetailView, PuntuacionesCreateView, PuntuacionesUpdateView,
    JuegoListView, JuegoDetailView, JuegoCreateView, JuegoUpdateView,CategoriaDeleteView,
    IntentosListView, IntentosDetailView, IntentosCreateView, IntentosUpdateView,CategoriaCreateView,CategoriaCreateView, obtener_pista,reset_palabras_usadas
)

urlpatterns = [
    path('game/', home, name='home'),

    path('obtener_pista/', obtener_pista, name='obtener_pista'),
     path('reset_palabras_usadas/', reset_palabras_usadas, name='reset_palabras_usadas'),
    path('Categoria/', CategoriaListView.as_view(), name='categoria_list'),
    path('Categoria/<int:pk>/', CategoriaDetailView.as_view(), name='categoria_detail'),
    path('Categoria/new/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('Categoria/<int:pk>/edit/', CategoriaCreateView.as_view(), name='categoria_update'),
    path('Categoria/<int:pk>/delete/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('dificultades/', DificultadListView.as_view(), name='dificultad_list'),
    path('dificultades/<int:pk>/', DificultadDetailView.as_view(), name='dificultad_detail'),
    path('palabras/', PalabrasAhorcadoListView.as_view(), name='palabras_list'),
    path('palabras/<int:pk>/', PalabrasAhorcadoDetailView.as_view(), name='palabras_detail'),
    path('puntuaciones/', PuntuacionesListView.as_view(), name='puntuaciones_list'),
    path('puntuaciones/<int:pk>/', PuntuacionesDetailView.as_view(), name='puntuaciones_detail'),
    path('puntuaciones/new/', PuntuacionesCreateView.as_view(), name='puntuaciones_create'),
    path('puntuaciones/<int:pk>/edit/', PuntuacionesUpdateView.as_view(), name='puntuaciones_update'),
    path('juegos/', JuegoListView.as_view(), name='juego_list'),
    path('juegos/<int:pk>/', JuegoDetailView.as_view(), name='juego_detail'),
    path('juegos/new/', JuegoCreateView.as_view(), name='juego_create'),
    path('juegos/<int:pk>/edit/', JuegoUpdateView.as_view(), name='juego_update'),
    path('intentos/', IntentosListView.as_view(), name='intentos_list'),
    path('intentos/<int:pk>/', IntentosDetailView.as_view(), name='intentos_detail'),
    path('intentos/new/', IntentosCreateView.as_view(), name='intentos_create'),
    path('intentos/<int:pk>/edit/', IntentosUpdateView.as_view(), name='intentos_update'),

]
