import pygame
import tkinter as tk
from tkinter import colorchooser
import sys

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

# Definir colores predeterminados
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Definir colores seleccionados
fill_color = WHITE
border_color = RED

# Función para obtener el color de un píxel


def get_pixel(x, y):
    return screen.get_at((x, y))

# Función para establecer el color de un píxel


def set_pixel(x, y, color):
    screen.set_at((x, y), color)

# Algoritmo de relleno por inundación (flood fill)


def flood_fill(x, y, target_color, fill_color):
    current_color = get_pixel(x, y)

    # Verificar si el píxel está dentro del área de relleno y no ha sido coloreado
    if current_color == target_color:
        set_pixel(x, y, fill_color)  # Colorear el píxel actual

        # Aplicar recursión a los píxeles adyacentes
        if x > 0:
            flood_fill(x - 1, y, target_color, fill_color)
        if x < WIDTH - 1:
            flood_fill(x + 1, y, target_color, fill_color)
        if y > 0:
            flood_fill(x, y - 1, target_color, fill_color)
        if y < HEIGHT - 1:
            flood_fill(x, y + 1, target_color, fill_color)

# Función para abrir la paleta de colores y seleccionar un color


def select_color(label):
    global fill_color, border_color
    color = colorchooser.askcolor(title="Seleccionar color")
    if color[1]:
        label.config(bg=color[1])
        if label == fill_color_label:
            fill_color = color[1]
        else:
            border_color = color[1]

# Función para ejecutar el algoritmo de relleno por inundación


def run_flood_fill():
    pygame.draw.rect(screen, border_color, (200, 200, 400, 300), 2)
    flood_fill(300, 300, border_color, fill_color)
    pygame.display.flip()

# Función para salir del programa


def quit_program():
    pygame.quit()
    sys.exit()


# Crear ventana de Tkinter
root = tk.Tk()
root.title("Flood Fill Algorithm")

# Etiqueta para seleccionar color de relleno
fill_color_label = tk.Label(
    root, text="Color de Relleno", bg="white", padx=10, pady=5)
fill_color_label.pack(pady=5)
fill_color_label.bind(
    "<Button-1>", lambda event: select_color(fill_color_label))

# Etiqueta para seleccionar color de borde
border_color_label = tk.Label(
    root, text="Color de Borde", bg="red", padx=10, pady=5)
border_color_label.pack(pady=5)
border_color_label.bind(
    "<Button-1>", lambda event: select_color(border_color_label))

# Botón para ejecutar el algoritmo de relleno
run_button = tk.Button(root, text="Ejecutar Relleno",
                       command=run_flood_fill, padx=10, pady=5)
run_button.pack(pady=10)

# Botón para salir del programa
quit_button = tk.Button(
    root, text="Salir", command=quit_program, padx=10, pady=5)
quit_button.pack(pady=5)

# Crear ventana de Pygame
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flood Fill Algorithm")

# Bucle principal de Tkinter
root.mainloop()
