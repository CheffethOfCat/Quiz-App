from tkinter import*
from tkinter import messagebox
import tkinter as tk

window = tk.Tk()
window.geometry("1200x700")
#Choosing quiz window size

title_label = tk.Label(window, text="Welcome to My App", font=("Helvetica", 16))
title_label.pack(pady=10)

def helloCallBack ():
    msg=messagebox.showinfo ("Hello Python", "Hello World.")
B = Button(window, text = "Hello", command = helloCallBack)
B.place(x=600,y=350)
#Button testing

window.mainloop()

#Comment