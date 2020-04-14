# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 13:26:29 2019

@author: Pacman
"""
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import  sys



def hacer_click():
    global num_cartas
    num_cartas = int(entry.get())
    #if num_cartas == 0 or num_cartas > 20:
    if num_cartas >= 2 and num_cartas<=20:
        ventana.destroy()
    else:
        messagebox.showinfo("Error", "El numero de cartas debe ser entre 2 y 20")


ventana = tk.Tk()
ventana.title ("--- Memorama ---")
ventana.geometry ("350x150+500+250")
Label(ventana, text = "Número de cartas entre 2 y 20:").pack()
entry = Entry(ventana,width=2)
button = Button(ventana, text="Aceptar",command= hacer_click)
button.place(x=50, y=100)
entry.pack()
ventana.mainloop()




class Carta:
    def __init__(self):
        self.valor = 0
        self.posicion = 0
        self.oculto = True  
        self.foto = tk.PhotoImage(file="fondo.gif")

class Memorama:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Memorama")
        self.ventana.geometry("710x520")
        self.botones = []
        self.cartas = []
        self.temporal = Carta()
        self.a = 0
        self.par = 0
        self.listo = True
        self.fondo = tk.PhotoImage(file="fondo.gif")
        self.crearTablero()
        self.revolver()
        self.ventana.mainloop()


    def crearTablero(self):

        contador = 0
        if num_cartas == 2:
            for i in range (2):
                for j in range(2):
                    btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                    btn.place(x=(j+1)*70,y=(i+1)*70)
                    self.botones.append(btn)
                    contador+=1
        else:
            if num_cartas == 3:
                for i in range (2):
                    for j in range(3):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1 
        if num_cartas == 4:
                for i in range (2):
                    for j in range(4):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
                        
        if num_cartas == 5:
            for i in range (3):
                for j in range(4):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
                        contador2 = len(self.botones)
                        if (contador2 >=9):
                            btn.place(x=(j+1)*135,y=(i+1)*72)
                            if (contador2 >=10):
                                btn.place(x=(j+1)*105,y=(i+1)*72)
                                break
        if num_cartas == 6:
                for i in range (3):
                    for j in range(4):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
            
        if num_cartas == 7:
            for i in range (4):
                for j in range(4):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
                        contador2 = len(self.botones)
                        if (contador2 >=13):
                            btn.place(x=(j+1)*135,y=(i+1)*72)
                            if (contador2 >=14):
                                btn.place(x=(j+1)*105,y=(i+1)*72)
                                break
        if num_cartas == 8:
                for i in range (4):
                    for j in range(4):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
        if num_cartas == 9:
                for i in range (3):
                    for j in range(6):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
        if num_cartas == 10:
                for i in range (4):
                    for j in range(5):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
        if num_cartas == 11:
            for i in range (4):
                for j in range(6):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
                        contador2 = len(self.botones)
                        if (contador2 >=19):
                            btn.place(x=(j+1)*135,y=(i+1)*71)
                            if (contador2 >=20):
                                btn.place(x=(j+1)*104,y=(i+1)*71)
                                if (contador2 >= 21):
                                    btn.place(x=(j + 1)*93, y=(i + 1) * 71)
                                    if (contador2 >= 22):
                                        btn.place(x=(j + 1)*88, y=(i + 1) * 71)
                                        break
        if num_cartas == 12:
            for i in range (4):
                    for j in range(6):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
        if num_cartas == 13:
            for i in range (5):
                for j in range(6):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
                        contador2 = len(self.botones)
                        if (contador2 >=25):
                            btn.place(x=(j+1)*285,y=(i+1)*71)
                            if (contador2 >=26):
                                btn.place(x=(j+1)*105,y=(i+1)*71)
                                break
        if num_cartas == 14:
            for i in range (4):
                    for j in range(7):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
        if num_cartas == 15:
            for i in range (5):
                    for j in range(6):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
        if num_cartas == 16:
            for i in range (6):
                for j in range(6):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
                        contador2 = len(self.botones)
                        if (contador2 >=31):
                            btn.place(x=(j+1)*285,y=(i+1)*71)
                            if (contador2 >=32):
                                btn.place(x=(j+1)*105,y=(i+1)*71)
                                break
        if num_cartas == 17:
            for i in range (6):
                for j in range(6):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
                        contador2 = len(self.botones)
                        if (contador2 >=31):
                            btn.place(x=(j+1)*137,y=(i+1)*71)
                            if (contador2 >=32):
                                btn.place(x=(j+1)*105,y=(i+1)*71)
                                if (contador2 >= 33):
                                    btn.place(x=(j + 1) * 93, y=(i + 1) * 71)
                                    if (contador2 >= 34):
                                        btn.place(x=(j + 1) * 88, y=(i + 1) * 71)
                                        break
        if num_cartas == 18:
            for i in range (6):
                    for j in range(6):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
        if num_cartas == 19:
            for i in range (6):
                for j in range(7):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1
                        contador2 = len(self.botones)
                        if (contador2 >=36):
                            btn.place(x=(j+1)*205,y=(i+1)*71)
                            if (contador2 >=37):
                                btn.place(x=(j+1)*139,y=(i+1)*71)
                                if (contador2 >= 38):
                                    btn.place(x=(j + 1) * 117, y=(i + 1) * 71)
                                    break

        if num_cartas == 20:
            for i in range (5):
                    for j in range(8):
                        btn = tk.Button(self.ventana,command=lambda a = contador:self.revisar(a), height=70,width=70,image=self.fondo)
                        btn.place(x=(j+1)*70,y=(i+1)*70)
                        self.botones.append(btn)
                        contador+=1

    def revolver(self):
        i = 1
        while (i<= num_cartas):
            carta1 = Carta()
            carta1.valor = i
            carta1.foto= tk.PhotoImage(file= str(i)+".gif")
            carta2 = Carta()
            carta2.valor = i
            carta2.foto = tk.PhotoImage(file = str(i)+".gif")
            self.cartas.append(carta1)
            self.cartas.append(carta2)
            i+=1

        cartasTemporal = []
        while len(self.cartas)>0:
            posicion = random.randrange(0,len(self.cartas))
            cartasTemporal.append(self.cartas.pop(posicion))
        self.cartas = cartasTemporal

    def revisar(self,a):
        if self.listo == True and self.cartas[a].oculto == True:
            self.botones[a].config(image=self.cartas[a].foto)
            if self.par == 0:
                self.temporal = self.cartas[a]
                self.cartas[a].oculto = False
                self.temporal.posicion = a
                self.par = 1
            elif self.par ==1:
                self.par= 0
                if self.temporal.valor == self.cartas[a].valor:
                    self.cartas[a].oculto = False
                    bandera = True
                    for elemento in self.cartas:
                        if elemento.oculto == True:
                            bandera = False
                            break
                    if bandera == True:
                            messagebox.showinfo("Ganaste","Felicidades, Ganaste" )
                else: 
                    self.a = a
                    self.listo = False
                    self.ventana.after(500,self.tapar)

    def tapar(self):
        self.cartas[self.temporal.posicion].oculto = True
        self.botones[self.temporal.posicion].config(image=self.fondo)
        self.botones[self.a].config(image=self.fondo)
        self.listo = True


obj = Memorama()