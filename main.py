from tkinter import *

window = Tk()
window.title("Are you dumb?")
window.geometry("500x500")
window.resizable(0,0)
window.iconbitmap("questhead")

background = PhotoImage(file=r"background.gif")

bg_label = Label(window, image=background)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

window.mainloop()