import tkinter as tk
from tkinter import ttk
from modelo.consultas_dao import Veterinaria, crear_tabla, editar_datos, guardar_datos, listar_datos,listar_genero, borrar_mascota

class Frame(tk.Frame):  
    def __init__(self, root = None):    
        super().__init__(root,width=600,height=1000)    
        self.root = root
        self.id_Mascota = None   
        self.pack()    
        #self.config(bg='green')

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.bloquear_campos()
        self.mostrar_tabla()
        
    

    def label_form(self):    
        #self.label_nombre = tk.Label(self, text="Mascota: ")    
        #self.label_nombre.config(font=('Arial',12,'bold'))    
        #self.label_nombre.grid(row= 0, column=0,padx=10,pady=10)
        self.label_nombre = tk.Label(self, text="Dueño: ")    
        self.label_nombre.config(font=('Arial',12,'bold'))    
        self.label_nombre.grid(row= 0, column=0,padx=10,pady=10)
        self.label_nombre = tk.Label(self, text="Nombre: ")    
        self.label_nombre.config(font=('Arial',12,'bold'))    
        self.label_nombre.grid(row= 1, column=0,padx=10,pady=10)
        self.label_nombre = tk.Label(self, text="Edad: ")    
        self.label_nombre.config(font=('Arial',12,'bold'))    
        self.label_nombre.grid(row= 2, column=0,padx=10,pady=10)    
        self.label_nombre = tk.Label(self, text="Genero: ")    
        self.label_nombre.config(font=('Arial',12,'bold'))    
        self.label_nombre.grid(row= 3, column=0,padx=10,pady=10)
        self.label_nombre = tk.Label(self, text="Raza: ")    
        self.label_nombre.config(font=('Arial',12,'bold'))    
        self.label_nombre.grid(row= 4, column=0,padx=10,pady=10)
        
    
    def input_form(self):
        #self.mascota = tk.StringVar()    
        #self.entry_mascota = tk.Entry(self, textvariable=self.mascota)    
        #self.entry_mascota.config(width=50)    
        #self.entry_mascota.grid(row= 0, column=2,padx=10,pady=10)    

        self.nombre = tk.StringVar()    
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)    
        self.entry_nombre.config(width=50)    
        self.entry_nombre.grid(row= 1, column=2,padx=10,pady=10) 

        self.dueño = tk.StringVar()    
        self.entry_dueño = tk.Entry(self, textvariable=self.dueño)    
        self.entry_dueño.config(width=50)    
        self.entry_dueño.grid(row= 0, column=2,padx=10,pady=10)   
        
        self.edad = tk.StringVar()
        self.entry_edad = tk.Entry(self, textvariable=self.edad)    
        self.entry_edad.config(width=50)    
        self.entry_edad.grid(row= 2, column=2,padx=10,pady=10) 
        
        x = listar_genero()
        y = []
        for i in x:
            y.append(i[1])
    

        self.generos = ['Selecione Uno'] + y
        self.entry_genero = ttk.Combobox(self, state="readonly")
        self.entry_genero['values'] = self.generos
        self.entry_genero.current(0)
        self.entry_genero.config(width=25)    
        self.entry_genero.bind("<<ComboboxSelected>>")    
        self.entry_genero.grid(row= 3, column=2,padx=10,pady=10)

        self.raza = tk.StringVar()
        self.entry_raza = tk.Entry(self, textvariable=self.raza)    
        self.entry_raza.config(width=50)    
        self.entry_raza.grid(row= 4, column=2,padx=10,pady=10) 
    
    def botones_principales(self):    
        self.btn_alta = tk.Button(self, text='Nuevo', command= self.habilitar_campos)    
        self.btn_alta.config(width= 25,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')    
        self.btn_alta.grid(row= 5, column=0,padx=10,pady=10)    
        
        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_Campos)    
        self.btn_modi.config(width= 25,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#0D2A83',cursor='hand2',activebackground='#7594F5',activeforeground='#000000')    
        self.btn_modi.grid(row= 5, column=1,padx=10,pady=10)    
        
        self.btn_cance = tk.Button(self, text='Cancelar', command=self.bloquear_campos)    
        self.btn_cance.config(width= 25,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')    
        self.btn_cance.grid(row= 5, column=2,padx=10,pady=10)
    
    def guardar_Campos(self):
        veterinaria = Veterinaria(
            #self.mascota.get(),
            self.nombre.get(),
            self.dueño.get(),
            self.edad.get(),
            self.entry_genero.current(),
            self.raza.get()
        )

        if self.id_Mascota is None:
            guardar_datos(veterinaria)
        else:
            editar_datos(veterinaria, int(self.id_Mascota))


        self.bloquear_campos()
        self.mostrar_tabla()
        


    
        
    def habilitar_campos(self):
        #self.entry_mascota.config(state='normal')    
        self.entry_nombre.config(state='normal')
        self.entry_dueño.config(state='normal')    
        self.entry_edad.config(state='normal')    
        self.entry_genero.config(state='normal')
        self.entry_raza.config(state='normal')    
        self.btn_modi.config(state='normal')    
        self.btn_cance.config(state='normal')    
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        #self.entry_mascota.config(state='disabled')    
        self.entry_nombre.config(state='disabled')
        self.entry_dueño.config(state='disabled')    
        self.entry_edad.config(state='disabled')    
        self.entry_genero.config(state='disabled')
        self.entry_raza.config(state='disabled')    
        self.btn_modi.config(state='disabled')    
        self.btn_cance.config(state='disabled')    
        self.btn_alta.config(state='normal')
        #self.mascota.set('')
        self.nombre.set('')
        self.dueño.set('')
        self.edad.set('')
        self.entry_genero.current(0)
        self.raza.set('')
        self.id_Mascota = None
    
    def mostrar_tabla(self):

        self.listar_date = listar_datos()   
        self.listar_date.reverse()

        self.tabla = ttk.Treeview(self, columns=('Dueño','Nombre','Edad','Genero','Raza'))
        self.tabla.grid(row=7,column=0,columnspan=7, sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command= self.tabla.yview)
        self.scroll.grid(row=7,column=7, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Dueño')
        self.tabla.heading('#2', text='Nombre')
        self.tabla.heading('#3', text='Edad')
        self.tabla.heading('#4', text='Genero')
        self.tabla.heading('#5', text='Raza')

        for d in self.listar_date:
            self.tabla.insert('', 0, text=d[0], values=(d[5], d[3], d[1], d[2], d[4],))
            
        
        

        self.btn_editar = tk.Button(self, text='Editar', command= self.editar_datos)    
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')    
        self.btn_editar.grid(row= 10, column=0,padx=10,pady=10)    
        
        self.btn_delete = tk.Button(self, text='Delete', command= self.eliminar_datos)    
        self.btn_delete.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')    
        self.btn_delete.grid(row= 10, column=1,padx=10,pady=10)  
    
    def editar_datos(self):
    

        self.id_Mascota = self.tabla.item(self.tabla.selection())['text']

    
        selected_genre = self.tabla.item(self.tabla.selection())['values'][3]

   
        for i, genre in enumerate(self.generos):
            if genre == selected_genre:
                self.entry_genero.current(i)
                break
        else:
            self.entry_genero.current(0)

    
        #self.mascota.set(self.tabla.item(self.tabla.selection())['values'][0])
        self.nombre.set(self.tabla.item(self.tabla.selection())['values'][1])
        self.dueño.set(self.tabla.item(self.tabla.selection())['values'][0])
        self.edad.set(self.tabla.item(self.tabla.selection())['values'][2])
        self.raza.set(self.tabla.item(self.tabla.selection())['values'][4])  
        

        self.habilitar_campos()
      

    def eliminar_datos(self):

        self.id_Mascota = self.tabla.item(self.tabla.selection())['text']

        borrar_mascota(int(self.id_Mascota)) 
        self.mostrar_tabla()    

def barrita_menu(root):  
    barra = tk.Menu(root)
    root.config(menu = barra, width = 300 , height = 300)
    menu_inicio = tk.Menu(barra, tearoff=0)
    menu_inicio2 = tk.Menu(barra, tearoff=0)

    # niveles 
    # #principal
    barra.add_cascade(label='Inicio', menu = menu_inicio) 
    barra.add_cascade(label='Consultas', menu = menu_inicio)  
    barra.add_cascade(label='Acerca de..', menu = menu_inicio)  
    barra.add_cascade(label='Ayuda', menu= menu_inicio2)  
    
    #submenu 
    menu_inicio.add_command(label='Conectar DB', command= crear_tabla)  
    menu_inicio.add_command(label='Desconectar DB')  
    menu_inicio.add_command(label='Salir', command= root.destroy)

    #submenu ayuda
    menu_inicio2.add_command()  
    menu_inicio2.add_command()  
    menu_inicio2.add_command()