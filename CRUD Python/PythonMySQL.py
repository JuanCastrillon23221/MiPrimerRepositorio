import tkinter as tk

#Importar los modulos restantas de tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Clientes import *
from Conexion import *

class FormularioClientes:
    global textBoxId
    textBoxId = None
    
    global textBoxNombres
    textBoxNombres = None
    
    global textBoxApellidos
    textBoxApellidos = None
    
    global groupBox
    groupBox = None
    
    global tree
    tree = None
    
    global combo
    combo = None
    
    global base
    base = None
    
    
def Formulario():
    global textBoxNombres
    global textBoxApellidos
    global textBoxId
    global combo
    global base
    global groupBox
    global tree
    
    try:
        base = Tk()
        base.geometry("1200x300")
        base.title("Formulario Python")
        
        #pady y padx son espaciados entre los elementos
        groupBox = LabelFrame(base, text="Datos del Personal", padx=5, pady=5)
        groupBox.grid(row=0, column=0, padx=10, pady=10)
        
        labelId = Label(groupBox, text="Id:", width=13, font=("arial",12)).grid(row=0, column=0)
        textBoxId = Entry(groupBox)
        textBoxId.grid(row=0, column=1)
        
        labelNombres = Label(groupBox, text="Nombres:", width=13, font=("arial",12)).grid(row=1, column=0)
        textBoxNombres = Entry(groupBox)
        textBoxNombres.grid(row=1, column=1)
        
        labelApellidos = Label(groupBox, text="Apellidos:", width=13, font=("arial",12)).grid(row=2, column=0)
        textBoxApellidos = Entry(groupBox)
        textBoxApellidos.grid(row=2, column=1)
        
        labelSexo = Label(groupBox, text="Sexo:", width=13, font=("arial",12)).grid(row=3, column=0)
        #Crea un input de seleccion
        seleccionSexo = tk.StringVar()
        combo = ttk.Combobox(groupBox, values=["Masculino", "Femenino"], textvariable=seleccionSexo)
        combo.grid(row=3, column=1)
        #Establece por defecto el valor de "Masculino"
        seleccionSexo.set("Masculino")
        
        Button(groupBox, text="Guardar", width=10, command=guardarRegistros).grid(row=4, column=0)
        Button(groupBox, text="Modificar", width=10, command=modificarRegistros).grid(row=4, column=1)
        Button(groupBox, text="Eliminar", width=10, command=eliminarRegistros).grid(row=4, column=2)
        
        groupBox = LabelFrame(base, text="Lista del Personal", padx=5, pady=5,)
        groupBox.grid(row=0, column=1, padx=5, pady=5)
        #Crear un Treeview
        
        #Configurar las columnas
        tree = ttk.Treeview(groupBox, columns=("Id", "Nombres", "Apellidos", "Sexo"),show='headings', height=5,)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="Id")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Nombres")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Apellidos")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Sexo")
        
        #Agregar los datos a la tabla
        #Mostrar la tabla
        for row in CClientes.mostrarClientes():
            tree.insert("", "end", values=row)
        
        #ejecutar la funcion de hacer clock y mostrar el resultado en los Entry
        tree.bind("<<TreeviewSelect>>", seleccionarRegistro)    
        
        tree.pack()
        
        
        
        base.mainloop()
        
    except ValueError as error:
        print("Error al mostrar la interfaz, error:{}".format(error))
            
            
def guardarRegistros():
    
    global textBoxApellidos, textBoxNombres, combo, groupBox
    
    try:
        #Verificar si los widgets estan inicializados
        if textBoxNombres is None or textBoxApellidos is None or combo is None:
            print("Los widgets no estan inicializados")
            return
        
        nombres = textBoxNombres.get()
        apellidos = textBoxApellidos.get()
        sexo = combo.get()
        
        CClientes.ingresarClientes(nombres, apellidos, sexo)
        messagebox.showinfo("Informacion", "Los datos fueron guardados")
        
        actualizarTreeView()
        
        #Limpiamos los campos
        textBoxNombres.delete(0, END)
        textBoxApellidos.delete(0, END)
        
    except ValueError as error:
        print("Error al ingresar los datos {}".format(error))
        
def actualizarTreeView():
    global tree
    
    try:
        #Borrar todos los elementos actuales del TreeView
        #El heading son los padres y los registros los hijos
        tree.delete(*tree.get_children())
        #Obtener los nuevos datos que deseamos mostrar
        datos = CClientes.mostrarClientes()
        #Insertar los nuevos datos en el TreeView
        for row in CClientes.mostrarClientes():
            tree.insert("","end",values=row)
            
    except ValueError as error:
        print("Error al actualizar tabla {}".format(error))
        
def seleccionarRegistro(event):
    try:
        #Obtener el Id del elemento seleccionado
        itemSeleccionado = tree.focus()
        if itemSeleccionado:
            #obtener los valores por columna
            values = tree.item(itemSeleccionado)['values']
            #Estableces los valores en los widgets entry
            textBoxId.delete(0,END)
            textBoxId.insert(0,values[0])
            textBoxNombres.delete(0,END)
            textBoxNombres.insert(0,values[1])
            textBoxApellidos.delete(0,END)
            textBoxApellidos.insert(0,values[2])
            combo.set(values[3])
            
    except ValueError as error:
        print("Error al seleccionar registro {}".format(error))

def modificarRegistros():
    
    global textBoxId,textBoxApellidos, textBoxNombres, combo, groupBox
    
    try:
        #Verificar si los widgets estan inicializados
        if  textBoxId is None or textBoxNombres is None or textBoxApellidos is None or combo is None:
            print("Los widgets no estan inicializados")
            return
        
        idUsuario = textBoxId.get()
        nombres = textBoxNombres.get()
        apellidos = textBoxApellidos.get()
        sexo = combo.get()
        
        CClientes.modificarClientes(idUsuario, nombres, apellidos, sexo)
        messagebox.showinfo("Informacion", "Los datos fueron actualizados")
        
        actualizarTreeView()
        
        #Limpiamos los campos
        textBoxId.delete(0, END)
        textBoxNombres.delete(0, END)
        textBoxApellidos.delete(0, END)
        
    except ValueError as error:
        print("Error al modificar los datos {}".format(error)) 
        
def eliminarRegistros():
    
    global textBoxId, textBoxNombres, textBoxApellidos
    
    try:
        #Verificar si los widgets estan inicializados
        if  textBoxId is None:
            print("Los widgets no estan inicializados")
            return
        
        idUsuario = textBoxId.get()
        
        CClientes.eliminarClientes(idUsuario)
        messagebox.showinfo("Informacion", "Los datos fueron eliminados")
        
        actualizarTreeView()
        
        #Limpiamos los campos
        textBoxId.delete(0, END)
        textBoxNombres.delete(0, END)
        textBoxApellidos.delete(0, END)
        
    except ValueError as error:
        print("Error al eliminar los datos {}".format(error))           
            
Formulario()