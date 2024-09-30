import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Ashly, eres especial")
ventana.geometry("600x500")  # Mantener la ventana más grande
ventana.configure(bg="#FFEBF0")

# Aumentar el tamaño del canvas para que el texto quepa mejor
canvas = tk.Canvas(ventana, width=500, height=300, bg="#FFEBF0", highlightthickness=0)
canvas.pack(pady=20)

pétalos = []

def dibujar_flor(paso):
    if paso == 1:
        pétalos.append(canvas.create_oval(220, 100, 280, 160, fill="yellow", outline=""))  # Centro
    elif paso == 2:
        pétalos.append(canvas.create_oval(190, 70, 250, 130, fill="pink", outline=""))  # Pétalo 1
    elif paso == 3:
        pétalos.append(canvas.create_oval(250, 70, 310, 130, fill="pink", outline=""))  # Pétalo 2
    elif paso == 4:
        pétalos.append(canvas.create_oval(190, 130, 250, 190, fill="pink", outline=""))  # Pétalo 3
    elif paso == 5:
        pétalos.append(canvas.create_oval(250, 130, 310, 190, fill="pink", outline=""))  # Pétalo 4
    elif paso == 6:
        # Ajustar la posición y el tamaño del texto para que quepa
        canvas.create_text(250, 260, text="Ashly, eres especial", font=("Helvetica", 26, "bold"), fill="#FF69B4")

    if paso < 6:
        ventana.after(500, lambda: dibujar_flor(paso + 1))

dibujar_flor(1)

def opcion_si():
    messagebox.showinfo("Respuesta", "¡Claro que lo eres! Eres muy especial para mí.")

def opcion_no():
    messagebox.showinfo("Respuesta", "¿Por qué elegiste que no? ¡Por supuesto que sí eres especial!")

# Ajustar la posición de los botones
boton_si = tk.Button(ventana, text="Sí", font=("Helvetica", 14), bg="#FFB6C1", fg="#4B0082", command=opcion_si)
boton_si.pack(side="left", padx=80, pady=20)

boton_no = tk.Button(ventana, text="No", font=("Helvetica", 14), bg="#FFB6C1", fg="#4B0082", command=opcion_no)
boton_no.pack(side="right", padx=80, pady=20)

ventana.mainloop()