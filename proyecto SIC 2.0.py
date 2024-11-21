import tkinter as tk
import pandas as pd
from tkinter import messagebox

try:
    usuarios = pd.read_csv('usuarios.csv')
except Exception as e:
    usuarios = pd.DataFrame(columns=["Nombre del cliente", "I.D.", "Ocupación", 
                                      "Ingreso Mensual", "Meta de Ahorro", "User", 
                                      "Correo", "Contraseña", "Balance"])

try:
    balance_df = pd.read_csv('gastos.csv')
except Exception as e:
    balance_df = pd.DataFrame(columns=["Tipo", "I.D.", "Fecha", "Categoría", "Monto", "Descripción"])

def func_iniciarSesion():
    global usuarios

    def func_menuSesionIniciada(usuario):
        global usuarios

        for widget in windowsmain.winfo_children():
            widget.destroy()

        etiqueta_menuSesionIniciada_bienvenida = tk.Label(windowsmain, text=f'Bienvenido {usuario}', font=('Arial', 24))
        etiqueta_menuSesionIniciada_bienvenida.pack()


    def func_autenticacion():
        global usuarios

        usuario = entradas[0].get()  # Obtener el texto de la primera entrada (Nombre de usuario)
        contraseña = entradas[1].get()  # Obtener el texto de la segunda entrada (Contraseña)

        # Buscar el usuario en el DataFrame
        try:
            if usuario in usuarios['Nombre de usuario'].values:
                index = usuarios.loc[usuarios['Nombre de usuario'] == usuario].index[0]

                if contraseña == usuarios.loc[index, 'Contraseña']:
                    func_menuSesionIniciada(usuario)
                else:
                    # Mostrar mensaje de error si la contraseña es incorrecta
                    messagebox.showerror('Error', "Contraseña incorrecta")
            else:
                # Mostrar mensaje de error si el usuario no existe
                messagebox.showerror('Error', "Usuario no encontrado")
        except Exception as e:
            messagebox.showerror('Error', 'Cree un usuario y una contraseña primero')

        
    
    for widget in windowsmain.winfo_children():
        widget.destroy()
    
    etiqueta_iniciarSesion_bienvenida = tk.Label(windowsmain, text='Iniciar sesión', font=('Arial', 24))
    etiqueta_iniciarSesion_bienvenida.pack()

    etiquetas = [
        'Nombre',
        'Contraseña'
    ]

    entradas = []

    for etiqueta in etiquetas:
        label = tk.Label(windowsmain, text=etiqueta, font=('Arial', 16))
        label.pack()
        entry = tk.Entry(windowsmain, width=40, font=('Arial', 12))
        entry.pack()

        entradas.append(entry)
    
    boton_iniciarSesion_procesar = tk.Button(windowsmain, text='Iniciar sesión', command=func_autenticacion)
    boton_iniciarSesion_procesar.pack()

    boton_iniciarSesion_volver = tk.Button(windowsmain, text='Volver', command=func_menuPrincipal)
    boton_iniciarSesion_volver.pack()

# Definimos la función para registrarse
def func_registrarse():
    global usuarios
        # Función que se llama cuando el botón es presionado
    def cargar_datos():
        global usuarios
        
        cedula = entradas[1].get()

        # Obtener el valor de la cédula de identidad ingresado
        try:
            cedula_int = int(cedula)
        except ValueError:
            # Si la cédula no es un número válido, mostrar error
            messagebox.showerror('Error', 'La cédula de identidad debe ser un número entero válido.')
            return  # Salir de la función si la cédula no es válida
        # Obtener los datos de las entradas
        nuevo_usuario = {
            'Nombre del cliente': entradas[0].get(),
            'I.D.': cedula_int,
            'Ocupación': entradas[2].get(),
            'Ingreso mensual': entradas[3].get(),
            'Meta de ahorro': entradas[4].get(),
            'Nombre de usuario': entradas[5].get(),
            'Correo': entradas[6].get(),
            'Contraseña': entradas[7].get(),
            'Balance': 0.00
        }

        nuevo_usuario_df = pd.DataFrame([nuevo_usuario])
        usuarios = pd.concat([usuarios, nuevo_usuario_df], ignore_index=True)
        # Guardar los datos en un archivo CSV
        usuarios.to_csv("usuarios.csv", index=False)
        
        messagebox.showinfo('Registro exitoso', '¡Usuario registrado con éxito!')

    # Eliminar elementos previos en la ventana
    for widget in windowsmain.winfo_children():
        widget.destroy()
        
    # Mensaje de bienvenida
    etiqueta_registrarse_bienvenida = tk.Label(windowsmain, text='Registro de usuario nuevo', font=('Arial', 24))
    etiqueta_registrarse_bienvenida.pack()

    # Crear campos de entrada
    etiquetas = [
        'Nombre y apellido: ',
        'Cédula de identidad: ',
        'Ocupación laboral: ',
        'Ingreso mensual: ',
        'Meta de ahorro: ',
        'Nombre de usuario: ',
        'Correo electrónico: ',
        'Contraseña: '
    ]
    
    entradas = []
    for etiqueta in etiquetas:
        label = tk.Label(windowsmain, text=etiqueta, font=('Arial', 16))
        label.pack()
        entry = tk.Entry(windowsmain, width=40, font=('Arial', 12))
        entry.pack()
        entradas.append(entry)

    # Botón para enviar los datos
    boton_registrarse_enviarDatos = tk.Button(windowsmain, text='Cargar datos', command=cargar_datos)
    boton_registrarse_enviarDatos.pack()

    boton_registrarse_atras = tk.Button(windowsmain, text='Volver a atrás', command=func_menuPrincipal)
    boton_registrarse_atras.pack()

# Función para salir del programa
def func_salir():
    windowsmain.destroy()

# Función menú principal
def func_menuPrincipal():
    windowsmain.title('CachiChén')

    for widget in windowsmain.winfo_children():
        widget.destroy()

    etiqueta_menuPrincipal_bienvenida = tk.Label(windowsmain, text='Bienvenido/a a CachiChén', font=('Arial', 24))
    etiqueta_menuPrincipal_bienvenida.pack()
    
    boton_iniciarSesion = tk.Button(windowsmain, text='Iniciar sesión', command=func_iniciarSesion)
    boton_iniciarSesion.pack()

    boton_registrarse = tk.Button(windowsmain, text='Registrarse', command=func_registrarse)
    boton_registrarse.pack()

    boton_salir = tk.Button(windowsmain, text='Salir', command=func_salir)
    boton_salir.pack()

    

# Crear la ventana principal
windowsmain = tk.Tk()
windowsmain.geometry("1366x768")

func_menuPrincipal()

# Ejecutar la aplicación
windowsmain.mainloop()
