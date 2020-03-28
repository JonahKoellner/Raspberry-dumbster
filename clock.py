from tkinter import *


from time import strftime

root = Tk()
root.configure(bg="#99ccff")
root.title("Clock")
root.attributes("-fullscreen" , True)  #makes it fullscreen. For test reasons comented so its easier to test
screenHeight=root.winfo_screenheight()
screenWidth=root.winfo_screenwidth()

def time():
    timeString = strftime('%H:%M:%S %p')
    lbl.config(text=timeString)
    lbl.after(1000, time)

lbl = Label(root, font = ('calibri', 100, 'bold'),
            background = '#99ccff',
            foreground = 'black')




'''end bit of the programm'''

lbl.pack(anchor='center')
time()
print(screenHeight , " ," , screenWidth)

mainloop()