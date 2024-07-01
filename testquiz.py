import tkinter as tk  # Python 3
from tkinter import font as tkfont  # Python 3

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, FirstWindow, JewWindow):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.winfo_toplevel().geometry("600x400")
        frame.tkraise()

    def open_new_window(self, title, text, width=600, height=400):
        '''Helper function to open a new top-level window with given title and text'''
        new_window = tk.Toplevel(self)
        new_window.geometry(f"{width}x{height}")
        new_window.title(title)
        label = tk.Label(new_window, text=text, font=("Helvetica", 12))
        label.pack(pady=20)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Go to First Window",
                            command=lambda: controller.show_frame("FirstWindow"))
        button4 = tk.Button(self, text="Go to Second Window (Siiuuu)",
                            command=lambda: controller.show_frame("JewWindow"))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class FirstWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="This is the First Window", font=controller.title_font)
        label.pack(pady=20)

        # Button to open a new top-level window
        btn = tk.Button(self, text='Click me!', command=self.open_new_window)
        btn.pack(pady=10)

        back_btn = tk.Button(self, text="Back to Start",
                             command=lambda: controller.show_frame("StartPage"))
        back_btn.pack(pady=10)

    def open_new_window(self):
        self.controller.open_new_window("New Window", "This is the new window")


class JewWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="This is the Second Window (Siiuuu)", font=controller.title_font)
        label.pack(pady=20)

        back_btn = tk.Button(self, text="Back to Start",
                             command=lambda: controller.show_frame("StartPage"))
        back_btn.pack(pady=10)

        # Open a specific new window
        siu_btn = tk.Button(self, text='Click you!', command=self.open_new_window)
        siu_btn.pack(pady=10)

    def open_new_window(self):
        self.controller.open_new_window("Siiuuu", "Wazzupppp", 500, 500)


if __name__ == "__main__":
    app = SampleApp()
    app.geometry("1200x700")
    app.mainloop()