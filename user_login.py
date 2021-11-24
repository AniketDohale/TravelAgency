from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
from tkinter import messagebox
import mysql.connector as mysql
from tkinter.messagebox import *

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

# USER LOGIN
def user_login(root):
    def login_user_clicked():
        username = entry1.get()
        userpassword = Password_1.get()

        if (username == "" or userpassword == ""):
            showinfo("Oops!", "Your information can't be empty!")
            return

        mydb = mysql.connect(
            host="localhost",
            user="root",
            password="Aniket@123",
            database="exp"
        )

        mycursor = mydb.cursor()
        sql = "select fullname,email, password, address from reg where email=%s and password=%s"
        val = (username, userpassword)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if result:
            # Button_2.configure(text = "Please Wait !!")
            showinfo("Success", "You're logged in!")
            l_frame.destroy(); main_frame.destroy(); lb.destroy()
            import view_place
            view_place.user_view_place(root, result[0], result[3])
        else:
            showerror("Failed", "You've entered wrong credentials!")
            Password_1.config(highlightcolor="red")

    ##############################################################################################################

    entry1 = StringVar()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()



    # Blue Label
    myFont = font.Font(family='Helvetica', size=19, weight='bold')
    l_frame = Frame(root, width=int(width), height=int(height * .04), bg='navy blue')
    label_frame = Frame(l_frame, bg='navy blue')
    label = Label(label_frame, text="User Login", bg="navy blue", fg="white", font=myFont, borderwidth=0).grid(row=0,
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
        import mainlogin
        mainlogin.main_login(root)
    # Back Button
    img_1 = PhotoImage(file="source/Back.png")
    Button_0 = Button(main, image=img_1, borderwidth=0, command=back_clicked)
    Button_0.image = img_1
    Button_0.place(x=0, y=5)

    # Add labels and widgets here
    border_frame = Frame(main, bg='black')
    bf = Frame(border_frame, bg='white')
    f2 = Frame(bf, bg='white')

    # Create Username
    # Label_1 = Label(f2, text="Username", width="20", font=('Arial', 10, 'bold'), anchor='w').pack(anchor='w')
    f4 = Frame(f2, bg='white')
    u_img = ImageTk.PhotoImage(file="source/user (1).png")
    ulabel = Label(f4, image=u_img)
    ulabel.image = u_img
    ulabel.grid(row=0, column=0, padx=8);
    ulabel.image = u_img
    Entry_1 = Entry(f4, width=45, highlightbackground="black", highlightcolor="green", highlightthickness=1,
                    textvariable=entry1, justify='c')
    Entry_1.grid(row=0, column=1, sticky='news')
    f4.pack(anchor='w', pady=15)

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

    # Create Password
    # Label_2 = Label(f2, text="Password", width="20", font=('Arial', 10,'bold'), anchor='w').pack(anchor='w')
    f3 = Frame(f2, bg="white")
    Password_1 = Entry(f3, show="*", width=45, highlightbackground="black", highlightcolor="green",
                       highlightthickness=1, justify='c')
    Password_1.grid(row=0, column=1, sticky='news')

    # Show Password
    pass_image = ImageTk.PhotoImage(file="../pythonProject1/source/pass.png")
    Button_1 = Button(f3, text="Show Password", height="0", width="26", bg="white", borderwidth=0, fg='blue',
                      image=pass_image, command=password)
    Button_1.grid(row=0, column=0, ipadx=5, padx=8)
    Button_1.image = pass_image
    f3.pack(anchor='w', pady=16)

    # Create Login Button
    Button_2 = Button(f2, text="Login", bg='#45b592', fg='#ffffff', font=(16), command=login_user_clicked)
    Button_2.pack(anchor='c', ipadx=40, pady=15)

    # Forget Password
    def forget_password_clicked():
        l_frame.destroy();
        main_frame.destroy();
        lb.destroy()
        import forget_password
        forget_password.forget_password(root)

    Button_3 = Button(f2, text="Forget Password", bg='white', height="0", width="15", borderwidth=0, fg="red",
                      anchor='w',
                      font=('Arial', 9, 'underline'), command=forget_password_clicked)
    Button_3.pack(anchor='c', pady=4)
    f4 = Frame(f2)
    # Don't have Account
    Label_2 = Label(f4, text="Don't have an Account", bg='white', height=0, borderwidth=0, font=('Arial', 10),
                    anchor='w')
    Label_2.pack(side=LEFT)

    # Sign Up
    def sign_up_clicked():
        l_frame.destroy();
        main_frame.destroy();
        lb.destroy()
        import registration
        registration.regi(root)

    Button_4 = Button(f4, text="Sign Up", fg='blue', bg='white', height=0, borderwidth=0,
                      font=('Arial', 9, 'underline', 'bold'),
                      command=sign_up_clicked)
    Button_4.pack(side=RIGHT)
    f4.pack(anchor='c')

    f2.pack(padx=60, pady=40)
    bf.pack(expand=1)

    main.pack(expand=1, fill=BOTH)
    border_frame.pack(expand=1, ipadx=3, ipady=3)
    main_frame.pack()
    main_frame.grid_propagate(0)
    main_frame.pack_propagate(0)

    lb=Label(root, width=int(width), text="User Login || Travel Agency", anchor="e")
    lb.pack()


#user_login(root)
#mainloop()
