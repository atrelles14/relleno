import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageTk, ImageDraw

# Definir los puntos del polígono
polygon_points = [(300, 200), (500, 200), (600, 400), (400, 500), (200, 400)]

# Función para dibujar el polígono
def draw_polygon(draw):
    draw.polygon(polygon_points, outline="red")

# Algoritmo de relleno de paridad (Parity Fill)
def parity_fill(x, y, target_color, fill_color, image):
    stack = [(x, y)]  # Pila para almacenar píxeles a procesar
    target_color = image.getpixel((x, y))  # Color del píxel inicial
    while stack:
        x, y = stack.pop()  # Obtener las coordenadas del píxel superior de la pila
        # Verificar si el píxel actual es del color objetivo
        if image.getpixel((x, y)) == target_color:
            image.putpixel((x, y), fill_color)  # Colorear el píxel actual
            # Agregar píxeles adyacentes a la pila si cumplen con las condiciones
            if x > 0:
                stack.append((x - 1, y))
            if x < image.width - 1:
                stack.append((x + 1, y))
            if y > 0:
                stack.append((x, y - 1))
            if y < image.height - 1:
                stack.append((x, y + 1))

# Función para seleccionar un color de relleno
def choose_fill_color():
    fill_color = colorchooser.askcolor()[1]
    if fill_color:
        return fill_color
    else:
        return None

# Función para convertir color hexadecimal a RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Función principal
def main():
    # Crear ventana principal
    root = tk.Tk()
    root.title("Parity Fill Algorithm")

    # Frame para los botones y el color seleccionado
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.LEFT, padx=10, pady=10)

    # Label para mostrar el color seleccionado
    selected_color_label = tk.Label(button_frame, width=10, height=2, bg="white")
    selected_color_label.pack(pady=5)

    # Botón para seleccionar color de relleno
    select_color_button = tk.Button(button_frame, text="Seleccionar Color", command=lambda: select_color(selected_color_label))
    select_color_button.pack(pady=5)

    # Botón para ejecutar el relleno
    fill_button = tk.Button(button_frame, text="Ejecutar Relleno", command=lambda: fill_polygon(canvas, image, selected_color_label))
    fill_button.pack(pady=5)

    # Botón para salir
    exit_button = tk.Button(button_frame, text="Salir", command=root.quit)
    exit_button.pack(pady=5)

    # Crear lienzo para dibujar
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack(side=tk.LEFT)

    # Crear una imagen en blanco
    image = Image.new("RGB", (800, 600), "white")

    # Dibujar el polígono en la imagen
    draw = ImageDraw.Draw(image)
    draw_polygon(draw)

    # Actualizar el lienzo con la imagen
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor='nw', image=photo)
    canvas.image = photo

    # Función para seleccionar el color de relleno
    def select_color(color_label):
        hex_fill_color = choose_fill_color()
        if hex_fill_color:
            fill_color_rgb = hex_to_rgb(hex_fill_color)
            color_label.config(bg=hex_fill_color)
            color_label.fill_color = fill_color_rgb

    # Función para rellenar el polígono con el color seleccionado
    def fill_polygon(canvas, image, color_label):
        if hasattr(color_label, 'fill_color'):
            fill_color_rgb = color_label.fill_color
            parity_fill(300, 300, (255, 0, 0), fill_color_rgb, image)
            photo = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, anchor='nw', image=photo)
            canvas.image = photo

    root.mainloop()

if __name__ == "__main__":
    main()
