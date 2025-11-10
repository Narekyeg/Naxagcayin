from tkinter import messagebox
from customtkinter import *
from PIL import Image
import main_page

root = CTk()
root.iconbitmap("Apple_logo.png")
root.geometry("350x600")
root.title("Attendify")
root.resizable(False,False)


img=Image.open("Apple_logo.png")
img1=Image.open("google_logo.png")
img2=Image.open("email_symbol.png")
# Labels
CTkLabel(master=root, text="Բարի Գալուստ Attendify!", font=("Times", 15)).place(x=100, y=10)
CTkLabel(master=root, text="Գրանցվեք, որպեսզի մուտք գործեք ձեր հաշիվը", font=("Times", 15)).place(x=25, y=55)

# Username and password entries
CTkLabel(master=root, text="Username", text_color="grey", font=("Times", 13)).place(x=78, y=100)
username_entry = CTkEntry(master=root, corner_radius=16, border_color="#FFCC70", border_width=1, width=200)
username_entry.place(x=75, y=125)

CTkLabel(master=root, text="Password", text_color="grey", font=("Times", 13)).place(x=78, y=200)
password_entry = CTkEntry(master=root, corner_radius=16, border_color="#FFCC70", border_width=1, width=200, show="•")
password_entry.place(x=75, y=225)

# Login function
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "Admin" and password == "password":
        # messagebox.showinfo("Success!", "You successfully logged in to your account!")
        root.destroy()
        main_page.open_main_window()
    else:
        messagebox.showerror("Error!", "Invalid username or password!")


# Buttons
CTkButton(master=root, text="Login!",command=login,width=200,corner_radius=16,hover_color="#2634ad").place(x=75, y=300)
CTkButton(master=root,text="Continue with Apple",width=200,corner_radius=16, image=CTkImage(dark_image=img,light_image=img),fg_color="#000000",hover_color="grey").place(x=75,y=340)
CTkButton(master=root,text="Continue with Google",width=200,corner_radius=16, image=CTkImage(dark_image=img1,light_image=img1),fg_color="#ffffff",hover_color="#d6d6d4",text_color="#000000").place(x=75,y=380)
CTkButton(master=root,text="Continue with E-mail",width=200,corner_radius=16, image=CTkImage(dark_image=img2,light_image=img2),fg_color="#ff0000",hover_color="#9e0303").place(x=75,y=420)


root.mainloop()