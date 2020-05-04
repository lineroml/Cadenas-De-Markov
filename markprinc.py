from tkinter import *

#funciones de botones
def acepta():
    if kbut.get() is not "" and nbut.get() is not "":
        k = int(kbut.get())
        n = int(nbut.get()) 

#config de pantalla
window = Tk()
window.title("Markov")
window.geometry('950x720')
window.config(background='#BBC2E2')

#config de labels
titulo = Label(window, text="Cadenas de Markov", font=("Consolas", 20), background='#BBC2E2')
titulo.grid(column=2, row=1)
labl = Label(window, text="Inserte K:", font=("Consolas", 15), background='#BBC2E2')
lab2 = Label(window, text="Inserte N:", font=("Consolas", 15), background='#BBC2E2')
lab3 = Label(window, text="-------------", font=("Consolas", 15), background='#BBC2E2',fg="#D9FFF8")
lab4 = Label(window, text="-------------", font=("Consolas", 15), background='#BBC2E2',fg="#D9FFF8")
emptylabel =  Label(window, text="                   ", font=("Consolas", 15), background='#BBC2E2',fg="#D9FFF8")
emptylabel2 =  Label(window, text="   ", font=("Consolas", 15), background='#BBC2E2',fg="#D9FFF8")
lab5=  Label(window, text="     Presentado por:", font=("Consolas", 10), background='#BBC2E2',fg="#0A0908")
lab6=  Label(window, text="Luisa Escobar y Maria Duarte", font=("Consolas", 10), background='#BBC2E2',fg="#0A0908")
labl.grid(column=1, row=2)
lab2.grid(column=1, row=3)
lab3.grid(column=1, row=4)
lab4.grid(column=2,row=4)
lab5.grid(column=4,row=1)
lab6.grid(column=4,row=2)
emptylabel.grid(column=3,row=0)
emptylabel2.grid(column=0,row=0)

#textboxes para k y n
kbut = Entry(window,width=50)
kbut.grid(column=2,row=2)
nbut = Entry(window,width=50)
nbut.grid(column=2,row=3)

#botones
btn = Button(window, text="     Aceptar     ", bg="#D9FFF8", command=acepta)
btn.grid(column=1, row=5)
btn2 = Button(window, text='      Grafica      ', bg="#D9FFF8")
btn2.grid(column=2, row=5)
salir = Button(window, text="     salir     ", bg= "#D9FFF8")

#main
window.mainloop()
