import tkinter as tk

##ventana = tk.Tk()
##ventana.geometry("500x500")
##ventana.title("Futoshiki v1")
##
##listaBotones = []
##cont = 0
##dimension = 20
##for i in range(3):
##    for j in range(3):
##        cont += 1
##        listaBotones += [ tk.Button(ventana,text=str(cont),compound="c",height=10,width=20).grid(row=i,column=j) ] 
##
##ventana.mainloop()
root = tk.Tk()
root.geometry("500x500")
def key(event):
    print ("pressed", repr(event.char))

def callback(event):
    print ("clicked at", event.x, event.y)

canvas= tk.Canvas(root, width=500, height=500)
canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
lineas = []
for i in range(3):
    lineas += [ canvas.create_line(500//3*i,0,500//3*i,500)]
    lineas += [ canvas.create_line(0,500//3*i,500,500//3*i)]
canvas.pack()

root.mainloop()
