from tkinter import *
import customtkinter as ctk
from PIL import Image
import subprocess

# Estilos de fuente
font_style1 = ("Helvetica", 14, "bold")
font_style2 = ("Helvetica", 16, "bold")
font_style3 = ("Helvetica", 13)

ctk.set_appearance_mode("light")

# Cambiar ruta de archivo


def dda():
    subprocess.Popen(["python", "relleno\oundary.py"])


def bren():
    subprocess.Popen(["python", "relleno\loodfill.py"])


def circunferencia():
    subprocess.Popen(["python", "relleno\parity.py"])


def elipse():
    subprocess.Popen(["python", "relleno\scan.py"])


def presentacion():
    for widget in root.winfo_children():
        widget.destroy()

    # Título
    ctk.CTkLabel(root, text="Proyecto No.2", font=("Helvetica", 20, "bold")).place(
        relx=0.5, rely=0.2, anchor="center")

    # Descripción del proyecto
    ctk.CTkLabel(root, text="Computación Gráfica y Visual", font=(
        "Helvetica", 16, "bold")).place(relx=0.5, rely=0.3, anchor="center")
    ctk.CTkLabel(root, text="Manejo de Elementos Gráficos en Entornos Digitales", font=(
        "Helvetica", 14)).place(relx=0.5, rely=0.4, anchor="center")

    # Información del facilitador y los estudiantes
    facilitador_info = "Facilitador:\nIng. Mark Tack"
    estudiantes_info = "\nEstudiantes:\nAdriana González (8-997-2009)\nJesús Linares (8-979-1507)\n1SF142"
    ctk.CTkLabel(root, text=facilitador_info, font=("Helvetica", 14),
                 justify="center").place(relx=0.5, rely=0.5, anchor="center")
    ctk.CTkLabel(root, text=estudiantes_info, font=("Helvetica", 14),
                 justify="center").place(relx=0.5, rely=0.6, anchor="center")

    # Botón de menú
    ctk.CTkButton(root, text="Menú", command=menu, font=font_style1).place(
        relx=0.5, rely=0.8, anchor="center")


def menu():
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry('600x730')
    ctk.CTkLabel(root, text="Algoritmos de Relleno",
                 font=font_style2).pack()
    ctk.CTkLabel(root, text="Seleccione una opción:", font=font_style3).pack()

    # Marco para las dos columnas
    frame_columns = ctk.CTkFrame(root)
    frame_columns.pack(side="top", padx=10, pady=8, anchor="n")

    # Marco para el botón "Regresar a Presentación"
    frame_button = ctk.CTkFrame(root)
    frame_button.pack(side="top", padx=10, pady=10, anchor="n")

    # Columnas de los botones
    frame_column1 = ctk.CTkFrame(frame_columns)
    frame_column1.pack(side="left", padx=10, pady=10)

    frame_column2 = ctk.CTkFrame(frame_columns)
    frame_column2.pack(side="left", padx=10, pady=10)

    # Botones con imágenes
    # Cambiar ruta de imágenes
    image_dda = ctk.CTkImage(light_image=Image.open(
        "relleno\img\goku.png"), size=(200, 200))
    image_bren = ctk.CTkImage(light_image=Image.open(
        "relleno\img\maya_f.png"), size=(200, 200))
    image_circunferencia = ctk.CTkImage(light_image=Image.open(
        "relleno\img\maya_feliz.png"), size=(200, 200))
    image_elipse = ctk.CTkImage(light_image=Image.open(
        "relleno\img\goku.png"), size=(200, 200))

    ctk.CTkButton(frame_column1, text="DDA", font=font_style1,
                  image=image_dda, command=dda, compound="top").pack(padx=10, pady=10)
    ctk.CTkButton(frame_column1, text="CIRCUNFERENCIA", font=font_style1,
                  image=image_circunferencia, command=circunferencia, compound="top").pack(padx=10, pady=10)
    ctk.CTkButton(frame_column2, text="BRESENHAM", font=font_style1,
                  image=image_bren, command=bren, compound="top").pack(padx=10, pady=10)
    ctk.CTkButton(frame_column2, text="ELIPSE", font=font_style1,
                  image=image_elipse, command=elipse, compound="top").pack(padx=10, pady=10)

    # Botón "Regresar a Presentación" al marco del botón
    ctk.CTkButton(frame_button, text="Regresar a Presentación",
                  font=font_style1, command=presentacion).pack(padx=10, pady=12)


root = ctk.CTk()
root.geometry('565x700')
root.title("PROYECTO No.1")
root.configure(padx=30, pady=30)

presentacion()
root.mainloop()
