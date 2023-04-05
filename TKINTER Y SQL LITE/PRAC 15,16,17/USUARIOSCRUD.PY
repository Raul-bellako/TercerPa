from tkinter import *
from tkinter import ttk
from tkinter import messagebox, Text
import tkinter as tk
from ControladorBD import *

# Instancia
c = ControladorBD()
# Funciones

def exeInsert():
    c.saveUser(Name.get(),Correo.get(),Contra.get(), )
def exeSelectUser():
    textBus.delete("0.0", "end")
    
    rsUser = c.consulUser(Busqueda.get())
    for user in rsUser:
        cadena = str(user[0])+" "+user[1]+" "+user[2]+" "+str(user[3])
    if(rsUser):
        textBus.insert("0.0",cadena)
    else:
        messagebox.showinfo("No encontrado","Usuario no existe en la Base de Datos")


"""def exeSelectAll():
    users = c.mostrarUsuarios()
    if users:
        for user in users:
            cadena = f'{user[0]} {user[1]} {user[2]} {user[3]}\n'
            textConsulta.insert(tk.END, cadena)
    else:
        messagebox.showinfo("Sin datos por mostrar","No se encontraron usuarios en la BD")"""

def exeSelectAll():
    # Eliminamos los datos previos del treeview
    tree.delete(*tree.get_children())
    users = c.mostrarUsuarios()
    if users:
        for user in users:
            cadena = (user[0], user[1], user[2], user[3])
            tree.insert('', tk.END, values=cadena)
    else:
        messagebox.showinfo("Sin datos por mostrar","No se encontraron usuarios en la BD")


def exeUpdate():    
    c.updateUser(id.get(), Name.get(), Correo.get(), Contra.get())
    messagebox.showinfo("Actualización de usuario", "Usuario actualizado exitosamente")

def exeDelete():
    result = messagebox.askquestion("Eliminar usuario", "¿Está seguro de que desea eliminar el usuario seleccionado?")
    if result == 'yes':
        c.deleteUser(id.get())
        messagebox.showinfo("Eliminación de usuario", "Usuario eliminado exitosamente")
        id.set('')
    else:
        return
    
w1 = Tk()
w1.title("CRUD de usuarios")
w1.geometry("640x480")

panel = ttk.Notebook(w1)
panel.pack(fill = 'both', expand = 'yes')

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

# Pestaña 1
titulo1 = Label(pestana1,text="Registro Usuarios",fg="#00CDFF",font=("Arial",28)).pack()

Name = tk.StringVar()
LBName = Label(pestana1,text="Nombre: ").pack()
ENName = Entry(pestana1,textvariable=Name).pack()

Correo = tk.StringVar()
LBCorreo = Label(pestana1,text="Correo: ").pack()
ENCorreo = Entry(pestana1,textvariable=Correo).pack()

Contra = tk.StringVar()
LBContra = Label(pestana1,text="Contraseña: ").pack()
ENContra = Entry(pestana1,textvariable=Contra).pack()

btnGuardar = Button(pestana1,text="Guardar Usuario",command=exeInsert).pack()

# Pestaña 2
titulo2 = Label(pestana2,text="Buscar usuario",fg="#11EC28",font=("Arial",28)).pack()

Busqueda = tk.StringVar()
LBid = Label(pestana2,text="Identificador de usuario").pack()
ENid = Entry(pestana2,textvariable=Busqueda).pack()

btnBusqueda = Button(pestana2,text="Click usuario",command=exeSelectUser).pack()

subBus = Label(pestana2,text="Registro",fg="#7511EC",font=("Arial",28)).pack()
textBus = Text(pestana2, height=5, width=75)
textBus.pack()

# Pestaña 3
titulo3 = Label(pestana3,text="Consultorio de usuarios",fg="#DAA520",font=("Arial",28)).pack()

btnConsultar = Button(pestana3,text="Click para consultar",command=exeSelectAll).pack()
subtConsulta = Label(pestana3,text="Usuarios registrados",fg="#ADFF2F",font=("Arial",28)).pack()

# Creamos el treeview
tree = ttk.Treeview(pestana3, columns=(1,2,3,4), show="headings", height=15)
tree.pack()

# Configuramos las columnas
tree.heading(1, text="ID")
tree.heading(2, text="Nombre")
tree.heading(3, text="Correo")
tree.heading(4, text="Contraseña")

# Definimos el tamaño de columnas
tree.column(1, width=50)
tree.column(2, width=200)
tree.column(3, width=200)
tree.column(4, width=200)

#Pestaña 4
titulo4 = Label(pestana4,text="Actualizar usuario",fg="#FF5733",font=("Arial",28)).pack()

LBidUpdate = Label(pestana4,text="Identificador de usuario: ").pack()
idUpdate = tk.StringVar()
ENidUpdate = Entry(pestana4,textvariable=idUpdate).pack()

newName = tk.StringVar()
LBnewName = Label(pestana4,text="Nuevo nombre: ").pack()
ENnewName = Entry(pestana4,textvariable=newName).pack()

newCorreo = tk.StringVar()
LBnewCorreo = Label(pestana4,text="Nuevo correo: ").pack()
ENnewCorreo = Entry(pestana4,textvariable=newCorreo).pack()

newContra = tk.StringVar()
LBnewContra = Label(pestana4,text="Nueva contraseña: ").pack()
ENnewContra = Entry(pestana4,textvariable=newContra).pack()

btnActualizar = Button(pestana4,text="Actualizar usuario",
command=lambda: [c.updateUser(idUpdate.get(), newName.get(), newCorreo.get(), newContra.get()),
messagebox.showinfo("Actualización", "El usuario ha sido actualizado correctamente")]).pack()

#Pestaña 5
titulo5 = Label(pestana5,text="Eliminar usuario",fg="#C70039",font=("Arial",28)).pack()

LBidDelete = Label(pestana5,text="Identificador de usuario: ").pack()
idDelete = tk.StringVar()
ENidDelete = Entry(pestana5,textvariable=idDelete).pack()

btnEliminar = Button(pestana5,text="Eliminar usuario",
command=lambda: [messagebox.askokcancel("Eliminar usuario", "¿Está seguro que desea eliminar este usuario?"),
c.deleteUser(idDelete.get()),

messagebox.showinfo("Eliminación", "El usuario ha sido eliminado correctamente")]).pack()






panel.add(pestana1, text = "Agregar Usuarios")
panel.add(pestana2, text = "Buscar Usuario")
panel.add(pestana3, text = "Consultar Usuarios")
panel.add(pestana4, text = "Actualizar Usuario")
panel.add(pestana5, text = "Eliminar Usuario")

w1.mainloop()