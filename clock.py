from tkinter import *


from time import strftime

root = Tk()

root.title("Clock")
root.attributes("-fullscreen" , True)  #makes it fullscreen. For test reasons comented so its easier to test

def time():
    timeString = strftime('%H:%M:%S %p')
    lbl.config(text=timeString)
    lbl.after(1000, time)

lbl = Label(root, font = ('calibri', 100, 'bold'),
            background = 'white',
            foreground = 'black')


lbl.pack(anchor='center')
time()

mainloop()