import tkinter as tk


def borrar ():
    entry1.delete(0,tk.END)
    entry1.insert(0, "0.0")
    entry2.delete(0,tk.END)
    entry2.insert(0, "0.0")
    
def convertir_a_farenheit():
    celsius=float(entry2.get())
    farenheit=(celsius*9/5)+32
    entry1.delete(0,tk.END)
    entry1.insert(0,f"{farenheit:.2f}")
    
def convertir_a_celsius():
    farenheit=float(entry1.get())
    celsius=(farenheit-32)*5.0/9.0
    entry2.delete(0,tk.END)
    entry2.insert(0,f"{celsius:.2f}")



ventana=tk.Tk()
ventana.title("Conversor de temperatura")

label1= tk.Label(ventana, text= 'Frenheit')
label1.grid(row=0,column=0)

entry1= tk.Entry(ventana)
entry1.grid(row=0, column=1)

button1= tk.Button(ventana, text="Convertir a Celsius",command=convertir_a_celsius)
button1.grid(row=0, column=2)

label2= tk.Label(ventana, text='Celsius')
label2.grid(row=1,column=0)

entry2= tk.Entry(ventana)
entry2.grid(row=1, column=1)

button2= tk.Button(ventana, text="Convertir a Farenheit",command=convertir_a_farenheit)
button2.grid(row=1, column=2)

button3= tk.Button(ventana, text="Reestablecer",command=borrar)
button3.grid(row=2, column=1)

ventana.geometry("520x480")

ventana.mainloop()
