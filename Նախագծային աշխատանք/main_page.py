from customtkinter import *

def open_main_window():
    win = CTk()
    win.title("Attendify")
    win.geometry("350x600")
    win.resizable(False,False)
    label=CTkLabel(master=win,text="Ընտրիր քո դասարանը",font=("Times",16)).pack()


    classes = {
        "10Ա դասարան": [
            "Աբրահամյան Միքայել",
            "Ավետիսյան Տիգրան",
            "Բաղդասարյան Էմմա",
            "Գրիգորյան Մարիամ",
            "Հովհաննիսյան Անի",
        ],
        "10Բ դասարան": [
            "Ալեքսանյան Դիանա",
            "Գալստյան Ռոբերտ",
            "Հակոբյան Էլեն",
            "Սահակյան Տիգրան",
            "Մարտիրոսյան Նարեկ",
        ],
        "10Գ դասարան": [
            "Բարսեղյան Մարիա",
            "Հովսեփյան Արամ",
            "Գևորգյան Սոֆիա",
            "Պետրոսյան Արամ",
        ]
    }



    CTkRadioButton(win, text="Present", value="Present").place(x=75,y=100)
    CTkRadioButton(win, text="Absent", value="Absent").place(x=75,y=140)


    my_combo=CTkComboBox(win,values=list(classes.keys())).place(x=100,y=50)


    students_frame = CTkScrollableFrame(win, label_text="Աշակերտներ",width=320,height=400)
    students_frame.place(x=5,y=100)

    win.mainloop()
