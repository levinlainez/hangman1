import json
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
import random
from .forms import RegistroForm, LoginForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Categoria
from .models import Dificultad
from .models import PalabrasAhorcado
from .models import Puntuaciones
from .models import Juego
from .models import Intentos
from .models import Usuario


#no lo borres >:c
def home(request):
    categorias = Categoria.objects.all()  # Obtén todas las categorías
    dificultades = Dificultad.objects.all()  # Obtén todos los niveles de dificultad
    palabras_ahorcado = PalabrasAhorcado.objects.all()  # Obtén todas las palabras del ahorcado
    puntuaciones = Puntuaciones.objects.all()  # Obtén todas las puntuaciones
    juegos = Juego.objects.all()  # Obtén todos los juegos
    intentos = Intentos.objects.all()  # Obtén todos los intentos
    # Pasa todos los conjuntos de datos al contexto de la plantilla
    return render(request, 'home.html', {
        'categorias': categorias,
        'dificultades': dificultades,
        'palabras_ahorcado': palabras_ahorcado,
        'puntuaciones': puntuaciones,
        'juegos': juegos,
        'intentos': intentos
    })

def binary_operations(request):
    return render(request, 'binary_operations.html')

def obtener_pista(request):
    categoria_id = request.GET.get('categoria_id')
    dificultad_id = request.GET.get('dificultad_id')
    
    palabras_ahorcado = PalabrasAhorcado.objects.filter(categoria_id=categoria_id, dificultad_id=dificultad_id)
    
    if palabras_ahorcado.exists():
        palabras_usadas = set(request.session.get('palabras_usadas', []))
        palabras_disponibles = palabras_ahorcado.exclude(palabras__in=palabras_usadas)
        
        if palabras_disponibles.exists():
            pista_aleatoria = random.choice(palabras_disponibles)
            data = {'pista': pista_aleatoria.pistas, 'palabra': pista_aleatoria.palabras}
            request.session['palabras_usadas'] = list(palabras_usadas.union({pista_aleatoria.palabras}))
        else:
            data = {'pista': 'No hay más palabras disponibles.', 'palabra': None}
    else:
        data = {'pista': 'No se encontró ninguna pista.', 'palabra': None}
    
    return JsonResponse(data)


@csrf_exempt
def reset_palabras_usadas(request):
    if request.method == 'POST':
        request.session['palabras_usadas'] = []  # Reiniciar la lista de palabras usadas
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)





# Vista para listar todas las categorías
class CategoriaListView(ListView):
    model = Categoria
    fields = ['nombreCate', 'descripcion']
    template_name = '../templates/prueba.html'
    success_url = reverse_lazy('categoria_list')


# Vista para mostrar los detalles de una categoría
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = '../templates/prueba.html'

# Vista para crear una nueva categoría
class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nombreCate', 'descripcion']
    template_name = '../templates/prueba.html'
    success_url = reverse_lazy('categoria_create')
 
# Vista para actualizar una categoría existente
class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nombreCate', 'descripcion']
    template_name = '../templates/prueba.html'
    success_url = reverse_lazy('categoria_update')

# Vista para eliminar una categoría existente
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = '../templates/prueba.html'
    success_url = reverse_lazy('categoria_delete')
    
#muestre la informacion de dificultad
class DificultadListView(ListView):
    model = Dificultad
    fields = ['nivelDificultad']
    template_name = '../templates/prueba.html'
    success_url = reverse_lazy('deficultad_list')

#dificultad
class DificultadDetailView(DetailView):
    model = Dificultad
    template_name = '../templates/prueba.html'

#muestre las palabras
class PalabrasAhorcadoDetailView(DetailView):
    model = PalabrasAhorcado
    template_name = '../templates/prueba.html'

class PalabrasAhorcadoListView(ListView):
    model = PalabrasAhorcado
    fields = ['palabras','pistas']
    template_name = '../templates/prueba.html'
    success_url = reverse_lazy('palabrasAhorcado_list')


