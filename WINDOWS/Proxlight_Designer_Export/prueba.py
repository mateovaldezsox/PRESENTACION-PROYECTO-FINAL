from cProfile import label
from subprocess import call
from tkinter import *
import pymysql
from tkinter import ttk
from tkinter import messagebox

def ventana_buscar():
    global window2
    window2 = Toplevel()
    window2.geometry("340x368")
    window2.configure(bg = "#323234")
    canvas = Canvas(
        window2,
        bg = "#323234",
        height = 368,
        width = 340,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img01 = PhotoImage(file = f"C:\\Users\\INTEL\\Desktop\\PROYECTO_FINAL_PY\\WINDOWS\\Proxlight_Designer_Export\\background01.png")
    background = canvas.create_image(
        176.0, 88.5,
        image=background_img01)

    img00 = PhotoImage(file = f"C:\\Users\\INTEL\\Desktop\\PROYECTO_FINAL_PY\\WINDOWS\\Proxlight_Designer_Export\\img00.png")
    b00 = Button(window2,
        image = img00,
        borderwidth = 0,
        highlightthickness = 0,
        background = "#557B83",
        command = btn00_clicked,
        relief = "flat")

    b00.place(
        x = 30, y = 56,
        width = 120,
        height = 130)

    img01 = PhotoImage(file = f"C:\\Users\\INTEL\\Desktop\\PROYECTO_FINAL_PY\\WINDOWS\\Proxlight_Designer_Export\\img01.png")
    b01 = Button(window2,
        image = img01,
        borderwidth = 0,
        highlightthickness = 0,
        background = "#557B83",
        command = btn3_clicked,
        relief = "flat")

    b01.place(
        x = 184, y = 56,
        width = 120,
        height = 130)

    img02 = PhotoImage(file = f"C:\\Users\\INTEL\\Desktop\\PROYECTO_FINAL_PY\\WINDOWS\\Proxlight_Designer_Export\\img02.png")
    b02 = Button(window2,
        image = img02,
        borderwidth = 0,
        highlightthickness = 0,
        background = "#323234",
        command = btn3_clicked,
        relief = "flat")

    b02.place(
        x = 30, y = 217,
        width = 120,
        height = 130)

    img03 = PhotoImage(file = f"C:\\Users\\INTEL\\Desktop\\PROYECTO_FINAL_PY\\WINDOWS\\Proxlight_Designer_Export\\img03.png")
    b03 = Button(window2,
        image = img03,
        borderwidth = 0,
        highlightthickness = 0,
        background = "#323234",
        command = btn3_clicked,
        relief = "flat")

    b03.place(
        x = 184, y = 217,
        width = 120,
        height = 130)

    window2.resizable(False, False)
    window2.mainloop()

def btn00_clicked():
    pass
    
def btn2_clicked(event):
    global window
    window.withdraw()

def btn3_clicked():
    window.deiconify()
    window2.withdraw()


window = Tk()
window.title("Administracion de alumnos")
window.geometry("330x358")
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

titulo=Label(text="Sistema de Administracion", bg="#557B83", fg="white", font=("Arial",15,"bold"))
titulo.place(x=40, y=10)

background_img = PhotoImage(file = f"C:\\Users\\INTEL\\Desktop\\PROYECTO_FINAL_PY\\WINDOWS\\Proxlight_Designer_Export\\background.png")
background = canvas.create_image(
    385.0, 180.0,
    image=background_img)

'''img0 = PhotoImage(file = f"C:\\Users\\INTEL\\Desktop\\PROYECTO_FINAL_PY\\WINDOWS\\Proxlight_Designer_Export\\img0.png")
background = canvas.create_image(
    85, 120.0,
    image=img0)
canvas.tag_bind(background, "<Button-1>", btn2_clicked)
canvas.tag_bind(background_img, "<Button-1>", btn2_clicked)

img1 = PhotoImage(file = f"C:\\Users\\INTEL\\Desktop\\PROYECTO_FINAL_PY\\WINDOWS\\Proxlight_Designer_Export\\img1.png")
background1 = canvas.create_image(
    240, 120.0,
    image=img1)
canvas.tag_bind(background1, "<Button-1>", btn2_clicked)
canvas.tag_bind(background_img, "<Button-1>", btn2_clicked)'''

img2 = PhotoImage(file = f"C:\\Users\\INTEL\\Desktop\\PROYECTO_FINAL_PY\\WINDOWS\\Proxlight_Designer_Export\\img2.png")
background2 = canvas.create_image(
    85, 120.0,
    image=img2)
canvas.tag_bind(background2, "<Button-1>", btn2_clicked)
canvas.tag_bind(background_img, "<Button-1>", btn2_clicked)

img3 = PhotoImage(file = f"C:\\Users\\INTEL\\Desktop\\PROYECTO_FINAL_PY\\WINDOWS\\Proxlight_Designer_Export\\img3.png")
background3 = canvas.create_image(
    240, 120,
    image=img3)
canvas.tag_bind(background3, "<Button-1>", btn2_clicked)
canvas.tag_bind(background_img, "<Button-1>", btn2_clicked)

img4 = PhotoImage(file = f"C:\\Users\\INTEL\\Desktop\\PROYECTO_FINAL_PY\\WINDOWS\\Proxlight_Designer_Export\\img4.png")
background4 = canvas.create_image(
    240, 275,
    image=img4)
canvas.tag_bind(background4, "<Button-1>", btn2_clicked)
canvas.tag_bind(background_img, "<Button-1>", btn2_clicked)

img5 = PhotoImage(file = f"C:\\Users\\INTEL\\Desktop\\PROYECTO_FINAL_PY\\WINDOWS\\Proxlight_Designer_Export\\img5.png")
background5 = canvas.create_image(
    85, 275,
    image=img5)
canvas.tag_bind(background5, "<Button-1>", btn2_clicked)
canvas.tag_bind(background_img, "<Button-1>", btn2_clicked)

window.resizable(False, False)
window.mainloop()

