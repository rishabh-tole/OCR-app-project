from tkinter import *
import os
os.system("clear")


root = Tk()
root.title("Note.LLC")
root.geometry("400x600")

def hi():
    hello_label = Label(root, text="hello" + textbox.get())
    hello_label.pack()

myLabel = Label(root, text="enter your first name:")
myLabel.pack()

textbox = Entry(root, width=30)
textbox.pack()

button = Button(root, text="submit", command=hi)
button.pack()



root.mainloop()
