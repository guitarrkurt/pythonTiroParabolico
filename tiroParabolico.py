#Descripcion: Solucion del tiro parabolico simple
 
#Librerias
from math import *        #funciones matematicas
from pylab import *   #graficar
from Tkinter import * #Ventana y Botones
 
#definimos la funcion del tiro parabolico, todo en terminos de x
def obtenerValores(f1, theta1, vx1, dt1, m1):
        #la funcion int(), convierte las cadenas de texto a valores enteros
        F               = int(f1)
        theta   = int(theta1)
        Vx      = int(vx1)
        Dt              = float(dt1)
        m               = int(m1)
        g       = 9.8
        #funcion que crea un intervalo que va de -1000 a 1000, con 100 puntos entre los dos
        import numpy as np
        x = np.linspace(-1000,1000,100)
        #dividimos la Y en primer, segundo y tercer termino, debido a su longitud
        primerTermino = ((F * sin(theta) * Dt) / m)
        segundoTermino = (x / (((F * cos(theta) * Dt) / m)  - Vx))
        tercerTermino = (0.5 * g) * (segundoTermino**2)
        y =  primerTermino * segundoTermino - tercerTermino
        #mandamos a graficar
        plot (x,y)
        show()
 
#Inicio de la ventana
ventana = Tk()
#tamano en pixeles de la ventana que sale al principio
ventana.geometry("400x300")
 
#Se declaran variables de tipo cadena de texto para la captura de los datos
textoEtiqueta1 = StringVar()
textoEtiqueta2 = StringVar()
textoEtiqueta3 = StringVar()
textoEtiqueta4 = StringVar()
textoEtiqueta5 = StringVar()
 
#Entry=caja de texto
E1 = Entry(ventana, textvar=textoEtiqueta1, bd =1)
#inset sirve para poner texto por default
E1.insert(0, "20")
E1.pack( side = BOTTOM )
#label=etiqueta que aparece al lado
#bottom significa que se coloque inmediatamente debajo del objeto anterior
L1 = Label(ventana, text="Fuerza:").pack( side = BOTTOM)
 
 
E2 = Entry(ventana, textvar=textoEtiqueta2, bd =1)
E2.insert(0, "30")
E2.pack( side = BOTTOM )
L2 = Label(ventana, text="Theta:").pack( side = BOTTOM)
 
 
 
E3 = Entry(ventana, textvar=textoEtiqueta3, bd =1)
E3.insert(0, "7")
E3.pack( side = BOTTOM )
L3 = Label(ventana, text="Vx:").pack( side = BOTTOM )
 
 
E4 = Entry(ventana, textvar=textoEtiqueta4, bd =1)
E4.insert(0, "0.01")
E4.pack( side = BOTTOM )
L4 = Label(ventana, text="Tiempo:").pack( side = BOTTOM )
 
 
E5 = Entry(ventana, textvar=textoEtiqueta5, bd =1)
E5.insert(0, "70")
E5.pack( side = BOTTOM )
L5 = Label(ventana, text="Pendiente m:").pack( side = BOTTOM )
 
#command ejecuta una funcion
#command con lambda ejecuta una funcion con parametros
myButton = Button(ventana, text="Enviar", command = lambda: obtenerValores(textoEtiqueta1.get(), textoEtiqueta2.get(),
                                                                                                                                                        textoEtiqueta3.get(), textoEtiqueta4.get(), textoEtiqueta5.get()))
#la funcion .get() de la variable de texto, obtiene el valor que contiene, y lo pasa como parametro
myButton.pack()
ventana.mainloop()
#fin de la ventana
