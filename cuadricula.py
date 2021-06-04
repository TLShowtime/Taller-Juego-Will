import tkinter as tk

ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Futoshiki v1")

listaBotones = []
cont = 0
dimension = 20
for i in range(3):
    for j in range(3):
        cont += 1
        listaBotones += [ tk.Button(ventana,text=str(cont),compound="c",height=10,width=20).grid(row=i,column=j) ] 



ventana.mainloop()
