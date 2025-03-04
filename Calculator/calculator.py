import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Calculator')
        self.config(width=280,height=420)
        self.resizable(False,False)

        self.result_var = tk.StringVar()

        self.display = tk.Entry(self, textvariable=self.result_var, font=('Arial',24),bd=10, relief='sunken', justify='right')
        self.display.place (x=20,y=20,width=240, height=60)

        buttons = [
            ('7', 20, 100), ('8', 80, 100), ('9', 140, 100), ('/', 200, 100),
            ('4', 20, 160), ('5', 80, 160), ('6', 140, 160), ('*', 200, 160),
            ('1', 20, 220), ('2', 80, 220), ('3', 140, 220), ('-', 200, 220),
            ('0', 20, 280), ('.', 80, 280), ('=', 140, 280), ('+', 200, 280),
        ]

        for(text,x,y) in buttons:
            self.create_button(text,x,y)

        self.create_button('C',20,340,width=240)

    def create_button(self,text,x,y,width=60,height=60):
        button = tk.Button(self, text=text, font=('Arial', 18), width=4, height=2,
        command= lambda: self.on_button_click(text))
        button.place(x=x,y=y,width=width, height=height)

    def on_button_click(self,text):
        current = self.result_var.get()

        if text == 'C':
            self.result_var.set('')
        elif text == '=':
            try:
                result = str(eval(current)) #result_var takes only string, but we need the content to be treated as a math operation
                self.result_var.set(result) # so eval will perform the math operation, and then str() converts the result into a string
            except ZeroDivisionError:
                messagebox.showerror('Invalid operation','Cannot divide a number by zero!')
            except Exception as e:
                messagebox.showerror('unexpected error',f'its a unexpected error:{str(e)}')
                self.result_var.set('0')
        else:
            self.result_var.set(current + text)

if __name__=='__main__':
 app = Calculator()
 app.mainloop()
