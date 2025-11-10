from customtkinter import *

def open_main_window():
    win = CTk()
    win.title("Attendify")
    win.geometry("350x600")
    win.resizable(False,False)

    win.mainloop()
