import tkinter as tk

ventana = tk.Tk()
ventana.resizable(0,0)
label = tk.Label(ventana,text="Hola, Soy Jesus Dominguez y estoy aprendiendo tkinter en OpenBootCamp")
opcion1 = tk.Checkbutton(ventana,text="Fundamentos de la Programación") 
opcion2 = tk.Checkbutton(ventana,text="HTML5/CSS3/JavaScript") 
opcion3 = tk.Checkbutton(ventana,text="Python") 
opcion4 = tk.Checkbutton(ventana,text="Java") 
opcion5 = tk.Checkbutton(ventana,text="Git") 

label.pack(anchor=tk.CENTER,ipadx=10,ipady=10)
opcion1.pack(anchor=tk.W,ipadx=10)
opcion2.pack(anchor=tk.W,ipadx=10)
opcion3.pack(anchor=tk.W,ipadx=10)
opcion4.pack(anchor=tk.W,ipadx=10)
opcion5.pack(anchor=tk.W,ipadx=10)

ventana.mainloop()
