from tkinter import*
from tkinter import messagebox
import tkinter as tk

window = tk.Tk()
window.geometry("1200x700")

def helloCallBack ():
    msg=messagebox.showinfo ("Hello Python", "Hello World.")
B = Button(window, text = "Hello", command = helloCallBack)
B.place(x=50,y=50)

window.mainloop()

#Comment