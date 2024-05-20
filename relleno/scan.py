import tkinter as tk
from tkinter import colorchooser

# Definir los puntos del polígono
polygon_points = [(300, 200), (500, 200), (600, 400), (400, 500), (200, 400)]

# Función para dibujar el polígono
def draw_polygon(canvas):
    return canvas.create_polygon(polygon_points, outline="red")

# Función para rellenar el polígono
def fill_polygon(event, canvas, fill_color):
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    # Convertir coordenadas de la ventana a coordenadas del lienzo
    if is_point_inside_polygon(x, y, polygon_points):
        canvas.itemconfig("polygon", fill=fill_color, outline="red")

# Función para verificar si un punto está dentro de un polígono
def is_point_inside_polygon(x, y, polygon):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

# Función para seleccionar un color de relleno
def choose_fill_color():
    fill_color = colorchooser.askcolor()[1]
    if fill_color:
        return fill_color
    else:
        return None

# Función principal
def main():
    # Crear ventana principal
    root = tk.Tk()
    root.title("Relleno de Polígono")

    # Frame para los botones y el color seleccionado
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.LEFT, padx=10, pady=10)

    # Label para mostrar el color seleccionado
    selected_color_label = tk.Label(button_frame, width=10, height=2, bg="white")
    selected_color_label.pack(pady=5)

    # Botón para seleccionar color de relleno
    select_color_button = tk.Button(button_frame, text="Seleccionar Color", command=lambda: select_color(selected_color_label))
    select_color_button.pack(pady=5)

    # Botón para salir
    exit_button = tk.Button(button_frame, text="Salir", command=root.quit)
    exit_button.pack(pady=5)

    # Crear lienzo para dibujar
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack(side=tk.LEFT)

    # Dibujar el polígono
    draw_polygon(canvas)

    # Función para seleccionar el color de relleno
    def select_color(color_label):
        hex_fill_color = choose_fill_color()
        if hex_fill_color:
            fill_color_rgb = hex_to_rgb(hex_fill_color)
            color_label.config(bg=hex_fill_color)
            color_label.fill_color = fill_color_rgb
            # Enlazar el evento de clic en el lienzo aquí
            canvas.bind("<Button-1>", lambda event: fill_polygon(event, canvas, fill_color_rgb))

    # Función para convertir color hexadecimal a RGB
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    root.mainloop()

if __name__ == "__main__":
    main()
