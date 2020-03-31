from tkinter import *


from time import strftime

root = Tk()
root.configure(bg="#cce6ff")
root.title("Clock")
root.attributes("-fullscreen" , True)  #makes it fullscreen. For test reasons comented so its easier to test
screenHeight=root.winfo_screenheight()
screenWidth=root.winfo_screenwidth()

def time():
    timeString = strftime('%H:%M:%S %p')
    lbl.config(text=timeString)
    lbl.after(1000, time)


lbl = Label(root, font = ('calibri', 100, 'bold'),
            background = '#cce6ff',
            foreground = 'black')

left = Frame(root, borderwidth=2, relief="solid", background="#cce6ff")
right = Frame(root, borderwidth=2, relief="solid", background="#cce6ff")



'''end bit of the programm'''

lbl.pack(anchor='center', side=TOP)
time()
print(screenHeight , " ," , screenWidth)



left.pack(side="left", expand=True, fill="both")
right.pack(side="right", expand=True, fill="both")


mainloop()