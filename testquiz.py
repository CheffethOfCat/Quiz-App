import tkinter as tk

class FirstWindow(tk.Frame):
    def __init__(self, parent):
            super().__init(parent)
            tk.Label(self, text = "this is window 1").pack(padx = 10, pady = 10)
            self.pack(padx=10, pady=10)

class SecondWindow(tk.Frame):
    def __init__(self, parent):
            super().__init(parent)
            tk.Label(self, text = "this is window 1").pack(padx = 10, pady = 10)
            self.pack(padx=10, pady=10)

class MainWindow(tk.Frame):
    def __init__(self, master):
            mainframe=tk.Frame(master)
            mainframe.pack(padx=10, pady=10, fill='both', expand=1)
            self.index=0

            self.frameList=[FirstWindow(mainframe), SecondWindow(mainframe)]
            self.frameList[1].forget()
            
            bottomframe=tk.Frame(master)
            bottomframe.pack(padx=10, pady=10)

            switch=tk.Button(bottomframe, text = "switch", command=self.changeWindow)
            switch.pack(padx=10,pady=10)
    
    def changeWindow(self):
          self.frameList[self.index]. forget()
          self.index=(self.index + 1) % len(self.frameList)
          self.frameList[self.index].tkraise()
          self.frameList[self.index].pack(padx=10, pady=10)

root = tk.Tk()
window = MainWindow(root)
root.mainloop()