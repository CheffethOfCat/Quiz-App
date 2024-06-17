from tkinter import*
from tkinter import messagebox
import tkinter as tk


window = tk.Tk()
window.geometry("1200x700")

#Choosing quiz window size

def New():
    new_window = tk.Toplevel(window)  # Creates a new top-level window
    new_window.geometry("600x400")
    new_window.title("New Window")
    label = tk.Label(new_window, text="This is the new window", font=("Helvetica", 12))
    label.pack(pady=20)

btn = Button(window, text = 'Click me!', command = New)
btn.place(x=600, y=350)

def Jew ():
    new_window = tk.Toplevel(window)
    new_window.geometry("500x500")
    new_window.title("Siiuuu")
    label = tk.Label(new_window, text= "wazzupppp", font=("Helvetica", 12))
    label.pack(pady=20)


siu = Button(window, text = 'Click you!', command = Jew)
siu.place(x=600, y=450)
#Previous button test

#Button opening another window for questions

title_label = tk.Label(window, text="Welcome to My App", font=("Helvetica", 16), 
                       fg = 'purple',
                       bg = 'black')
title_label.pack(pady=10)

#Adding TItle
#def helloCallBack ():
 #   msg=messagebox.showinfo ("Hello Python", "Hello World.")
#B = Button(window, text = "Hello", command = helloCallBack)
#B.place(x=600,y=350)

#Button testing

window.mainloop()

#Comment