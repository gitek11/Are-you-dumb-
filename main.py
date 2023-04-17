from tkinter import *
from random import randint

window = Tk()
window.title("Are you dumb?")
window.geometry("500x500")
window.resizable(0,0)
window.iconbitmap("questhead")





background = PhotoImage(file=r"background.gif")

bg_label = Label(window, image=background)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

text_dumb = Label(window, text = "Are you DUMB?", bg="white", font=("consolas", 50, "bold"))
text_dumb.place(x=7, y=40)

btn_yes = Button(window, text="yes", font=("consolas", 30))
btn_yes.place(x=30, y=350)

btn_no = Button(window, text="no😒", font=("consolas", 30))
btn_no.place(x=150, y=350)

window.mainloop()