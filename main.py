from tkinter import *
from tkinter import messagebox
from random import randint

# -----------------Variables-------------------- #

counter = 0

# -----------------Mi amor por ella <3 logic-------------------- #


def start():
    canvas.grid_forget()
    start_button.grid_forget()
    window.title("¿Queri?")
    window.config(padx=30, pady=60)
    love_phase_label.grid(column=1, row=1)
    button_si.grid(column=0, row=1)
    button_no.grid(column=2, row=1)


def yes():
    window.title("❤❤❤❤AMOR ETERNO POR SIEMPRE❤❤❤❤")
    window.config(bg="red")
    button_si.grid_forget()
    button_no.grid_forget()
    love_phase_label.config(text="❤TE AMOOOOOOOOOO❤", bg="red")
    messagebox.showinfo(title="❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤",
                        message="SIUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU❤❤❤❤")


def no():
    global counter
    counter += 1
    if counter % 4 == 0:
        love_phase_label.config(text="¿¿¿¿Como que no????", font=("Times", "32", "bold"))
        window.title("¿Como que no?")
        messagebox.askokcancel(title="NO TE LA CREO", message="¿Como que no?")
    window.title("¿Queri?")
    love_phase_label.config(text="¿Quieres ser mi novia?", font=("Times", "24", "bold italic"))
    button_no.grid(column=randint(0, 2), row=randint(0, 2))


# -----------------Gui-------------------- #

window = Tk()
window.iconbitmap("Assets/heart.ico")
window.title("Juis Juis Juis jijiji")
window.config(pady=20)

canvas = Canvas(width=256, height=256)
logo_img = PhotoImage(file="Assets/heart_logo.png")
canvas.create_image(128, 128, image=logo_img)
canvas.grid(column=1, row=0)

start_button = Button(text="¡Empezar!", command=start)
start_button.grid(column=1, row=1, padx=5)

love_phase_label = Label(text="¿Quieres ser mi novia?", width=30, font=("Times", "24", "bold italic"))

button_si = Button(text="Si", width=4, font=("Times", "12", "bold"), command=yes)

button_no = Button(text="No", width=4, font=("Times", "12", "bold"), command=no)

window.mainloop()
