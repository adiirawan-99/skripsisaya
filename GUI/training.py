from tkinter import *
from tkinter import font
import partial.training_func as trainingF

def btn_clicked():
    print("Button Clicked")

def backtomenu():
    global window
    window.destroy()
    from menu import showmenu
    showmenu()

def showtraining():
    global window
    window = Tk()

    window.geometry("1100x617")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 617,
        width = 1100,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    img0 = PhotoImage(file ="assets/training/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : trainingF.uploadimage(),
        relief = "flat")

    b0.place(
        x = 98, y = 540,
        width = 469,
        height = 52)

    background_img = PhotoImage(file ="assets/training/background.png")
    background = canvas.create_image(
        583.5, 308.5,
        image=background_img)

    img1 = PhotoImage(file ="assets/training/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : trainingF.saveboar(),
        relief = "flat")

    b1.place(
        x = 681, y = 248,
        width = 200,
        height = 45)

    img2 = PhotoImage(file ="assets/training/img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = backtomenu,
        relief = "flat")

    b2.place(
        x = 785, y = 194,
        width = 214,
        height = 45)

    img3 = PhotoImage(file ="assets/training/img3.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : trainingF.savecow(),
        relief = "flat")

    b3.place(
        x = 886, y = 248,
        width = 200,
        height = 45)

    img4 = PhotoImage(file ="assets/training/img4.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        # command = lambda : trainingF.training(result),
        command = lambda : trainingF.training_all(result),
        relief = "flat")

    b4.place(
        x = 785, y = 301,
        width = 214,
        height = 45)

    result = Label( wraplength=300, background="white", font=("Chakra Petch", "14"), justify=LEFT, anchor="w")
    result.place(
                x = 690, y = 400,

                # width = 400,
                # height = 200
            )
   

    window.resizable(False, False)
    window.mainloop()
