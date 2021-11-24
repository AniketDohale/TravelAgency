from tkinter import *

import mysql.connector
from tkscrolledframe import ScrolledFrame
from PIL import ImageTk, Image
from tkinter import filedialog, font
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
# ADD TOUR
def add_tour(root):
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    # Package Details clicked
    def package_details_clicked():
        b_frame.destroy(); main_frame.destroy(); lb.destroy()
        import package_details
        package_details.package_details(root)

    # Booking Details clicked
    def booking_details_clicked():
        b_frame.destroy(); main_frame.destroy(); lb.destroy()
        import booking_details
        booking_details.booking_details(root)

    # USER DETAILS CLICKED
    def user_details_clicked():
        b_frame.destroy(); main_frame.destroy(); lb.destroy()
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
                borderwidth=0)
    b2 = Button(button_frame, text="View Package Details", bg="navy blue", fg="white", font=myFont, activebackground='navy blue',
                borderwidth=0, command=package_details_clicked)
    b3 = Button(button_frame, text="View Booking Details", bg="navy blue", fg="white", font=myFont, activebackground='navy blue',
                borderwidth=0, command=booking_details_clicked)
    b4 = Button(button_frame, text="View User Details", bg="navy blue", fg="white", font=myFont, activebackground='navy blue',
                borderwidth=0, command=user_details_clicked)
    b5 = Button(button_frame, text="Logout", bg="navy blue", fg="white", font=myFont, activebackground='navy blue', borderwidth=0, command=logout)

    b1.grid(row=0, column=0, padx=int(width * .84 / 36))
    b2.grid(row=0, column=1, padx=int(width * .84 / 36))
    b3.grid(row=0, column=2, padx=int(width * .84 / 36))
    b4.grid(row=0, column=3, padx=int(width * .84 / 36))
    b5.grid(row=0, column=4, padx=int(width * .84 / 36))
    button_frame.pack()
    b_frame.pack()
    b_frame.pack_propagate(0)

    # =====================================VARIABLES==========================
    pid = StringVar()
    aplace = StringVar()
    adultn = StringVar()
    des = StringVar()
    stay = StringVar()
    food = StringVar()
    bus = StringVar()
    train = StringVar()
    airline = StringVar()
    clickedday = StringVar()
    clickednig = StringVar()

    # =====================================METHODS=========================================

    def Database():
        global conn, cursor
        conn = mysql.connector.connect(host='localhost',
                                       database='exp',
                                       user='root',
                                       password='Aniket@123')
        cursor = conn.cursor()

    def Submit():
        Database()

        if pid.get == "" or aplace.get() == "" or adultn.get() == "" or des.get()=="" or stay.get()=="" or food.get()=="" or bus.get()=="" or train.get()=="" or airline.get()=="":
            lbl_result.config(text="Please complete the required field!", fg="orange")
        else:
            """username=StringVar()
            Query="SELECT * FROM add_tour"
            value=(pid,aplace,adultn,childn,des,stay,food,bus,train,airline,clickedday,clickednig)
            value=tour.add_tour.get()
            cursor.execute(Query,value)
            if cursor.fetchone() is not None:
                lbl_result.config(text="Username is already taken", fg="red")
            else:"""
            photo = x
            with open(photo, 'rb') as file:
                data = file.read()

            query = "INSERT INTO add_tour (place_name, adults, description, stay, food, bus, train, airlines, days, night, img) VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"

            cursor.execute(query, (
                                   str(aplace.get()), str(adultn.get()), str(des.get()),
                                   str(stay.get()), str(food.get()), str(bus.get()), str(train.get()), str(airline.get()),
                                   str(clickedday.get()),
                                   str(clickednig.get()), data))

            # query = "INSERT INTO add_tour (package_id, place_name, adults, children, description, stay, food, bus, train, airlines, days, night, img) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)",(str(pid.get()),
            # str(aplace.get()), str(adultn.get()), str(childn.get()),str(des.get()),
            # str(stay.get()),str(food.get()),str(bus.get()),str(train.get()),str(airline.get()),str(clickedday.get()),str(clickednig.get()),data,)

            # cursor.execute(query,(data,))
            conn.commit()
            pid.set("")
            aplace.set("")
            adultn.set("")
            des.set("")
            stay.set("")
            food.set("")
            bus.set("")
            train.set("")
            airline.set("")

            lbl_result.config(text="Successfully Created!")
            cursor.close()
            conn.close()

   # ===================================================Main Frame==================================================
    main_frame = Frame(root)

    sf = ScrolledFrame(main_frame, width=int(width), height=int(height*.615), borderwidth=0)
    sf.pack(side='top', expand=1, fill='both')
    sf.bind_arrow_keys(root)
    sf.bind_scroll_wheel(root)
    inner_frame = sf.display_widget(Frame)

    add_tour = Frame(inner_frame)
    l1 = Label(add_tour, text="Add Tour Packages")
    l1.grid(column=0, columnspan=2, pady=10)


    l3 = Label(add_tour, text="Add Place:")
    l3.grid(row=2, column=0, sticky=W, pady=10)
    # aplace=StringVar()
    place = Entry(add_tour, textvariable=aplace)
    place.grid(row=2, column=1, sticky=W, pady=10)

    l4 = Label(add_tour, text="Number of Members:")
    l4.grid(row=3, column=0, sticky=W, pady=10)
    # adultn=StringVar()
    adult_no = Entry(add_tour, textvariable=adultn)
    adult_no.grid(row=3, column=1, sticky=W, pady=10)



    l6 = Label(add_tour, text="Description:")
    l6.grid(row=5, column=0, sticky=W, pady=10)
    # des=StringVar()
    descri = Entry(add_tour, textvariable=des)
    descri.grid(row=5, column=1, sticky=W, pady=10)

    l7 = Label(add_tour, text="Stay Amount:")
    l7.grid(row=6, column=0, sticky=W, pady=10)
    # stay=StringVar()
    stay_a = Entry(add_tour, textvariable=stay)
    stay_a.grid(row=6, column=1, sticky=W, pady=10)

    l8 = Label(add_tour, text="Food Amount:")
    l8.grid(row=7, column=0, sticky=W, pady=10)
    # food=StringVar()
    food_a = Entry(add_tour, textvariable=food)
    food_a.grid(row=7, column=1, sticky=W, pady=10)

    l9 = Label(add_tour, text="Bus Amount:")
    l9.grid(row=8, column=0, sticky=W, pady=10)
    # bus=StringVar()
    bus_a = Entry(add_tour, textvariable=bus)
    bus_a.grid(row=8, column=1, sticky=W, pady=10)

    l10 = Label(add_tour, text="Train Amount:")
    l10.grid(row=9, column=0, sticky=W, pady=10)
    # train=StringVar()
    train_a = Entry(add_tour, textvariable=train)
    train_a.grid(row=9, column=1, sticky=W, pady=10)

    l11 = Label(add_tour, text="Airlines Amount:")
    l11.grid(row=10, column=0, sticky=W, pady=10)
    # airline=StringVar()
    air_a = Entry(add_tour, textvariable=airline)
    air_a.grid(row=10, column=1, sticky=W, pady=10)

    l12 = Label(add_tour, text="Number of Days:")
    l12.grid(row=11, column=0, sticky=W, pady=10)
    # clickedday=StringVar()
    clickedday.set("1")
    option = OptionMenu(add_tour, clickedday, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                        "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "30",
                        "31").grid(row=11, column=1, sticky=W, pady=10)

    l13 = Label(add_tour, text="Number of Nights:")
    l13.grid(row=12, column=0, sticky=W, pady=10)
    # clickednig=StringVar()
    clickednig.set("1")
    option = OptionMenu(add_tour, clickednig, "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                        "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "30",
                        "31").grid(row=12, column=1, sticky=W, pady=10)

    l14 = Label(add_tour, text="Add Image:")
    l14.grid(row=13, column=0, sticky=W, pady=10)

    def openfn():
        filename = filedialog.askopenfilename(title='open')
        return filename

    def open_img():
        global x
        x = openfn()
        img = Image.open(x)
        img = img.resize((200, 150), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(add_tour, image=img)
        panel.image = img
        panel.grid(row=14, column=1, sticky=W, pady=10)

    add = Button(add_tour, text="Choose File", command=open_img)
    add.grid(row=13, column=1, sticky=W, pady=10)

    # upload=Button(add_tour,text="Upload")
    # upload.grid(row=15,column=1,sticky=W,pady=10)

    btn_submit = Button(add_tour, text="Submit", command=Submit)
    btn_submit.grid(row=15, column=1, sticky=W, pady=10)

    lbl_result = Label(add_tour, text="", font=('arial', 18))
    lbl_result.grid(row=15, column=2)

    add_tour.pack(padx=width*.4)

    main_frame.pack()
    lb = Label(root, width=int(width), text="Add Tour Package || Travel Agency", anchor="e")
    lb.pack()

#add_tour()
#mainloop()
