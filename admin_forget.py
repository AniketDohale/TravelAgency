from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from tkcalendar import DateEntry
from tkinter import messagebox
import mysql.connector as mysql
from tkinter.messagebox import *
'''
# Create a root window
root = Tk()
root.title("Forget Password(Admin)")
root.state("zoomed")

bg_image = Image.open(r"D:\Temporary\\bg4.jpg")
pic = ImageTk.PhotoImage(bg_image)
l1 = Label(root, image=pic)
l1.place(x=0, y=0)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
img_frame = Frame(root, bg='blue')
photo = Image.open(r"D:\Temporary\\travel_1.png")
resized = photo.resize((int(width * .84), int(height * .23)), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
image_label = Label(img_frame, image=new_pic).pack()
img_frame.pack(pady=5)
'''
##############################################################################################################
def admin_forget_password(root):
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    # Blue Label
    myFont = font.Font(family='Helvetica', size=19, weight='bold')
    l_frame = Frame(root, width=int(width), height=int(height * .04), bg='navy blue')
    label_frame = Frame(l_frame, bg='navy blue')
    label = Label(label_frame, text="Forget Password(Admin)", bg="navy blue", fg="white", font=myFont, borderwidth=0).grid(row=0,
                                                                                                               column=0,
                                                                                                               padx=int(
                                                                                                                   width * .84 / 14))
    label_frame.pack()
    l_frame.pack()
    l_frame.pack_propagate(0)

    def clicked():
        if entry1.get() == "" or entry2.get() == "" or entry3.get() == "":
            messagebox.showerror("Error", "Fields Missing")

        else:

            con = mysql.connect(host="localhost", user="root", password="*********", database="exp")
            cur = con.cursor()
            cur.execute("select * from al where email=%s and sk=%s", (entry1.get(), entry3.get()))
            row = cur.fetchall()

            if row:
                cur.execute("update al set password=%s where email=%s and sk=%s",
                            (entry2.get(), entry1.get(), entry3.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Password Updated Successsfully")
                back_clicked()
            else:
                showerror("Failed", "You've entered wrong credentials!")


    ##############################################################################################################



    ##############################################################################################################
    entry1 = StringVar()
    entry2 = StringVar()
    entry3 = StringVar()
    ##############################################################################################################

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
        import admin_login
        admin_login.admin_login(root)

    # Back Button
    img_1 = PhotoImage(file="source/Back.png")
    Button_0 = Button(main_frame, image=img_1, borderwidth=0, command=back_clicked)
    Button_0.image = img_1
    Button_0.place(x=0, y=5)
    # Add labels and widgets here
    border=Frame(main, bg='black')
    bf=Frame(border, bg='white')
    f2 = Frame(bf, bg='white')
    # Create Username
    Label_1 = Label(f2, text="Username", width="30", font=('Arial', 12), bg='white', anchor='w').grid(row=0, column=0)
    Entry_1 = Entry(f2, width=35, highlightbackground="black", highlightcolor="green", highlightthickness=1,
                    justify='center', textvariable=entry1)
    Entry_1.grid(row=1, column=0, ipady=2, sticky='news')

    # adding pady
    Label(f2, bg='white').grid(row=2, pady=1)

    # Create Confirm Password
    Label_2 = Label(f2, text="Confirm Password", width="30", font=('Arial', 12), bg='white', anchor='w').grid(row=3, column=0)
    Password_1 = Entry(f2, show="*", width=35, highlightbackground="black", highlightcolor="green", highlightthickness=1,
                       justify='center', textvariable=entry2)
    Password_1.grid(row=4, column=0, sticky='news')


    ###############################################################################################################

    # Show/Hide Password
    def password():
        if Password_1.cget('show') == '':
            Password_1.config(show='*')
            Button_1.config(text='Show Password')
        else:
            Password_1.config(show='')
            Button_1.config(text='Hide Password')


    ##############################################################################################################

    # Show Password
    Button_1 = Button(f2, text="Show Password", width="12", bg='white', border=0, anchor='e',command=password)
    Button_1.grid(row=5, column=0, sticky='news')

    # pady
    Label(f2, bg='white').grid(row=6, pady=1)

    # Confirm Special key
    Label_3 = Label(f2, text="Special Key", width="30", font=('Arial', 12), anchor='w', bg='white').grid(row=7, column=0)
    Entry_2 = Entry(f2, width=35, highlightbackground="black", highlightcolor="green", highlightthickness=1,
                    justify='center', textvariable=entry3)
    Entry_2.grid(row=8, column=0, ipady=2, sticky='news')

    # Create Submit Button
    Button_2 = Button(f2, text="Submit", bg='#45b592', fg='#ffffff', height="2", width="30", command=clicked)
    Button_2.grid(row=9, column=0, pady=10)

    f2.pack(padx=40, pady=40)
    bf.pack(padx=3, pady=3)
    border.pack(expand=1)
    main.pack(expand=1, fill=BOTH)
    main_frame.pack()
    main_frame.grid_propagate(0)
    main_frame.pack_propagate(0)

    lb=Label(root, width=int(width * .12), text="View Place || Travel Agency", anchor="e")
    lb.pack()

#admin_forget_password(root)
#mainloop()
