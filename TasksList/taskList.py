import tkinter as tk


def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)


def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista de tareas")

# Crear una entrada de texto para ingresar las tareas
entrada_tarea = tk.Entry(ventana)
entrada_tarea.pack()

# Crear un boton para agregar tareas
boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack()

# Crear una lista para mostrar las tareas
lista_tareas = tk.Listbox(ventana)
lista_tareas.pack()

# Crear un boton para eliminar la tarea seleccionada
boton_eliminar = tk.Button(ventana, text="Eliminar tarea", command=eliminar_tarea)
boton_eliminar.pack()

# ejecutar el bucle principal de la aplicacion
ventana.mainloop()
