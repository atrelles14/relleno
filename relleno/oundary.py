import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

# Definir colores
WHITE = (255, 205, 55)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Crear ventana
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Boundary Fill Algorithm")

# Algoritmo de relleno de límites (Boundary Fill) utilizando un enfoque iterativo


def boundary_fill(x, y, boundary_color, fill_color):
    stack = [(x, y)]  # Pila para almacenar píxeles a procesar

    while stack:
        x, y = stack.pop()  # Obtener las coordenadas del píxel superior de la pila
        if screen.get_at((x, y)) != boundary_color and screen.get_at((x, y)) != fill_color:
            screen.set_at((x, y), fill_color)  # Colorear el píxel actual

            # Agregar píxeles adyacentes a la pila si cumplen con las condiciones
            if x > 0:
                stack.append((x - 1, y))
            if x < WIDTH - 1:
                stack.append((x + 1, y))
            if y > 0:
                stack.append((x, y - 1))
            if y < HEIGHT - 1:
                stack.append((x, y + 1))


# Dibujar un rectángulo rojo como límite
pygame.draw.rect(screen, RED, (200, 200, 400, 300), 2)

# Llamar al algoritmo de relleno de límites
boundary_fill(300, 300, RED, WHITE)

# Actualizar la pantalla
pygame.display.flip()

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
