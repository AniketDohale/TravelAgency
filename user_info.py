from tkinter import *
from tkscrolledframe import ScrolledFrame
from PIL import ImageTk, Image
from tkinter import filedialog,font
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

# USER DETAILS
def user_details(root):
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

    # Package Details clicked
    def package_details_clicked():
        b_frame.destroy();
        main_frame.destroy();
        lb.destroy()
        import  package_details
        package_details.package_details(root)

    # Booking Details clicked
    def booking_details_clicked():
        b_frame.destroy();
        main_frame.destroy();
        lb.destroy()
        import booking_details
        booking_details.booking_details(root)

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
                borderwidth=0, command=package_details_clicked)
    b3 = Button(button_frame, text="View Booking Details", bg="navy blue", fg="white", font=myFont, activebackground='navy blue',
                borderwidth=0, command=booking_details_clicked)
    b4 = Button(button_frame, text="View User Details", bg="navy blue", fg="white", font=myFont, activebackground='navy blue',
                borderwidth=0)
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
    # codding of view frame is at the bottom
    view.pack()

    frm = Frame(inner_frame)
    frm.pack()
    def load(query):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aniket@123", database='exp'
        )
        mycursor = mydb.cursor()
        mycursor.execute(query)
        # mycursor.execute("select (stay + food + bus + train + airlines) as 'Total' from tour.add_tour")
        rows = mycursor.fetchall()

        tv = ttk.Treeview(frm, columns=(1, 2, 3, 4, 5, 6, 7), show="headings", height="10")
        tv.grid(row=3, column=0, sticky=NE, pady=10)

        tv.column(1, width=110)
        tv.column(2, width=80)
        tv.column(3, width=150)
        tv.column(4, width=80)
        tv.column(5, width=80)
        tv.column(6, width=80)
        tv.column(7, width=80)

        tv.heading(1, text="Name", anchor=NW)
        tv.heading(2, text="Mobile No.", anchor=NW)
        tv.heading(3, text="Email Id", anchor=NW)
        tv.heading(4, text="Gender", anchor=NW)
        tv.heading(5, text="DOB", anchor=NW)
        tv.heading(6, text="Age", anchor=NW)
        tv.heading(7, text="City", anchor=NW)

        for i in rows:
            tv.insert('', 'end', values=i)

        yscrollbar = ttk.Scrollbar(frm, orient="vertical", command=tv.yview)
        yscrollbar.grid(row=3, column=1, sticky='ns')
        tv.configure(yscrollcommand=yscrollbar.set)

    # load is a function which is used to show table data
    load("select fullname,mobileno,email,gender,birthdate,age,address from reg")

    inner_frame.pack(expand=TRUE)
    l1 = Label(view, text="View User Details", font=myFont, bg='#013d47',fg='white')
    l1.grid(column=0, columnspan=2, pady=10)

    # Codinng inside view frame
    def search_clicked():
        input=f"select fullname,mobileno,email,gender,birthdate,age,address from reg where fullname like'%{pl.get()}%'"
        load(input)

    pl = StringVar()
    place_name = Entry(view, textvariable=pl)
    place_name.grid(row=1, column=0, sticky=W, pady=10)
    search = Button(view, text="Search", command=search_clicked)
    search.grid(row=1, column=1, sticky=W, padx=10, pady=10)

    main_frame.pack()
    main_frame.pack_propagate(0)

    lb = Label(root, width=int(width), text="User Details || Travel Agency", anchor="e")
    lb.pack()

#user_details(root)
#mainloop()
