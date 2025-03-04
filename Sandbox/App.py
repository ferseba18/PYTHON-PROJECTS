import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def hello():
    message = box.get()
    greet.config(text=message)

messagebox.showinfo(title='Informaation',message='This is only information')
messagebox.showwarning(title='Warning',message='This is only a warning')
messagebox.showerror(title='Error',message='You screwed up')

window = tk.Tk()
#initialize the window of the app
window.title('Window 123456')
window.config(width=300, height=300)

label = ttk.Label(text= 'Input your greeting')
label.place(x=10,y=10)

box = ttk.Entry()
box.place(x=10,y=40)

button = ttk.Button(text = 'Greet',command=hello)
button.place(x=10,y=70, width=100, height=25)

dropdown_list = ttk.Combobox(values=['Potatoes','Pumpkin','Pears'])
dropdown_list.place(x=10,y=100)

checkbox = ttk.Checkbutton(text='Checking...')
checkbox.place(x=10,y=140)

greet = ttk.Label(text='')
greet.place(x=10,y=200)

window.mainloop()
#keeps the window open

