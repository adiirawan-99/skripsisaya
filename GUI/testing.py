from tkinter import *
import partial.testing_func as TestingF

def btn_clicked():
    print("Button Clicked")

def backtomenu():
    global window
    window.destroy()
    from menu import showmenu
    showmenu()

def showtesting():
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

    background_img = PhotoImage(file ="assets/testing/background.png")
    background = canvas.create_image(
        883.0, 308.5,
        image=background_img)

    img0 = PhotoImage(file ="assets/testing/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : TestingF.testing(result),
        relief = "flat")

    b0.place(
        x = 785, y = 298,
        width = 214,
        height = 45)

    img1 = PhotoImage(file ="assets/testing/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = backtomenu,
        relief = "flat")

    b1.place(
        x = 785, y = 246,
        width = 214,
        height = 45)

    img2 = PhotoImage(file ="assets/testing/img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : TestingF.uploadimage(),
        relief = "flat")

    b2.place(
        x = 10, y = 10,
        width = 646,
        height = 362)

    img3 = PhotoImage(file ="assets/testing/img3.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b3.place(
        x = 10, y = 395,
        width = 331,
        height = 216)

    img4 = PhotoImage(file ="assets/testing/img4.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b4.place(
        x = 336, y = 395,
        width = 320,
        height = 212)

    result = Label( wraplength=300, background="white", font=("Chakra Petch", "12"), justify=LEFT, anchor="w")
    result.place(
                x = 690, y = 400,

                # width = 400,
                # height = 200
            )

    
   

    window.resizable(False, False)
    window.mainloop()
