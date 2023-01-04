from logging import root
from tkinter import *  # use for GUI
from time import strftime

root = Tk()
root.title('Digital clock')


def time():
    string = strftime('%H : %M : %S %p')
    label.config(text=string)
    label.after(1000, time)  # time updated after 1000 mili second.


label = Label(root, font=('calibri', 30, 'bold'),
              background='green', foreground='black')
label.pack(anchor='center')  # which position have the clock string
time()
mainloop()
