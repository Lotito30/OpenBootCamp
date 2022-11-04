import tkinter as tk

ventana = tk.Tk()
ventana.geometry("250x270")
ventana.resizable(0,0)
seleccion = tk.IntVar()
def reiniciar():
    seleccion.set(0)
r1 = tk.Radiobutton(ventana,text="Opcion 1",value=1,variable=seleccion)
r2 = tk.Radiobutton(ventana,text="Opcion 2",value=2,variable=seleccion)
r3 = tk.Radiobutton(ventana,text="Opcion 3",value=3,variable=seleccion)
r4 = tk.Radiobutton(ventana,text="Opcion 4",value=4,variable=seleccion)
r5 = tk.Radiobutton(ventana,text="Opcion 5",value=5,variable=seleccion)
boton_reiniciar = tk.Button(ventana,text="Reiniciar",command=reiniciar)

r1.grid(column=0,row=0,padx=10,pady=10)
r2.grid(column=0,row=1,padx=10,pady=10)
r3.grid(column=0,row=2,padx=10,pady=10)
r4.grid(column=0,row=3,padx=10,pady=10)
r5.grid(column=0,row=4,padx=10,pady=10)
boton_reiniciar.grid(column=0,row=5,padx=10,pady=10)

ventana.mainloop()