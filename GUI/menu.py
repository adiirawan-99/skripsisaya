from ctypes import WINFUNCTYPE
from tkinter import *

from pkg_resources import get_build_platform


def btn_clicked():
    print("Button Clicked")

def testing():
    global window
    window.destroy()
    from testing import showtesting
    showtesting()
def training():
    global window
    window.destroy()
    from training import showtraining
    showtraining()

def showmenu():
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

    background_img = PhotoImage(file ="assets/menu/background.png")
    background = canvas.create_image(
        576.5, 308.5,
        image=background_img)

    img0 = PhotoImage(file ="assets/menu/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = testing,
        relief = "flat")

    b0.place(
        x = 736, y = 517,
        width = 332,
        height = 55)

    img1 = PhotoImage(file ="assets/menu/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = training,
        relief = "flat")

    b1.place(
        x = 403, y = 517,
        width = 329,
        height = 55)

    window.resizable(False, False)
    window.mainloop()
