from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter.ttk import Combobox
from datetime import *
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
resized = photo.resize((int(width), int(height * .22)), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
image_label = Label(img_frame, image=new_pic).pack()
img_frame.pack()
'''

# PLACE DETAILS
def payment_recipt(root, uname, city, place_name, Begindate, Enddate, no_members, id, stay_cost, food_charges,
                   travel_amount, total_cost):
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    # Blue Label
    myFont = font.Font(family='Helvetica', size=19, weight='bold')
    l_frame = Frame(root, width=int(width), height=int(height * .04), bg='navy blue')
    label_frame = Frame(l_frame, bg='navy blue')
    label = Label(label_frame, text="Recipt", bg="navy blue", fg="white", font=myFont, borderwidth=0).grid(row=0,
                                                                                                           column=0,
                                                                                                           padx=int(
                                                                                                               width * .84 / 14))
    label_frame.pack()
    l_frame.pack()
    l_frame.pack_propagate(0)

    frm = Frame(root, width=int(width), height=int(height * .665), bg='white')

    # Ext Frame
    photo = Image.open(r"source/bg8.jpg")
    resized = photo.resize((int(width), int(height * .662)), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(resized)
    # img = PhotoImage(file="source/g.png")
    E_label = Label(frm, image=new_pic, borderwidth=0)
    E_label.image = new_pic
    E_label.place(x=0, y=0)

    def back_clicked():
        l_frame.destroy()
        frm.destroy()
        lb.destroy()
        import view_place
        view_place.user_view_place(root, uname, city)

    # Back Button
    img_1 = PhotoImage(file="source/Back.png")
    Button_0 = Button(frm, image=img_1, borderwidth=0, command=back_clicked)
    Button_0.image = img_1
    Button_0.place(x=0, y=5)
    border = Frame(frm, bg='black')
    table_frame = Frame(border, bg='white')

    frame_1 = Frame(table_frame, bg='white')
    label_title = Label(frame_1, text="Travel Agency", font=("Bold", 20)).grid(row=0, column=0, columnspan=5, pady=10,
                                                                               sticky='news')
    label_name = Label(frame_1, text="Name  :", anchor='w', bg='white').grid(row=4, column=0, pady=5, sticky='news')
    label_user_name = Label(frame_1, text=uname, anchor='w', bg='white').grid(row=4, column=1, pady=5, sticky='news')

    line5 = Frame(frame_1, bg='black', bd=2, height=2, width=400)
    line5.grid(row=1, column=0, columnspan=3);
    line5.grid_propagate(0)

    label_place = Label(frame_1, text="Tour :", anchor='w', bg='white').grid(row=5, column=0, pady=5, sticky='news')
    label_place_name = Label(frame_1, text=f" {city} to {place_name}", anchor='w', bg='white').grid(row=5, column=1,
                                                                                                    pady=5,
                                                                                                    sticky='news')

    label_members = Label(frame_1, text="Members  :", anchor='w', bg='white').grid(row=6, column=0, pady=5,
                                                                                   sticky='news')
    label_user_name = Label(frame_1, text=no_members, anchor='w', bg='white').grid(row=6, column=1, pady=5,
                                                                                   sticky='news')

    # label_booking_id = Label(frame_1, text="Booling Id  :").grid(row=4, column=5, pady=5)
    # label_id = Label(frame_1, text="292").grid(row=4, column=6, pady=5)

    frame_2 = Frame(frame_1, bg='white')

    label_date = Label(frame_2, text="Date  :", anchor='w', bg='white').grid(row=5, column=2, pady=5, sticky='news')
    label_user_date = Label(frame_2, text=f"{Begindate} to {Enddate}", anchor='w', bg='white').grid(row=5, column=3,
                                                                                                    pady=5,
                                                                                                    sticky='news')

    label_package = Label(frame_2, text="Package Id  :", anchor='w', bg='white').grid(row=6, column=2, pady=5,
                                                                                      sticky='news')
    label_package_id = Label(frame_2, text=id, anchor='w', bg='white').grid(row=6, column=3, pady=5, sticky='news')

    frame_2.grid(row=5, column=2, rowspan=2)

    # Line
    line2 = Frame(frame_1, bg='black', bd=2, height=2, width=400)
    line2.grid(row=7, column=0, columnspan=3);
    line2.grid_propagate(0)
    label_particulars = Label(frame_1, text="Particulars", font=("Bold", 15)).grid(row=8, column=0, columnspan=5,
                                                                                   sticky='news')
    # label_user_date = Label(frame_1, text="Amounts", anchor='w').grid(row=8 , column=3, pady=20, sticky='news')

    line3 = Frame(frame_1, bg='black', bd=2, height=2, width=400)
    line3.grid(row=9, column=0, columnspan=3);
    line3.grid_propagate(0)

    label_stay = Label(frame_1, text="Stay Cost  :", anchor='w', bg='white').grid(row=10, column=0, pady=5,
                                                                                  sticky='news')
    label_stay_cost = Label(frame_1, text=stay_cost, anchor='w', bg='white').grid(row=10, column=1, pady=5,
                                                                                  sticky='news')

    label_food = Label(frame_1, text="Food Cost  :", anchor='w', bg='white').grid(row=11, column=0, pady=5,
                                                                                  sticky='news')
    label_food_cost = Label(frame_1, text=food_charges, anchor='w', bg='white').grid(row=11, column=1, pady=5,
                                                                                     sticky='news')

    label_travelling = Label(frame_1, text="Travelling Cost  :", anchor='w', bg='white').grid(row=12, column=0, pady=5,
                                                                                              sticky='news')
    label_travelling_cost = Label(frame_1, text=travel_amount, anchor='w', bg='white').grid(row=12, column=1, pady=5,
                                                                                            sticky='news')

    line4 = Frame(frame_1, bg='black', bd=2, height=2, width=400)
    line4.grid(row=13, column=0, columnspan=3);
    line4.grid_propagate(0)

    label_total = Label(frame_1, text="Total Amount  :", anchor='w', bg='white').grid(row=14, column=0, pady=5,
                                                                                      sticky='news')
    label_total_amount = Label(frame_1, text=total_cost, anchor='w', bg='white').grid(row=14, column=1, pady=5,
                                                                                      sticky='news')

    line5 = Frame(frame_1, bg='black', bd=2, height=2, width=400)
    line5.grid(row=15, column=0, columnspan=3);
    line5.grid_propagate(0)

    def save():
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 18)
        pdf.cell(0, 10, 'Travel Agency', align="C", ln=1)
        pdf.ln(5)
        pdf.cell(0, 0, border=1, ln=1)
        pdf.set_font('Arial', '', 16)
        pdf.cell(100, 10, f"Name: {uname}")
        pdf.cell(100, 10, f"Date: {Begindate} to {Enddate}", ln=1)
        pdf.cell(100, 10, f"Tour: {city} to {place_name}")
        pdf.cell(100, 10, f"Package ID: {id}", ln=1)
        pdf.cell(0, 10, f"No. of Members: {no_members}", ln=1)
        pdf.ln(2)
        pdf.cell(0, 0, border=1, ln=1)
        pdf.set_font('Helvetica', '', 18)
        pdf.cell(0, 10, "Particulars", align="C", ln=1)
        pdf.cell(0, 0, border=1, ln=1)
        pdf.set_font('Arial', '', 16)
        pdf.ln(2)
        pdf.cell(50, 10, f"Stay Cost: {stay_cost}", ln=1)
        pdf.cell(50, 10, f"Food Cost: {food_charges}", ln=1)
        pdf.cell(50, 10, f"Travelling Cost: {travel_amount}", ln=1)
        pdf.cell(0, 0, border=1, ln=1)
        pdf.cell(50, 10, f"Total Cost: {total_cost}", ln=1)

        files = [('PDF', '*.pdf'),
                 ('Text Document', '*.txt')]
        file = asksaveasfile(filetypes=files, defaultextension=files)
        pdf.output(file.name, 'F')
        import subprocess
        subprocess.Popen([file.name], shell=True)

    print_button = Button(frame_1, text="Print", width=15, bg='gray', command=save).grid(row=16, column=0, columnspan=5,
                                                                                         pady=20)

    # txtReceipt = Entry(frame_1)    #.grid(row=13,column=3)
    frame_1.pack(padx=20)

    table_frame.pack(expand=1)
    border.pack(expand=1, ipadx=3, ipady=3)
    frm.pack()
    frm.pack_propagate(0)

    lb = Label(root, width=int(width), text="Recipt || Travel Agency", anchor="e")
    lb.pack()


#payment_recipt(root, 'aniket dohale', 'Mumbai', 'kerala', '24-05-21', '31-05-21', '4', '2', '5000', '0', '0', '5000')
#mainloop()