from tkinter import *
from tkscrolledframe import ScrolledFrame
from PIL import ImageTk, Image
from tkinter import filedialog, font
import os
from tkinter import ttk
import mysql.connector
'''
# Create a root window
root = Tk()
root.state("zoomed")

bg_image = Image.open(r"source/bg4.jpg")
pic = ImageTk.PhotoImage(bg_image)
l1 = Label(root, image=pic)
l1.place(x=0, y=0)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

img_frame = Frame(root, bg='blue')
photo = Image.open(r"source/travel_1.png")
resized = photo.resize((int(width * .84), int(height * .23)), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
image_label = Label(img_frame, image=new_pic).pack()
img_frame.pack(pady=5)
'''
# PACKAGE DETAILS
def package_details(root):
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    # ADD TOUR CLICKED
    def add_tour_clicked():
        b_frame.destroy();
        main_frame.destroy();
        lb.destroy()
        # Opening package details
        import add_tour
        add_tour.add_tour(root)

    # Booking Details clicked
    def booking_details_clicked():
        b_frame.destroy();
        main_frame.destroy();
        lb.destroy()
        import booking_details
        booking_details.booking_details(root)

    # USER DETAILS CLICKED
    def user_details_clicked():
        b_frame.destroy();
        main_frame.destroy();
        lb.destroy()
        import user_info
        user_info.user_details(root)

    # LOGOUT CLICKED
    def logout():
        main_frame.destroy()
        b_frame.destroy()
        lb.destroy()
        import mainlogin
        mainlogin.main_login(root)

    myFont = font.Font(family='Helvetica', size=19, weight='bold')
    b_frame = Frame(root, width=int(width), height=int(height * .05), bg='navy blue')
    button_frame = Frame(b_frame, bg='navy blue')
    b1 = Button(button_frame, text="Package Details", bg="navy blue", fg="white", font=myFont, activebackground='navy blue',
                borderwidth=0, command=add_tour_clicked)
    b2 = Button(button_frame, text="View Package Details", bg="navy blue", fg="white", font=myFont, activebackground='navy blue',
                borderwidth=0)
    b3 = Button(button_frame, text="View Booking Details", bg="navy blue", fg="white", font=myFont, activebackground='navy blue',
                borderwidth=0, command=booking_details_clicked)
    b4 = Button(button_frame, text="View User Details", bg="navy blue", fg="white", font=myFont, activebackground='navy blue',
                borderwidth=0, command=user_details_clicked)
    b5 = Button(button_frame, text="Logout", bg="navy blue", fg="white", font=myFont, activebackground='navy blue', borderwidth=0,
                command=logout)

    b1.grid(row=0, column=0, padx=int(width * .84 / 36))
    b2.grid(row=0, column=1, padx=int(width * .84 / 36))
    b3.grid(row=0, column=2, padx=int(width * .84 / 36))
    b4.grid(row=0, column=3, padx=int(width * .84 / 36))
    b5.grid(row=0, column=4, padx=int(width * .84 / 36))
    button_frame.pack()
    b_frame.pack()
    b_frame.pack_propagate(0)

    main_frame = Frame(root, width=int(width), height=int(height*.665))
    # Ext Frame
    photo = Image.open(r"source/bg8.jpg")
    resized = photo.resize((int(width), int(height * .662)), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(resized)
    # img = PhotoImage(file="source/g.png")
    E_label = Label(main_frame, image=new_pic, borderwidth=0)
    E_label.image = new_pic
    E_label.place(x=0, y=0)
    inner_frame = Frame(main_frame, bg='#013d47')
    view = Frame(inner_frame, bg='#013d47')

    view.pack(padx=420)

    frm = Frame(inner_frame)
    frm.pack()

    def load(query):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="*********", database='exp'
        )
        mycursor = mydb.cursor()
        mycursor.execute(query)
        rows = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), show="headings", height="10")
        tv.grid(row=3, column=0, sticky=NE, pady=10)

        tv.column(1, width=90)
        tv.column(2, width=90)
        tv.column(3, width=80)
        tv.column(4, width=90)
        tv.column(5, width=90)
        tv.column(6, width=90)
        tv.column(7, width=90)
        tv.column(8, width=90)
        tv.column(9, width=100)
        tv.column(10, width=80)
        tv.column(11, width=80)
        # tv.column(13,width=80)

        tv.heading(1, text="Package Id", anchor=NW)
        tv.heading(2, text="Place", anchor=NW)
        tv.heading(3, text="Members", anchor=NW)
        tv.heading(4, text="Description", anchor=NW)
        tv.heading(5, text="Stay amount", anchor=NW)
        tv.heading(6, text="Food amount", anchor=NW)
        tv.heading(7, text="Bus amount", anchor=NW)
        tv.heading(8, text="Train amount", anchor=NW)
        tv.heading(9, text="Airlines amount", anchor=NW)
        tv.heading(10, text="Days", anchor=NW)
        tv.heading(11, text="Nights", anchor=NW)
        # tv.heading(13,text="Image",anchor=NW)

        for i in rows:
            tv.insert('', 'end', values=i)

        yscrollbar = ttk.Scrollbar(frm, orient="vertical", command=tv.yview)
        yscrollbar.grid(row=3, column=1, sticky='ns')
        tv.configure(yscrollcommand=yscrollbar.set)

    load(
        "select package_id,place_name,adults,description,stay,food,bus,train,airlines,days,night from add_tour")

    l1 = Label(view, text="View Packages", font=myFont, bg='#013d47',fg='white')
    l1.grid(column=0, columnspan=2, pady=10)

    def search_clicked():
        input = f"select package_id,place_name,adults,description,stay,food,bus,train,airlines,days,night from add_tour where place_name like'%{pl.get()}%'"
        load(input)

    pl = StringVar()
    place_name = Entry(view, textvariable=pl)
    place_name.grid(row=1, column=0, sticky=W, pady=10)
    search = Button(view, text="Search", command=search_clicked)
    search.grid(row=1, column=1, sticky=W, padx=10, pady=10)

    frm.pack()
    inner_frame.pack(pady=10, expand=TRUE)

    main_frame.pack()
    main_frame.pack_propagate(0)

    lb = Label(root, width=int(width), text="Package Details || Travel Agency", anchor="e")
    lb.pack()
#package_details(root)
#mainloop()