#lista las puntaciones
class PuntuacionesListView(ListView):
    model = Puntuaciones
    fields = ['puntaje']
    template_name = '../templates/prueba.html'
    success_url = reverse_lazy('puntuaciones_list')

#detalla las puntuaciones
class PuntuacionesDetailView(DetailView):
    model = Puntuaciones
    template_name = '../templates/prueba.html'

class PuntuacionesCreateView(CreateView):
    model = Puntuaciones
    fields = ['puntaje']
    template_name = '../templates/prueba.html'
    success_url = reverse_lazy('puntuaciones_create')

class PuntuacionesUpdateView(UpdateView):
    mode = Puntuaciones
    fields = ['puntaje']
    template_name = '../templates/prueba.html'
    success_url = reverse_lazy('puntuaciones_update')

#juegos
#lista las juegos
class JuegoListView(ListView):
    model = Juego
    fields = ['intentos_restantes','estado','fecha_inicio','fecha_fin','palabra_oculta']
    template_name = '../templates/prueba.html'
    success_url = reverse_lazy('juego_list')

#detalla  juegos
class JuegoDetailView(DetailView):
    model = Juego
    template_name = '../templates/prueba.html'

class JuegoCreateView(CreateView):
    model = Juego
    fields = ['intentos_restantes','estado','fecha_inicio','fecha_fin','palabra_oculta']
    template_name = '../templates/prueba.html'
    success_url = reverse_lazy('juego_create')

class JuegoUpdateView(UpdateView):
    mode = Juego
    fields = ['intentos_restantes','estado','fecha_inicio','fecha_fin','palabra_oculta']
    template_name = '../templates/prueba.html'
    success_url = reverse_lazy('juego_update')


#INTENTOS

#lista intentos
class IntentosListView(ListView):
    model = Intentos
    fields = ['letra','es_correcto','fecha_intento']
    template_name = '../templates/prueba.html'
    success_url = reverse_lazy('intentos_list')


#detalles intentos
class IntentosDetailView(DetailView):
    model = Intentos
    template_name = '../templates/prueba.html'

class IntentosCreateView(CreateView):
    model = Intentos
    fields = ['letra','es_correcto','fecha_intento']
    template_name = '../templates/prueba.html'
    success_url = reverse_lazy('intentos_create')

class IntentosUpdateView(UpdateView):
    mode = Intentos
    fields = ['letra','es_correcto','fecha_intento']
    template_name = '../templates/prueba.html'
    success_url = reverse_lazy('intentos_update')



def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            usuario = data.get('usuario')
            contrasena = data.get('password')
            if Usuario.objects.filter(usuario=usuario).exists():
                return JsonResponse({'success': False, 'message': 'El usuario ya existe.'})
            nuevo_usuario = Usuario(usuario=usuario, contrasena=contrasena)
            nuevo_usuario.save()
            return JsonResponse({'success': True, 'redirect_url': reverse('login')})  # Enviar URL de redirección
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Método no permitido'})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            usuario = data.get('usuario')
            contrasena = data.get('password')
            user = Usuario.objects.filter(usuario=usuario, contrasena=contrasena).first()
            if user:
                return JsonResponse({'success': True, 'redirect_url': reverse('home')})
            return JsonResponse({'success': False, 'message': 'Credenciales inválidas.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Método no permitido'})


# Vista para crear una nueva categoría
#class CategoriaCreateView(CreateView):
 #   model = Categoria
  #  fields = ['nombreCate', 'descripcion']
   # template_name = 'categoria_form.html'
    #success_url = reverse_lazy('categoria_list')

# Vista para actualizar una categoría existente
#class CategoriaUpdateView(UpdateView):
 #   model = Categoria
  #  fields = ['nombreCate', 'descripcion']
   # template_name = 'categoria_form.html'
    #success_url = reverse_lazy('categoria_list')

# Vista para eliminar una categoría existente
#class CategoriaDeleteView(DeleteView):
 #   model = Categoria
  #  template_name = 'categoria_confirm_delete.html'
   # success_url = reverse_lazy('categoria_list')

