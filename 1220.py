
# Kaip sukurti grafinę vartotojo sąsają (su Tkinter)

# from tkinter import Tk, Label
#
# langas = Tk()
# langas.geometry("250x200")
# uzrasas = Label(langas, text="Tiesiog tekstas")
# uzrasas.pack()
# langas.mainloop()

# from tkinter import Tk, Frame, Button, BOTTOM, LEFT, Y
#
# langas = Tk()
# langas.geometry("250x200")
# virsutinis = Frame(langas)
# apatinis = Frame(langas)
#
# mygtukas1 = Button(virsutinis, text="1 mygtukas")
# mygtukas2 = Button(virsutinis, text="2 mygtukas")
# mygtukas3 = Button(virsutinis, text="3 mygtukas")
# mygtukas4 = Button(apatinis, text="4 mygtukas")
#
# virsutinis.pack()
# apatinis.pack(side=BOTTOM)
# mygtukas1.pack(side=LEFT)
# mygtukas2.pack(side=LEFT)
# mygtukas3.pack(side=LEFT)
# mygtukas4.pack(side=BOTTOM, fill=Y)
#
# langas.mainloop()

# from tkinter import *
#
# langas = Tk()
#
# uzrasas1 = Label(langas, text="Vardas")
# laukas1 = Entry(langas)
# uzrasas2 = Label(langas, text="Pavardė")
# laukas2 = Entry(langas)
# varnele = Checkbutton(langas, text="Pažymėk varnelę")
#
# uzrasas1.grid(row=0, column=0, sticky=E)
# laukas1.grid(row=0, column=1)
# uzrasas2.grid(row=1, column=0, sticky=E)
# laukas2.grid(row=1, column=1)
# varnele.grid(row=2, columnspan=2)
#
# langas.mainloop()
#
# from tkinter import *
# langas = Tk()
# langas.geometry("200x300")
# def spausdinti():
#     print("Spausdina!")
#
# mygtukas = Button(langas, text="Spausdinti", command=spausdinti)
# mygtukas.pack()
# langas.mainloop()
#
# # Spausdina!

# from tkinter import *
# langas = Tk()
#
# def spausdinti(event):
#     print("Paspaustas kairys pelės mygtukas!")
#
# def spausdinti2(event):
#     print("Paspaustas dešinys pelės mygtukas!")
#
# def spausdinti3(event):
#     print("Paspaustas ENTER!")
#
# mygtukas = Button(langas, text="Spausdinti")
# mygtukas.bind("<Button-1>", spausdinti)
# mygtukas.bind("<Button-3>", spausdinti2)
# langas.bind("<Return>", spausdinti3)
# mygtukas.pack()
#
# langas.mainloop()

# Paspaustas kairys pelės mygtukas!
# Paspaustas dešinys pelės mygtukas!
# Paspaustas ENTER!

#
# from tkinter import *
#
# langas = Tk()
#
# def spausdinti():
#     ivesta = laukas1.get()
#     rezultatas["text"] = ivesta
#
# uzrasas1 = Label(langas, text="Įrašykite žodį")
# laukas1 = Entry(langas)
# mygtukas = Button(langas, text="Įvesti", command=spausdinti)
# rezultatas = Label(langas, text="")
#
# uzrasas1.grid(row=0, column=0)
# laukas1.grid(row=0, column=1)
# mygtukas.grid(row=0, column=2)
# rezultatas.grid(row=1, columnspan=3)
#
# langas.mainloop()
#
# from tkinter import *
#
# langas = Tk()
# boksas = Listbox(langas)
# sarasas = range(1, 200)
# boksas.insert(END, *sarasas)
# boksas.pack(side=LEFT)
# langas.mainloop()

# from tkinter import *
# langas = Tk()
# masyvas = range(1, 200)
# scrollbaras = Scrollbar(langas)
# boksas = Listbox(langas,
# yscrollcommand=scrollbaras.set)
# scrollbaras.config(command=boksas.yview)
# boksas.insert(END, *masyvas)
# scrollbaras.pack(side=RIGHT, fill=Y)
# boksas.pack(side=LEFT)
# langas.mainloop()
#
# from tkinter import *
#
# langas = Tk()
# sarasas = range(1, 200)
#
# def spausdinti():
#     pasirinkta = sarasas[boksas.curselection()[0]]
#     uzrasas["text"] = pasirinkta
#
# mygtukas = Button(langas, text="Spausdinti",
# command=spausdinti)
#
# uzrasas = Label(langas, text="Nieko")
# boksas = Listbox(langas, selectmode=SINGLE)
# boksas.insert(END, *sarasas)
# boksas.pack(side=LEFT)
# mygtukas.pack()
# uzrasas.pack()
# langas.mainloop()
#
# from tkinter import *
# langas = Tk()
#
# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)
#
# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")
# submeniu.add_command(label="Antras")
# langas.mainloop()
#
# from tkinter import *
# langas = Tk()
#
# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)
#
# def antras():
#     print("Antras!")
#
# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")
# submeniu.add_command(label="Antras",
# command=antras)
# langas.mainloop()
#
# # Antras!

# from tkinter import *
# langas = Tk()
#
# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)
# submeniu2 = Menu(meniu, tearoff = 0)
# submeniu3 = Menu(meniu, tearoff = 0)
#
# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")
#
# submeniu.add_command(label="Antras")
# submeniu.add_separator()
# submeniu.add_command(label="Trečias")
#
# meniu.add_cascade(label="Meniu 2",
# menu=submeniu2)
# submeniu2.add_command(label="1")
# submeniu2.add_command(label="2")
#
# meniu.add_cascade(label="Meniu 3",
# menu=submeniu3)
#
# langas.mainloop()


# NAMU DARBAI
# 1 uzduotis

# from tkinter import *
# langas = Tk()
# langas1 = StringVar()
#
#
# def spausdinti():
#     ivesta = laukas1.get()
#     rezultatas["text"] = "Labas, " + laukas1.get() + "!"
#     langas1.set((uzrasas1["text"]))
# def isvalyti():
#     rezultatas["text"] = ""
# def atkurti():
#     rezultatas["text"] = langas1.get()
# def iseiti():
#     langas.destroy()
#
# uzrasas1 = Label(langas, text="Įveskite vardą")
# laukas1 = Entry(langas)
# mygtukas = Button(langas, text="Patvirtinti", command=spausdinti)
# rezultatas = Label(langas, text="")
# langas.bind("<Return>", lambda  event: spausdinti())
#
#
# uzrasas1.grid(row=0, column=0)
# laukas1.grid(row=0, column=1)
# laukas1.focus()
# mygtukas.grid(row=0, column=2)
# rezultatas.grid(row=1, columnspan=3)
#
# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)
# meniu.add_cascade(label="Meniu", menu=submeniu)
#
# submeniu.add_command(label="Išvalyti", command= isvalyti)
# submeniu.add_command(label="Atkurti paskutinį", command= atkurti)
# submeniu.add_separator()
# submeniu.add_command(label="Išeiti", command= iseiti)
#
# langas.mainloop()
