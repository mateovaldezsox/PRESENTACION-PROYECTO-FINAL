from tkinter import *
from PIL import Image, ImageTk

def btn0_clicked(event):
    print("btn0")

def btn1_clicked(event):
    print("btn1")

def btn2_clicked(event):
    print("btn2")

def btn3_clicked(event):
    print("btn3")
    
def btn4_clicked(event):
    print("btn4")

def btn5_clicked(event):
    print("btn5")

window = Tk()
window.geometry("489x358")
window.configure(bg = "#323234")
canvas = Canvas(
    window,
    bg = "#323234",
    height = 358,
    width = 489,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    385.0, 233.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
background = canvas.create_image(
    85, 120.0,
    image=img0)
canvas.tag_bind(background, "<Button-1>", btn0_clicked)
canvas.tag_bind(background_img, "<Button-1>", btn0_clicked)
'''b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 179, y = 57,
    width = 120,
    height = 120)'''

'''b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    bg = "#557B83",
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 179, y = 57,
    width = 120,
    height = 120)'''

img1 = PhotoImage(file = f"img1.png")
background1 = canvas.create_image(
    240, 120.0,
    image=img1)
canvas.tag_bind(background1, "<Button-1>", btn1_clicked)
canvas.tag_bind(background_img, "<Button-1>", btn1_clicked)
'''b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    bg = "#323234",
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 337, y = 57,
    width = 120,
    height = 120)'''

img2 = PhotoImage(file = f"img2.png")
background2 = canvas.create_image(
    400, 120.0,
    image=img2)
canvas.tag_bind(background2, "<Button-1>", btn2_clicked)
canvas.tag_bind(background_img, "<Button-1>", btn2_clicked)
'''b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    bg = "#323234",
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 28, y = 211,
    width = 120,
    height = 120)'''

img3 = PhotoImage(file = f"img3.png")
background3 = canvas.create_image(
    85, 275,
    image=img3)
canvas.tag_bind(background3, "<Button-1>", btn3_clicked)
canvas.tag_bind(background_img, "<Button-1>", btn3_clicked)
'''b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    bg = "#323234",
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 179, y = 211,
    width = 120,
    height = 120)'''

img4 = PhotoImage(file = f"img4.png")
background4 = canvas.create_image(
    240, 275,
    image=img4)
canvas.tag_bind(background4, "<Button-1>", btn4_clicked)
canvas.tag_bind(background_img, "<Button-1>", btn4_clicked)
'''b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    bg = "#323234",
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 337, y = 211,
    width = 120,
    height = 120)'''

img5 = PhotoImage(file = f"img5.png")
background5 = canvas.create_image(
    400, 275,
    image=img5)
canvas.tag_bind(background5, "<Button-1>", btn5_clicked)
canvas.tag_bind(background_img, "<Button-1>", btn5_clicked)
'''b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    bg = "#557B83",
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 27, y = 56,
    width = 110,
    height = 119)'''

window.resizable(False, False)
window.mainloop()
