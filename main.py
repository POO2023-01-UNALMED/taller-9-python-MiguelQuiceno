from tkinter import Tk, Button, Entry

# Configuración de la ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("290x285")

# Configuración de la pantalla de salida 
pantalla = Entry(root, width=19, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4,rowspan=1, padx=1, pady=1)

# Configuración de los botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_1.grid(row=1, column=0, padx=1, pady=1)

boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_2.grid(row=1, column=1, padx=1, pady=1)

boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_3.grid(row=1, column=2, padx=1, pady=1)

boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_4.grid(row=2, column=0, padx=1, pady=1)

boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_5.grid(row=2, column=1, padx=1, pady=1)

boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_6.grid(row=2, column=2, padx=1, pady=1)

boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_7.grid(row=3, column=0, padx=1, pady=1)

boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_8.grid(row=3, column=1, padx=1, pady=1)

boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2")
boton_9.grid(row=3, column=2, padx=1, pady=1)

boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2")
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0)
boton_punto.grid(row=4, column=2, padx=1, pady=1)

boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_mas.grid(row=1, column=3, padx=1, pady=1)

boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_menos.grid(row=2, column=3, padx=1, pady=1)

boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)

boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2")
boton_division.grid(row=4, column=3, padx=1, pady=1)

boton_1.bind("<Button-1>", lambda e: escribir("1"))
boton_2.bind("<Button-1>", lambda e: escribir("2"))
boton_3.bind("<Button-1>", lambda e: escribir("3"))
boton_4.bind("<Button-1>", lambda e: escribir("4"))
boton_5.bind("<Button-1>", lambda e: escribir("5"))
boton_6.bind("<Button-1>", lambda e: escribir("6"))
boton_7.bind("<Button-1>", lambda e: escribir("7"))
boton_8.bind("<Button-1>", lambda e: escribir("8"))
boton_9.bind("<Button-1>", lambda e: escribir("9"))

boton_punto.bind("<Button-1>", lambda e: escribir("."))
boton_mas.bind("<Button-1>", lambda e: escribir("+"))
boton_menos.bind("<Button-1>", lambda e: escribir("-"))
boton_multiplicacion.bind("<Button-1>", lambda e: escribir("*"))
boton_division.bind("<Button-1>", lambda e: escribir("/"))
boton_igual.bind("<Button-1>", lambda e: igualar())

#Eventos
def escribir(num):
    s=""
    s = pantalla.get()+num
    pantalla.delete(0, len(pantalla.get()) + 1 )
    pantalla.insert(0, s)
    

def calcular(s):
    if "+" in s:
        s = s.split("+")
        return float(s[0]) + float(s[1])from tkinter import Tk, Button, Entry
2
​
3
# Configuración ventana principal
4
root = Tk()
5
root.title(***)
6
root.resizable(0,0)
7
root.geometry(***)
8
​
9
# Configuración pantalla de salida 
10
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
11
pantalla.grid(row=0, column=0, columnspan=***, padx=1, pady=***)
12
​
13
# Configuración botones
14
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=***, padx=1, pady=***)
15
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=***, column=***, padx=***, pady=1)
16
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=***, padx=***, pady=1)
17
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=***, column=***, padx=1, pady=***)
18
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=***, column=1, padx=***, pady=***)
19
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=***, padx=***, pady=1)
20
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=***, column=***, padx=1, pady=***)
21
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=***, column=***, padx=1, pady=1)
22
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=***, pady=***)
23
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=***, columnspan=***, padx=1, pady=1)
24
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=***, column=***, padx=1, pady=1)
25
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=***, padx=***, pady=1)
26
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=***, column=3, padx=1, pady=1)
27
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=***, column=***, padx=1, pady=1)
28
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=***, column=***, padx=1, pady=***)
29
​
30
root.mainloop()
    elif "-" in s:
        s = s.split("-")
        return float(s[0]) - float(s[1])
    elif "*" in s:
        s = s.split("*")
        return float(s[0]) * float(s[1])
    elif "/" in s:
        s = s.split("/")
        return float(s[0]) / float(s[1])
    else:
        raise Exception("Operación no válida")
    

def igualar():
    escribir(" = "+ str( round(calcular( pantalla.get() ), 2) )  )
    
root.mainloop()
