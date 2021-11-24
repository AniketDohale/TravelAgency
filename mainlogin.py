from tkinter import *
from PIL import ImageTk, Image
from tkinter import font






# MAIN LOGIN
def main_login(root):
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    # ADMIN LOGIN CLICKED
    def a_login():
        l_frame.destroy()
        main_frame.destroy()
        lb.destroy()
        import admin_login
        admin_login.admin_login(root)

    # user login clicked
    def u_login():
        l_frame.destroy()
        main_frame.destroy()
        lb.destroy()
        import user_login
        user_login.user_login(root)

    # Blue Label
    myFont = font.Font(family='Helvetica', size=19, weight='bold')
    l_frame = Frame(root, width=int(width), height=int(height * .04), bg='navy blue')
    label_frame = Frame(l_frame, bg='navy blue')
    label = Label(label_frame, text="Main Login", bg="navy blue", fg="white", font=myFont, borderwidth=0).grid(row=0,
                                                                                                          column=0,
                                                                                                          padx=int(
                                                                                                              width * .84 / 14))
    label_frame.pack()
    l_frame.pack()
    l_frame.pack_propagate(0)

    main_frame = Frame(root, width=int(width), height=int(height*.665))


    # Ext Frame
    photo = Image.open(r"source/bg8.jpg")
    resized = photo.resize((int(width), int(height*.662)), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(resized)
    #img = PhotoImage(file="source/g.png")
    E_label = Label(main_frame, image=new_pic, borderwidth=0)
    E_label.image=new_pic
    E_label.place(x=0, y=0)
    main = Frame(main_frame, bg='#013d47')
    # Add labels and widgets here
    border=Frame(main, bg='black')
    bf=Frame(border, bg="white")
    f2 = Frame(bf, bg='white')

    b1 = Button(f2, text="Admin Login", bg='#45b592', fg='#ffffff', height="3", width="30", command=a_login).pack(pady=15)

    b2 = Button(f2, text="User Login", bg='#45b592', fg='#ffffff', height="3", width="30", command=u_login).pack(pady=15)

    f2.pack(padx=40, pady=40)
    bf.pack(padx=3, pady=3)
    border.pack()
    main.pack( pady=150)
    main_frame.pack()
    main_frame.grid_propagate(0)
    main_frame.pack_propagate(0)

    lb = Label(root, width=int(width), text="Home || Travel Agency", anchor="e")
    lb.pack()
