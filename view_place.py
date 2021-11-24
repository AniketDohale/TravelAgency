from functools import partial
from tkinter import *
from tkinter import font
import mysql.connector
from tkscrolledframe import ScrolledFrame
from PIL import ImageTk,Image

'''
# Create a root window
root = Tk()
root.state("zoomed")

bg_image=Image.open(r"source/bg4.jpg")
pic=ImageTk.PhotoImage(bg_image)
l1=Label(root,image=pic)
l1.place(x=0,y=0)

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

img_frame=Frame(root,bg='blue')
photo=Image.open(r"source/travel_1.png")
resized=photo.resize((int(width*.84),int(height*.23)),Image.ANTIALIAS)
new_pic=ImageTk.PhotoImage(resized)
image_label=Label(img_frame,image=new_pic).pack()
img_frame.pack(pady=5)
'''
# USER VIEW PLACE
def user_view_place(root, uname, city):
    # LOGOUT CLICKED
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    def logout():
        main_frame.destroy()
        b_frame.destroy()
        lbl.destroy()
        import mainlogin
        mainlogin.main_login(root)

    myFont = font.Font(family='Helvetica', size=19, weight='bold')
    b_frame = Frame(root, width=int(width), height=int(height * .05), bg='navy')
    button_frame = Frame(b_frame, bg='navy')
    b1 = Button(button_frame, text="View Place", bg="navy", fg="white", font=myFont, borderwidth=0,
                activebackground="navy")
    b2 = Button(button_frame, text="Logout", bg="navy", fg="white", font=myFont, borderwidth=0, activebackground="navy", command=logout)
    # b3 = Button(button_frame, text="Button", bg="blue", fg="white", font=myFont, borderwidth=0, activebackground="blue")
    # b4 = Button(button_frame, text="Button", bg="blue", fg="white", font=myFont, borderwidth=0, activebackground="blue")
    # b5=Button(button_frame,text="Button",bg="blue",fg="white", font = myFont,borderwidth=0)

    b1.grid(row=0, column=0, padx=int(width * .84 / 14) * 2)
    b2.grid(row=0, column=1, padx=int(width * .84 / 14) * 2)
    # b3.grid(row=0, column=2, padx=int(width * .84 / 14))
    # b4.grid(row=0, column=3, padx=int(width * .84 / 14))
    # b5.grid(row=0,column=4,padx=int(width*.84/16))
    button_frame.pack()
    b_frame.pack()
    b_frame.pack_propagate(0)


    main_frame = Frame(root)
    search_frame = Frame(main_frame)
    search_frame.pack()

    sf = ScrolledFrame(main_frame, width=int(width), height=int(height*.665 ), borderwidth=0)
    sf.pack(side='top', expand=1, fill='both')
    sf.bind_arrow_keys(root)
    sf.bind_scroll_wheel(root)
    inner_frame = sf.display_widget(Frame)
    frm = Frame(inner_frame)
    frm.pack()
    def load(query):
        for widget in frm.winfo_children():
            widget.destroy()
        # sql to get images
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="*********",
            database="exp"
        )

        mycursor = mydb.cursor()
        #query = "select * from view_place;"
        #view_place(place_id int primary key auto_increment, photo longblob, place varchar(20), days int, amount float)
        mycursor.execute(query)
        x = mycursor.fetchall()

        def klik(n):
            #print(f"{n} clicked")
            b_frame.destroy();
            main_frame.destroy();
            lbl.destroy()

            import place_details
            place_details.place_details(root, n[0],uname, city)

        lb = list()
        img = list()
        # img = ImageTk.PhotoImage(Image.open(r"C:\Users\Shubham\Downloads\dubai.jpg"))
        j = 0;
        k = 0
        for i in x:

            data = i[11]
            with open(f'photo{i[0]}.jpg', 'wb') as file:
                r_data = file.write(data)

            photo = Image.open(f'photo{i[0]}.jpg')
            resized = photo.resize((int(width/6), int(height/3.5)), Image.ANTIALIAS)
            new_pic = ImageTk.PhotoImage(resized)
            img.append(new_pic)
            frame = Frame(frm)

            lb.append(
                #Button(frame, image=img[-1], width=int(width / 7.5), height=int(height / 4.5),
                       #command=partial(klik, i)))
                Button(frame, image=img[-1], command=partial(klik, i)))
            lb[-1].pack()
            lb[-1].image = img[-1]

            place_name = str(i[1])
            Button(frame, text=f"{place_name.capitalize()}", font=font.Font(size=16, underline=1, family='roman', weight='bold'), command=partial(klik, i), border=0).pack()
            Label(frame, text=f"Number of days: {i[9]} days", font=font.Font(size=15)).pack()
            amount=int(i[4]+i[5])
            Label(frame, text=f"Rs. {amount}/-", font=font.Font(size=16)).pack()

            frame.grid(row=k, column=j, padx=58, pady=10)
            j = j + 1
            if (j % 4 == 0):
                j = 0
                k = k + 1

        mycursor.close()

    #load("select * from view_place;")
    load("select * from add_tour;")
    main_frame.pack()

    def search_clicked():
        query=f"select * from add_tour where place_name Like '%{pl.get()}%';"
        load(query)
    Label(search_frame, text="Destination Place", font=font.Font(size=12)).pack(side=LEFT)
    search = Button(search_frame, text="Search", font=font.Font(size=10), command=search_clicked)
    search.pack(side=RIGHT, padx=30)
    clicked = StringVar()
    clicked.set("India")
    pl = StringVar()
    place_name = Entry(search_frame, textvariable=pl, font=font.Font(size=12))
    place_name.pack(side=RIGHT, pady=10)

    lbl = Label(root, width=int(width), text="View Place || Travel Agency", anchor="e")
    lbl.pack()

#user_view_place(root)
#mainloop()
