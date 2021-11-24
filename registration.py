from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from tkinter import font
from tkinter import messagebox
from datetime import datetime, date
import re
import mysql.connector
from mysql.connector import Error
'''
# Create a root window
root = Tk()
root.title("Registration")
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

# SIGN PU CLICKED
def regi(root):
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aniket@123",
        database="exp"
    )
    mycursor = mydb.cursor()

    #####################################################################################
    def Register_clicked():
        fullname = entry_1.get()
        password_3 = password_1.get()
        password_4 = password_2.get()

        """
        if password_3 != password_4:
            messagebox.showerror('Error', 'Password and confirm password must be the same!')

        else:
            password_3 == ''
            messagebox.showerror('Error', 'Password is empty')
        """


        Select = "select fullname from reg where fullname='%s'" % (fullname)
        mycursor.execute(Select)
        result = mycursor.fetchall()
        if not result:
            Insert = "Insert into reg(fullname,mobileno,email,gender,birthdate,age,password,address) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            mobileno = entry_2.get()
            email = entry_3.get()
            gender = combobox_1.get()
            birthdate = entry_4.get()
            age = entry_5.get()
            city=entry_6.get()
            password = password_1.get()
            if (mobileno != "" and email != "" and gender != "" and birthdate != "" and age != "" and city!='' and password != ""):
                Value = (fullname, mobileno, email, gender, birthdate, age, password, city)
                mycursor.execute(Insert, Value)
                mydb.commit()
                messagebox.askokcancel("Information", "Successfully Registered")
                import user_login
                main_frame.destroy()
                l_frame.destroy()
                lb.destroy()
                user_login.user_login(root)

            else:
                if (
                        mobileno != "" and email != "" and gender != "" and birthdate != "" and age != "" and password != ""):
                    messagebox.askokcancel(
                        "Information", "New Entery Fill All Details")
                else:
                    messagebox.askokcancel("Information", "Some fields left blank")
        else:
            messagebox.askokcancel("Information", "Record Already exists. sign in")
            back_clicked()

    #####################################################################################

    def CheckAge(event):
        global result  # To return calculation
        result = str(entry_4.get())

        today = date.today()
        # Convert user input into a date
        dob_data = result.split("/")

        dobDay = int(dob_data[0])
        dobMonth = int(dob_data[1])
        dobYear = int(dob_data[2])
        dob = date(dobYear, dobMonth, dobDay)

        # Calculate number of days lived
        numberOfDays = (today - dob).days

        # Convert this into whole years to display the age
        age = numberOfDays // 365

        entry_5.delete(0, str(age))
        if age != 0:
            entry_5.insert(0, str(age))

    result = 0

    #####################################################################################

    def pw():
        password_3 = password_1.get()
        password_4 = password_2.get()

        if password_3 != password_4:
            messagebox.showerror('Error', 'Password and confirm password must be the same!')

        elif password_3 == '':
            messagebox.showerror('Error', 'Password is empty')
        else:
            password_3 == password_4
            Register_clicked()


    #####################################################################################

    def checkPassword(event):
        strength = ['*Empty', '*Very Weak', '*Weak', '*Medium', '*Strong', '*Very Strong']
        score = 1
        password = password_1.get()
        print(password, len(password))

        if len(password) == 0:
            passwordStrength.set(strength[0])
            return

        if len(password) < 4:
            passwordStrength.set(strength[1])
            return

        if len(password) >= 8:
            score += 1

        if re.search("[0-9]", password):
            score += 1

        if re.search("[a-z]", password) and re.search("[A-Z]", password):
            score += 1

        if re.search(".", password):
            score += 1

        passwordStrength.set(strength[score])

    #####################################################################################

    myFont = font.Font(family='Helvetica', size=19, weight='bold')
    l_frame = Frame(root, width=int(width), height=int(height * .04), bg='navy blue')
    label_frame = Frame(l_frame, bg='navy blue')
    label = Label(label_frame, text="Registration", bg="navy blue", fg="white", font=myFont, borderwidth=0).grid(row=0,
                                                                                                           column=0,
                                                                                                           padx=int(
                                                                                                               width * .84 / 14))
    label_frame.pack()
    l_frame.pack()
    l_frame.pack_propagate(0)

    main_frame = Frame(root, width=int(width), height=int(height*.665))
    main = Frame(main_frame)

    # Ext Frame
    photo = Image.open(r"source/bg8.jpg")
    resized = photo.resize((int(width), int(height * .662)), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(resized)
    # img = PhotoImage(file="source/g.png")
    E_label = Label(main, image=new_pic, borderwidth=0)
    E_label.image = new_pic
    E_label.place(x=0, y=0)

    def back_clicked():
        l_frame.destroy()
        main_frame.destroy()
        lb.destroy()
        import user_login
        user_login.user_login(root)
    # Back Button
    img_1 = PhotoImage(file="source/Back.png")
    Button_0 = Button(main, image=img_1, borderwidth=0, command=back_clicked)
    Button_0.image = img_1
    Button_0.place(x=0, y=5)

    # Add labels and widgets here
    border=Frame(main, bg="black")
    bf=Frame(border, bg='white')
    f2 = Frame(bf, bg='white')

    # Full Name
    label_1 = Label(f2, text="Full Name -", width=15, font=("bold", 10),bg='white', anchor='w')
    label_1.grid(row=0, column=0, pady=5)
    entry_1 = Entry(f2, width=25, highlightbackground="black", highlightcolor="green", highlightthickness=1)
    entry_1.grid(row=0, column=1, pady=10)

    # Mobile No.
    label_2 = Label(f2, text="Mobile No. -", width=15, font=("bold", 10),bg='white', anchor='w')
    label_2.grid(row=1, column=0, pady=5)
    entry_2 = Entry(f2, width=25, highlightbackground="black", highlightcolor="green", highlightthickness=1)
    entry_2.grid(row=1, column=1, pady=5)

    # Email
    label_3 = Label(f2, text="Email -", width=15, font=("bold", 10), bg='white', anchor='w')
    label_3.grid(row=2, column=0, pady=5)
    entry_3 = Entry(f2, width=25, highlightbackground="black", highlightcolor="green", highlightthickness=1)
    entry_3.grid(row=2, column=1, pady=10)

    # Gender
    label_4 = Label(f2, text="Gender -", width=15, font=("bold", 10), bg='white', anchor='w')
    label_4.grid(row=3, column=0, pady=10)

    var = StringVar()
    var.set("")
    data = ("Male", "Female", "Transgender")
    combobox_1 = Combobox(f2, values=data, width=22)
    combobox_1.current(0)
    combobox_1.grid(row=3, column=1)

    """
    var = IntVar()
    R_Frame= Frame(f2)
    Radiobutton(R_Frame, text="Male", padx = 5, variable=var, value=1).pack(side=LEFT)
    Radiobutton(R_Frame, text="Female", padx = 20, variable=var, value=2).pack(side=RIGHT)
    R_Frame.grid(row=3, column=1)
    """

    # Birth Date
    label_5 = Label(f2, text="Birth Date -", width=15, font=("bold", 10), bg='white',anchor='w')
    label_5.grid(row=4, column=0, pady=5, sticky='e')
    entry_4 = DateEntry(f2, width=22, locale='en_US', date_pattern='dd/mm/y')
    entry_4.bind('<Leave>', CheckAge)
    entry_4.grid(row=4, column=1, pady=5)

    # Age
    label_6 = Label(f2, text="Age -", width=15, font=("bold", 10), bg='white', anchor='w')
    label_6.grid(row=5, column=0, pady=5)
    entry_5 = Entry(f2, width=25, highlightbackground="black", highlightcolor="green", highlightthickness=1)
    entry_4.bind('<Leave>', CheckAge)
    entry_4.bind('<Return>', CheckAge)
    entry_5.grid(row=5, column=1, pady=5)

    # Address
    label_8 = Label(f2, text="City -", width=15, font=("bold", 10), bg='white', anchor='w')
    label_8.grid(row=6, column=0, pady=10)

    var1 = StringVar()
    var1.set("")

    entry_6 = Entry(f2, textvariable=var1, width=25, highlightbackground="black", highlightcolor="green", highlightthickness=1)
    entry_6.bind('<Leave>', CheckAge)
    entry_6.grid(row=6, column=1, pady=5)

    # New Password
    label_7 = Label(f2, text="New Password -", width=15, font=("bold", 10), bg='white',anchor='w')
    label_7.grid(row=7, column=0, pady=5)
    password_1 = Entry(f2, show="*", width=25, highlightbackground="black", highlightcolor="green",
                       highlightthickness=1)
    password_1.bind("<Leave>", checkPassword)
    password_1.grid(row=7, column=1, pady=10)

    ###############################################################################################################

    # Show/Hide Password
    def password():
        if password_1.cget('show') == '' and password_2.cget('show') == '':
            password_1.config(show='*')
            password_2.config(show='*')
            show.config(text='Show Password')
        else:
            password_1.config(show='')
            password_2.config(show='')
            show.config(text='Hide Password')

    ##############################################################################################################
    # Show Password
    show = Button(f2, text='Show Password', bg='white', bd=0, anchor='w', command=password)
    show.grid(row=8,column=0, sticky='news', pady=4)

    # password strength detector
    passwordStrength = StringVar()
    checkStrLab = Label(f2, textvariable=passwordStrength, fg='red', bg='white')
    checkStrLab.grid(row=8, column=1, sticky=W)

    # Confirm Password
    label_8 = Label(f2, text="Confirm Password -", width=15, font=("bold", 10), bg='white',anchor='w')
    label_8.grid(row=9, column=0, pady=5)
    password_2 = Entry(f2, show="*", width=25, highlightbackground="black", highlightcolor="green",
                       highlightthickness=1)
    password_2.grid(row=9, column=1, pady=5)

    # Submit Button
    button_1 = Button(f2, text="Submit", bg='#45b592', fg='#ffffff', height="2", width="25",
                      command=pw).grid(row=10,
                                                     column=0,
                                                     pady=20,
                                                     columnspan=2)

    f2.pack(padx=60, pady=20)
    bf.pack( padx=3, pady=3)
    border.pack(expand=1)
    main.pack(expand=1, fill=BOTH)
    main_frame.pack()
    main_frame.grid_propagate(0)
    main_frame.pack_propagate(0)

    lb = Label(root, width=int(width), text="Registration || Travel Agency", anchor="e")
    lb.pack()

#regi(root)
#mainloop()
