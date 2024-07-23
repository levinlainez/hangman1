from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Categoria
from .models import Dificultad
from .models import PalabrasAhorcado
from .models import Puntuaciones
from .models import Juego
from .models import Intentos


#no lo borres >:c
def home(request):
    return render(request, 'home.html')

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

