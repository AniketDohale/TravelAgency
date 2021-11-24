from datetime import date
from tkinter import *
from tkinter.ttk import Combobox

import mysql.connector
import pwn as pwn
from PIL import ImageTk, Image
from tkinter import font
from tkinter import messagebox
from tkcalendar import DateEntry
'''
# Create a root window
root = Tk()
root.title("User Login")
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

# PLACE DETAILS
def place_details(root, pid, uname, city):
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    # Blue Label
    myFont = font.Font(family='Helvetica', size=19, weight='bold')
    b_frame = Frame(root, width=int(width), height=int(height * .04), bg='navy blue')
    label_frame = Frame(b_frame, bg='navy blue')
    label = Label(label_frame, text="Place Details", bg="navy blue", fg="white", font=myFont, borderwidth=0).grid(row=0,
                                                                                                               column=0,
                                                                                                               padx=int(
                                                                                                                   width * .84 / 14))
    label_frame.pack()
    b_frame.pack()
    b_frame.pack_propagate(0)

    frm = Frame(root, width=int(width), height=int(height*.665))

    # Ext Frame
    photo = Image.open(r"source/bg8.jpg")
    resized = photo.resize((int(width), int(height * .662)), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(resized)
    # img = PhotoImage(file="source/g.png")
    E_label = Label(frm, image=new_pic, borderwidth=0)
    E_label.image = new_pic
    E_label.place(x=0, y=0)

    def back_clicked():
        b_frame.destroy()
        frm.destroy()
        lb.destroy()
        import view_place
        view_place.user_view_place(root, uname, city)

    # Back Button
    img_1 = PhotoImage(file=r"source/Back.png")
    Button_0 = Button(frm, image=img_1, borderwidth=0, command=back_clicked)
    Button_0.image = img_1
    Button_0.place(x=0, y=5)
    border = Frame(frm, bg='black')
    table_frame = Frame(border)



    # variables
    date_var=StringVar()
    i_path = StringVar()

    days=IntVar()
    a=IntVar(); stay=IntVar(); food=IntVar()
    members=IntVar(); bus=IntVar(); train=IntVar(); flight=IntVar()


    # Details

    info_frame = Frame(table_frame)

    # database connectivity

    def database():
        global conn, cursor
        conn = mysql.connector.connect(host='localhost',
                                       database='exp',
                                       user='root',
                                       password='*********')

        cursor = conn.cursor()

    def place_details1():
        database()
        #vaibha query "select place_name ,place_description ,tour_duration ,members ,stay_cost ,date from place_details where members=5;"
        '''create table exp.add_tour(package_id  int primary key auto_increment, place_name varchar(30),
            adults int, children int, description varchar(50), stay bigint, food bigint, bus bigint, train bigint, airlines bigint,
            days int, night int, img longblob);'''

        cursor.execute(f"select * from add_tour where package_id = {pid};")
        record = cursor.fetchall()
        travel=[]
        for i in record:

            # setting variable value
            a.set(i[2]); stay.set(i[4]); food.set(i[5]); bus.set(i[6]); train.set(i[7]); flight.set(i[8])
            # travel will be like [200, 700, 0]
            members.set(a.get())
            # caclulating per person value
            stay.set(int(stay.get()/members.get()))
            food.set(int(food.get()/members.get()))
            bus.set(int(bus.get()/members.get())); train.set(int(train.get()/members.get())); flight.set(int(flight.get()/members.get()))
            travel.extend([bus.get(), train.get(), flight.get()])
            global dict1
            dict1 = {"Not_Selected": 0, "Bus": bus.get(), "Train": train.get(), "Flight": flight.get()}




            main_frame = Frame(table_frame)
            photo = Image.open(f'photo{i[0]}.jpg')
            resized = photo.resize((int(width / 4), int(height / 2.5)), Image.ANTIALIAS)
            location_pic = ImageTk.PhotoImage(resized)
            image_label_l = Label(main_frame, image=location_pic, bg="white")
            image_label_l.grid(row=1, column=1, sticky=E + W + S + N)
            image_label_l.image = location_pic
            main_frame.pack(side="left")

            # payment_table1 data fetching
            myFont2 = font.Font(family='Helvetica', size=15)
            place_name=str(i[1])
            labeinfo_name = Label(info_frame, text=place_name.capitalize(), anchor='w', font=myFont2)
            labeinfo_name.grid(row=0, column=2, pady=1, sticky='news')

            readOnlyText = Text(info_frame, width=int(labeinfo_name.winfo_width()*2.5), height=int(labeinfo_name.winfo_height()*6))
            readOnlyText.insert(1.0, i[3])
            readOnlyText.configure(state='disabled')
            readOnlyText.grid(row=1, column=2, pady=1, sticky='news')

            '''
            info_description = Label(info_frame, text=i[4], width=20, anchor='w')
            info_description.grid(row=1, column=2, pady=1, sticky='news')
            '''
            f1=Frame(info_frame)
            days.set(i[9])
            '''info_duration = OptionMenu(f1, days, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                        "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "30",
                        "31")'''
            info_duration=Label(f1, text=days.get(), font=myFont2)
            info_duration.pack(side=LEFT)
            Label(f1, text="Days", anchor='w', font=myFont2).pack(side=LEFT)
            f1.grid(row=2, column=2, pady=1, sticky='w')


            def func(value):
                # getting old values
                value = int(value)
                stay.set(int(stay.get()/members.get()))
                food.set(int(food.get()/members.get()))
                bus.set(int(bus.get()/members.get()))

                # updating old values
                members.set(int(a.get()))
                stay.set(int(stay.get()*members.get()))
                food.set(int(food.get() * members.get()))
                bus.set(int(bus.get() * members.get()))



            info_adult = Frame(info_frame)

            adult = OptionMenu(info_adult, a, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                        "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "30",
                        "31", command=func)

            #adult = Label(info_adult, text=a.get(), textvariable=a, anchor='w', font=myFont2)
            adult.pack(side=LEFT)
            Label(info_adult, text=" Members", font=myFont2).pack(side=LEFT)
            info_adult.grid(row=3, column=2, pady=1, sticky='w')

            stay.set(int(stay.get()*members.get()))
            info_stay = Label(info_frame, text=stay.get(), textvariable=stay, width=20, anchor='w', font=myFont2)
            info_stay.grid(row=4, column=2, pady=1)


            date_conf = DateEntry(info_frame, locale='en_US', textvariable=date_var, date_pattern='dd/mm/y', width=20, anchor='w')
            date_conf.grid(row=7, column=2, pady=1, sticky='news')

            data = ("Yes", "No")
            food.set(int(food.get()*members.get()))
            food_charges = Label(info_frame, text=food.get(), textvariable=food,width=20, anchor='w', font=myFont2)
            food_charges.grid(row=5, column=2)

            v = StringVar()
            v.set("")

            Bus = "Bus"
            Train = "Train"
            Flight = "Flight"
            data=["Not_Selected"]
            if travel[0]!=0:
                data.append(Bus)
            if travel[1]!=0:
                data.append(Train)
            if travel[2]!=0:
                data.append(Flight)


            data=tuple(data)
            #data = (Bus, Train, Flight)
            combobox_2 = Combobox(info_frame, values=data, textvariable=i_path, width=20)
            if len(data)!=0:
                combobox_2.current(0)
            else:
                combobox_2['values']=("No travelling Facility",)
                combobox_2.current(0)
            combobox_2.grid(row=6, column=2, sticky='news')





        cursor.close()
        conn.close()

    def payment_details2():
        day=int(days.get())
        #print(i_path.get())
        travel_amount=int(dict1[i_path.get()]*members.get())
        #print(travel_amount[0])
        # output will be like ['bus', '500']
        b_frame.destroy();
        frm.destroy();
        lb.destroy()
        import pyment_option
        pyment_option.payment_option(root, pid, members.get(), stay.get(), food.get(), travel_amount, date_var.get(), day, uname, city)

    myFont1 = font.Font(family='Helvetica', size=11,)
    # frame weights
    name_info = Label(info_frame, text="Name :", width=14, anchor='w', font=myFont1).grid(row=0, column=1, pady=1, padx=5)
    # info_name = Label(info_frame, text="Goa", width=20, anchor='w').grid(row=0, column=2, pady=1)

    description_info = Label(info_frame, text="Description :", width=14, anchor='w', font=myFont1).grid(row=1, column=1, pady=1, stick='n')
    # info_description = Label(info_frame, text="Goa with many beaches", width=20, anchor='w').grid(row=1, column=2,
    # pady=1)

    duration_info = Label(info_frame, text="Duration :", width=14, anchor='w', font=myFont1).grid(row=2, column=1, pady=1)
    # info_duration = Label(info_frame, text="2 Day + 1 Night", width=20, anchor='w').grid(row=2, column=2, pady=1)

    adult_info = Label(info_frame, text="No. Of Members :", width=14, anchor='w', font=myFont1).grid(row=3, column=1, pady=1)
    # info_adult = Label(info_frame, text="4", width=20, anchor='w').grid(row=3, column=2, pady=1)

    stay_check = Label(info_frame, text="Stay Rs :", width=14, anchor='w', font=myFont1).grid(row=4, column=1, pady=1)
    # info_stay = Label(info_frame, text="4500", width=20, anchor='w').grid(row=4, column=2, pady=1)

    info_food = Label(info_frame, text="Food :", width=14, anchor='w', font=myFont1).grid(row=5, column=1, pady=1)


    info_traveling = Label(info_frame, text="Travelling :", width=14, anchor='w', font=myFont1).grid(row=6, column=1, pady=1)
    time_label = Label(info_frame, text=" Date :", width=14, anchor='w', font=myFont1).grid(row=7, column=1, pady=1)

    place_details1()

    # date_conf = Label(info_frame, text="26 April 2021", width=20, anchor='w').grid(row=7, column=2, pady=1)

    confirm_book = Button(info_frame, text="Confirm Booking ", width=15, command=payment_details2)

    confirm_book.grid(row=11, column=2, pady=2, ipady=10)

    info_frame.pack(side="right")

    table_frame.pack(padx=3, pady=3)
    border.pack(side=TOP, expand=YES)
    frm.pack()
    frm.pack_propagate(0)

    lb = Label(root, width=int(width), text="Place Details || Travel Agency", anchor="e")
    lb.pack()

#place_details(root)
#mainloop()
