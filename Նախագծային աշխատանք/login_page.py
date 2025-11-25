from tkinter import messagebox
from customtkinter import *
from PIL import Image
import main_page
import sign_up

root = CTk()
# root.iconbitmap("photos/photo.jpg")
root.geometry("350x600")
root.title("ClassLink")
root.resizable(False,False)
set_appearance_mode("Light")

# Labels
CTkLabel(master=root, text="Բարի Գալուստ ClassLink!", font=("Times", 15)).place(x=100, y=10)
CTkLabel(master=root, text="Գրանցվեք, որպեսզի մուտք գործեք ձեր հաշիվը", font=("Times", 15)).place(x=25, y=55)

# Username and password entries
CTkLabel(master=root, text="Username", text_color="grey", font=("Times", 13)).place(x=78, y=100)
username_entry = CTkEntry(master=root, corner_radius=16, border_color="#FFCC70", border_width=1, width=200,placeholder_text="Enter your username")
username_entry.place(x=75, y=125)

CTkLabel(master=root, text="Password", text_color="grey", font=("Times", 13)).place(x=78, y=230)
password_entry = CTkEntry(master=root, corner_radius=16, border_color="#FFCC70", border_width=1, width=200, show="•",placeholder_text="Enter your password")
password_entry.place(x=75, y=255)
# Login function
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Admin" and password == "12345678":
        # messagebox.showinfo("Success!", "You successfully logged in to your account!")
        root.destroy()
        main_page.open_main_window()
    else:
        messagebox.showerror("Error!", "Invalid username or password!")

def sign_Up():

    root.destroy()
    sign_up.open_sign_up_page()

# Buttons
CTkButton(master=root, text="Login!",command=login,width=200,corner_radius=16,hover_color="#2634ad").place(x=75, y=400)
CTkButton(master=root,text="Sign Up!",command=sign_Up,width=200,corner_radius=16,fg_color="#d3d7de",text_color="black",hover_color="#8f9194").place(x=75,y=450)


root.mainloop()

