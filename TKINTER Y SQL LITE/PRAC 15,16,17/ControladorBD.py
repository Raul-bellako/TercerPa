from tkinter import messagebox
import sqlite3
import bcrypt

class ControladorBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/12103/Documents/GitHub/TercerPa/TKINTER Y SQL LITE/PRAC 15,16,17/DB Usuarioos.db")
            print("Conectando a la base de datos")
            return conexion
        except sqlite3.OperationalError:
            print("No pudo hacerse la conexion")
    
    def encripPass(self,contra):
        # 1 Contraseña
        conPlana = contra
        conPlana = conPlana.encode()
        sal = bcrypt.gensalt()
        
        conHa = bcrypt.hashpw(conPlana,sal)
        print(conHa)
        
        return conHa
    
    def saveUser(self,name,email,contra):
        # Llamamos metodo conexión
        conx = self.conexionBD()
        
        # Aqui si no esta completo sale el mensaje
        if (name == "" or email == "" or contra == "") :
            messagebox.showwarning("Cuidado","Formulario incompleto")
            conx.close()
        else:
            #Realizar insert a BD
            cursor = conx.cursor()
            conH = self.encripPass(contra)
            datos = (name,email,conH)
            SaveInSql = "insert into tbRegistrados(nombre,correo,contra) values(?,?,?)"
            
            # Ejecutar insert
            cursor.execute(SaveInSql,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Realizado","Usuario Guardado")
    
    def consulUser(self,id):
        # Realizar la conexion a la BD
        conx = self.conexionBD()
        if id ==  '':
            messagebox.showwarning("Advertencia","Campo vacío")
            conx.close()
        else:
            
            try:
                cursor = conx.cursor()
                sqlSelect = " select * from tbRegistrados where id = "+id
                
                cursor.execute(sqlSelect)
                RSuser = cursor.fetchall()
                conx.close()
                return RSuser
                
            except sqlite3.OperationalError:
                print("Error de consulta")
    
    
    def updateUser(self, id, name, email, contra):
        # Realizar la conexion a la BD
        conx = self.conexionBD()
        if id ==  '':
            messagebox.showwarning("Advertencia","Campo ID vacío")
            conx.close()
        else:
            try:
                cursor = conx.cursor()
                sqlUpdate = "UPDATE tbRegistrados SET nombre = ?, correo = ?, contra = ? WHERE id = ?"
                contraH = self.encripPass(contra)
                data = (name, email, contraH, id)
                cursor.execute(sqlUpdate, data)
                conx.commit()
                conx.close()
            except sqlite3.OperationalError:
                print("Error de consulta")  
                
    def deleteUser(self, id):
    # Realizar la conexion a la BD
     conx = self.conexionBD()
     cursor = conx.cursor()
     sqlDelete = "delete from tbRegistrados where id = ?"

    # Eliminar usuario
     try:
        cursor.execute(sqlDelete, (id,))
        conx.commit()
        conx.close()
     except sqlite3.Error as error:
        print("Error al eliminar usuario: ", error)
     else:
        print("Usuario eliminado exitosamente")

  
    
    def mostrarUsuarios(self):
        # Creamos la conexión 
        conx = self.conexionBD()
        cursor = conx.cursor()
        SQLSelectAll = "select * from tbRegistrados"
        
        # Obtenemos todos los usuarios 
        cursor.execute(SQLSelectAll)
        usuarios = cursor.fetchall()

        # Cerramos la conexion con la db
        conx.close()
        
        return usuarios
    

