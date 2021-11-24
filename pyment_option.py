from tkinter import *
from tkinter.ttk import Combobox
from datetime import *
import mysql.connector
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

# PAYMENT OPTION
def payment_option(root, id, members, stay, food, travel_amount, travel_date, day, uname, city):
    # Dates
    date_1 = list(travel_date.split("/"))
    date_var2 = f"{date_1[2]}-{date_1[1]}-{date_1[0]}"
    Begindate = datetime.strptime(date_var2, "%Y-%m-%d")
    Enddate = Begindate + timedelta(days=day)
    Begindate = Begindate.strftime("%d-%m-%y")
    Enddate = Enddate.strftime("%d-%m-%y")
    print(Begindate)
    print(Enddate)
    ##################################################################

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    myFont = font.Font(family='Helvetica', size=19, weight='bold')
    b_frame = Frame(root, width=int(width), height=int(height * .04), bg='navy blue')
    label_frame = Frame(b_frame, bg='navy blue')
    label = Label(label_frame, text="Payment", bg="navy blue", fg="white", font=myFont, borderwidth=0).grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=int(
                                                                                                                      width * .84 / 14))
    label_frame.pack()
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

    def back_clicked():
        b_frame.destroy()
        main_frame.destroy()
        lb.destroy()
        import place_details
        place_details.place_details(root, id, uname, city)

    # Back Button
    img_1 = PhotoImage(file="source/Back.png")
    Button_0 = Button(main_frame, image=img_1, borderwidth=0, command=back_clicked)
    Button_0.image = img_1
    Button_0.place(x=0, y=5)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aniket@123",
        database="exp"
    )

    mycursor = mydb.cursor()
    # query = "select * from view_place;"
    # view_place(place_id int primary key auto_increment, photo longblob, place varchar(20), days int, amount float)
    mycursor.execute(f"select package_id, place_name, stay, food, adults from add_tour where package_id={id}")
    x = mycursor.fetchone()
    place_name=x[1];
    total_cost=int(stay+food+travel_amount)

    main=Frame(main_frame, bg='#013d47')
    table_frame = Frame(main, bg="#33666d")
    label_place = Label(table_frame, text="Place", fg='white', bg='#013d47', width=18).grid(row=0, column=0, padx=1, pady=2)
    label_stay = Label(table_frame, text="Stay", fg='white', bg='#013d47', width=18).grid(row=0, column=1, padx=1, pady=2)
    label_food = Label(table_frame, text="Food", fg='white', bg='#013d47', width=18).grid(row=0, column=2, padx=1, pady=2)
    label_travelling = Label(table_frame, text="Travelling", fg='white', bg='#013d47', width=18).grid(row=0, column=3, padx=1, pady=2)
    label_total = Label(table_frame, text="Total Cost", fg='white', bg='#013d47', width=18).grid(row=0, column=4, padx=1, pady=2)

    label_place1 = Label(table_frame, text=place_name, fg='white', bg='#013d47', width=18).grid(row=1, column=0, padx=1, pady=2)
    label_stay1 = Label(table_frame, text=stay, fg='white', bg='#013d47', width=18).grid(row=1, column=1, padx=1, pady=2)
    label_food1 = Label(table_frame, text=food, fg='white', bg='#013d47', width=18).grid(row=1, column=2, padx=1, pady=2)
    label_travelling1 = Label(table_frame, text=travel_amount, fg='white', bg='#013d47', width=18).grid(row=1, column=3, padx=1, pady=2)
    label_total1 = Label(table_frame, text=total_cost, fg='white', bg='#013d47', width=18).grid(row=1, column=4, padx=1, pady=2)
    table_frame.pack()

    frm = Frame(main, bg='#013d47')
    radio=IntVar()
    radio.set("1")
    rad1 = Radiobutton(frm, text="Debit Card", variable=radio, value=1, bg='#33666d').grid(row=3, column=4, pady=5)
    rad2 = Radiobutton(frm, text="Credit Card", variable=radio, value=2, bg='#33666d').grid(row=4, column=4)
    label_cno = Label(frm, text="Card Number", fg='white', bg='#013d47').grid(row=7, column=5, pady=4)
    cno=StringVar()
    cno_entry = Entry(frm, text="enter number", textvariable=cno, width=20).grid(row=7, column=6, pady=4)
    label_cvv = Label(frm, text="CVV/CVC", fg='white', bg='#013d47').grid(row=9, column=5, pady=4)
    cvv=StringVar()
    cvv_entry = Entry(frm, text="enter CVV number", textvariable=cvv, width=20).grid(row=9, column=6, pady=4)
    label_exp = Label(frm, text="Expire Date MM/YYYY", fg='white', bg='#013d47').grid(row=11, column=5, pady=4)
    date_m=StringVar()
    date_y = StringVar()
    EXP_entry = Frame(frm, bg='#013d47')
    m_entry = Entry(EXP_entry, text="enter EXP number", textvariable=date_m, width=2).pack(side=LEFT)
    y_entry = Entry(EXP_entry, text="enter EXP number", textvariable=date_y, width=2).pack(side=LEFT)
    EXP_entry.grid(row=11, column=6, pady=4, sticky='news')
    label_total = Label(frm, text="Total Charges", fg='white', bg='#013d47').grid(row=15, column=4, pady=40)
    label_cash = Label(frm, text=f"Rs.{total_cost}/-", fg='white', bg='#013d47').grid(row=15, column=7, pady=40)
    mycursor.close()
    def pay():
        if(cno.get()!="" and cvv.get()!="" and date_m.get()!="" and date_y.get()!=""):
            mycursor=mydb.cursor()
            #print(radio.get())
            if radio.get()==1 :
                mycursor.execute(f"select * from card_details where debit_card={cno.get()} and cvv_cvc={cvv.get()} and exp_month={date_m.get()} and exp_year={date_y.get()};")
                x=mycursor.fetchone()
            elif radio.get()==2 :
                mycursor.execute(f"select * from card_details where credit_card={cno.get()} and cvv_cvc={cvv.get()} and exp_month={date_m.get()} and exp_year={date_y.get()};")
                x=mycursor.fetchone()

            if x:

                query="insert into booking(package_id, username, city, place_name, begin_date, end_date, no_members, stay_cost, food_charges,travel_amount, total_cost) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                values=(id, uname, city, place_name, Begindate, Enddate, members, stay, food, travel_amount, total_cost)
                mycursor.execute(query, values)
                mydb.commit()

                messagebox.showinfo("pyment", "Transaction Succesful")
                frm.destroy()
                b_frame.destroy()
                main_frame.destroy()
                lb.destroy()
                import  payment_recipt
                payment_recipt.payment_recipt(root, uname, city, place_name, Begindate, Enddate, members, id, stay, food, travel_amount, total_cost)
            else:
                messagebox.showinfo("pyment", "Wrong Card Information.")
        else:
            messagebox.showinfo("pyment", "enter pyment details.")


    pay_button = Button(frm, text="Pay", width=10, font=("Arial", 10), bg="grey", command=pay).grid(row=20, column=6, pady=5)
    frm.pack()
    main.pack(expand=TRUE)
    main_frame.pack()
    main_frame.pack_propagate(0)

    lb = Label(root, width=int(width), text="Payment || Travel Agency", anchor="e")
    lb.pack()

#payment_option(root, 500)
#mainloop()
