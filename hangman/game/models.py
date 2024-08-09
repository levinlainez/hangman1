from django.db import models

# Modelo para la tabla 'categoria'
class Categoria(models.Model):
    nombreCate = models.CharField(max_length=100)  # Campo de texto con una longitud máxima de 100 caracteres
    descripcion = models.CharField(max_length=1000)  # Campo de texto con una longitud máxima de 1000 caracteres

    def __str__(self):
        return self.nombreCate  # Devuelve el nombre de la categoría como representación en cadena del objeto

# Modelo para la tabla 'dificultad'
class Dificultad(models.Model):
    nivelDificultad = models.CharField(max_length=50)  # Campo de texto con una longitud máxima de 50 caracteres

    def __str__(self):
        return self.nivelDificultad  # Devuelve el nivel de dificultad como representación en cadena del objeto



# Modelo para la tabla 'puntuaciones'
class Puntuaciones(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relación de clave foránea con la tabla 'categoria'
    dificultad = models.ForeignKey(Dificultad, on_delete=models.CASCADE)  # Relación de clave foránea con la tabla 'dificultad'
    puntaje = models.IntegerField()  # Campo entero para almacenar el puntaje

# Modelo para la tabla 'palabrasAhorcado'
class PalabrasAhorcado(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relación de clave foránea con la tabla 'categoria'
    dificultad = models.ForeignKey(Dificultad, on_delete=models.CASCADE)  # Relación de clave foránea con la tabla 'dificultad'
    palabras = models.CharField(max_length=100)  # Campo de texto para las palabras, longitud máxima de 100 caracteres
    pistas = models.CharField(max_length=100)  # Campo de texto para las pistas, longitud máxima de 100 caracteres
    
    def __str__(self):
        return f"{self.palabras} - {self.pistas}"


# Modelo para la tabla 'juego'
class Juego(models.Model):
    palabras = models.ForeignKey(PalabrasAhorcado, on_delete=models.CASCADE)  # Relación de clave foránea con la tabla 'palabrasAhorcado'
    intentos_restantes = models.IntegerField(default=6)  # Campo entero para los intentos restantes, por defecto 6
    estado = models.CharField(max_length=11, choices=[('en_progreso', 'En Progreso'), ('ganado', 'Ganado'), ('perdido', 'Perdido')], default='en_progreso')  # Campo de texto para el estado del juego con opciones
    fecha_inicio = models.DateTimeField(auto_now_add=True)  # Campo de fecha y hora para el inicio del juego, se añade automáticamente
    fecha_fin = models.DateTimeField(null=True, blank=True)  # Campo de fecha y hora para el fin del juego, puede ser nulo
    palabra_oculta = models.CharField(max_length=100)  # Campo de texto para la palabra oculta, longitud máxima de 100 caracteres

# Modelo para la tabla 'intentos'
class Intentos(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)  # Relación de clave foránea con la tabla 'juego'
    letra = models.CharField(max_length=1)  # Campo de texto para la letra intentada, longitud máxima de 1 caracter
    es_correcto = models.BooleanField()  # Campo booleano para indicar si el intento fue correcto
    fecha_intento = models.DateTimeField(auto_now_add=True)  # Campo de fecha y hora para el intento, se añade automáticamente

class Usuario(models.Model):
    id = models.AutoField
    usuario = models.CharField(max_length=150, unique=True)
    contrasena = models.CharField(max_length=128)

    def __str__(self):
        return self.usuario

import mysql.connector
from mysql.connector import Error

