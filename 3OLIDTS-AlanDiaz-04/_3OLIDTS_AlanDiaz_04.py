import tkinter as tk

ventana=tk.Tk()
ventana.title("Conversor de temperatura")

label1= tk.Label(ventana, text= 'Frenheit')
label1.grid(row=0,column=0)

entry1= tk.Entry(ventana)
entry1.grid(row=0, column=1)

button1= tk.Button(ventana, text="Convertir a Celsius") #,comand=convertir_a_celsius)
button1.grid(row=0, column=2)

label2= tk.Label(ventana, text='Celsius')
label2.grid(row=1,column=0)

entry2= tk.Entry(ventana)
entry2.grid(row=1, column=1)

button2= tk.Button(ventana, text="Convertir a Farenheit")#,comand=convertir_a_farenheit)
button2.grid(row=1, column=2)

button3= tk.Button(ventana, text="Reestablecer")#,comand=borrar)
button3.grid(row=2, column=1)

ventana.geometry("520x480")

ventana.mainloop()
