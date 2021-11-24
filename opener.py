from tkinter import *
from PIL import ImageTk, Image
from tkinter import font

# Create a root window
root = Tk()
root.title("Travel Agency")
root.state("zoomed")

bg_image = Image.open(r"source/bg4.jpg")
pic = ImageTk.PhotoImage(bg_image)
l1 = Label(root, image=pic)
l1.place(x=0, y=0)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

img_frame = Frame(root, bg='blue')
photo = Image.open(r"source/travel_1.png")
resized = photo.resize((int(width), int(height * .22)), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
image_label = Label(img_frame, image=new_pic).pack()
img_frame.pack()

import mainlogin
mainlogin.main_login(root)
#import user_info
#user_info.user_details(root)
#import package_details
#package_details.package_details(root)
#import add_tour
#add_tour.add_tour(root)
#import view_place
#view_place.user_view_place(root, 'shubham mhatre', 'Mumbai')
#import place_details
#place_details.place_details(root, 5, 'shubham')
#import place_details
#place_details.place_details(root, 7, 'shubham')
#import pyment_option
#pyment_option.payment_option(root, 1, 5000)
#import payment_recipt
#payment_recipt.payment_recipt(root, 'aniket dohale','Mumbai',  'kerala',  '24-05-21', '31-05-21', '4', '2', '5000', '0', '0', '5000')
#import registration
#registration.regi(root)
#import admin_forget
#admin_forget.admin_forget_password(root)

mainloop()
