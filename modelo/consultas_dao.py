
from tkinter import messagebox
from .connecciondb import Conneccion

def crear_tabla():
    conn = Conneccion()

    sqlGenero = '''
        CREATE TABLE IF NOT EXISTS Genero(
            ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Nombre VARCHAR(50)
        );
    '''

    sqlMascota = '''
        CREATE TABLE IF NOT EXISTS Mascota(
            ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Nombre VARCHAR(150),
            Raza VARCHAR(50)
        );
    '''

    sqlVeterinaria = '''
        CREATE TABLE IF NOT EXISTS VeterinariaDB(
            ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Nombre VARCHAR(150),
            Edad INTEGER,
            GeneroID INTEGER,
            MascotaID INTEGER,
            Raza VARCHAR(50),
            dueño VARCHAR(50),
            FOREIGN KEY (GeneroID) REFERENCES Genero(ID),
            FOREIGN KEY (MascotaID) REFERENCES Mascota(ID)
        );
    '''

    try:
        cursor = conn.cursor
        cursor.execute(sqlGenero)
        cursor.execute(sqlMascota)
        cursor.execute(sqlVeterinaria)
        conn.cerrar_con()
        messagebox.showinfo('Base de datos', 'Base de datos conectada con éxito')
    except Exception as e:
        messagebox.showerror('Base de datos', f'Error al conectar la base de datos: {e}')


class Veterinaria:
    def __init__(self, dueño, nombre, edad, generoID, raza):
        self.dueño = dueño
        self.nombre = nombre
        self.edad = edad
        self.generoID = generoID
        self.raza = raza

    def __str__(self):
        return f'VeterinariaDB [{self.dueño},{self.nombre}, {self.edad}, {self.generoID}, {self.raza}]'


def guardar_datos(veterinaria):
    conn = Conneccion()

    try:
        sql_mascota = f'''
            INSERT INTO Mascota (Nombre, Raza)
            VALUES ('{veterinaria.nombre}', '{veterinaria.raza}');
        '''
        conn.cursor.execute(sql_mascota)
        mascota_id = conn.cursor.lastrowid

        sql_veterinaria = f'''
            INSERT INTO VeterinariaDB (MascotaID, dueño, Nombre, Edad, GeneroID, Raza)
            VALUES ({mascota_id}, '{veterinaria.nombre}', {veterinaria.edad}, {veterinaria.generoID}, '{veterinaria.raza}', '{veterinaria.dueño}');
        '''
        conn.cursor.execute(sql_veterinaria)

        conn.cerrar_con()
        messagebox.showinfo('Base de datos', 'Datos guardados con éxito')
    except Exception as e:
        conn.cerrar_con()
        messagebox.showerror('Base de datos', f'Error al guardar los datos: {e}')





def listar_datos():
    conn = Conneccion()
    listar_date = []

    sql = '''
            SELECT 
            v.ID,  
            v.Nombre AS veterinariaDB, 
            v.Edad,
            v.raza,
            v.GeneroID, 
            m.Nombre AS MascotaNombre
        FROM 
            VeterinariaDB AS v
        LEFT JOIN 
            Genero AS g ON v.GeneroID = g.ID
        LEFT JOIN 
            Mascota AS m ON v.MascotaID = m.ID

        

    '''        

    try:
        conn.cursor.execute(sql)
        listar_date = conn.cursor.fetchall()  
        conn.cerrar_con()
        return listar_date
    except Exception as e:
        messagebox.showerror('Base de datos', f'Error al listar los datos: {e}')


def listar_genero():
  conn = Conneccion()
  listar_generos = []

  sql = '''
      SELECT * FROM Genero
  '''

  try:
      conn.cursor.execute(sql)
      listar_generos =  conn.cursor.fetchall()  # Obtener solo el nombre
      conn.cerrar_con()
      return listar_generos

  except Exception as e:
      messagebox.showerror('Base de datos', f'Error al listar los generos: {e}')



def editar_datos(veterinaria, id):
    conn = Conneccion()

    sql= f'''

        UPDATE VeterinariaDB
        SET Nombre = '{veterinaria.nombre}',
            Edad = '{veterinaria.edad}',
            GeneroID = '{veterinaria.generoID}',
            Raza = '{veterinaria.raza}',
            dueño = '{veterinaria.dueño}'
        WHERE ID = '{id}'
    
'''
    try:
        cursor = conn.cursor
        cursor.execute(sql)
        conn.cerrar_con()
        messagebox.showinfo('Base de datos', 'Datos actualizados con éxito')
    except Exception as e:
        messagebox.showerror('Base de datos', f'Error al actualizar los datos: {e}')


def borrar_mascota(id):
    conn = Conneccion()

    sql= f'''

        DELETE FROM VeterinariaDB
        WHERE ID = {id}
    
'''
    sql2= f'''

        DELETE FROM Mascota
        WHERE ID = {id}

    '''

    try:
        cursor = conn.cursor
        cursor.execute(sql)
        cursor.execute(sql2)
        conn.cerrar_con()
        messagebox.showinfo('Base de datos', 'Datos actualizados con éxito')
    except Exception as e:
        messagebox.showerror('Base de datos', f'Error al actualizar los datos: {e}')                        