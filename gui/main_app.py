from tkinter import *
from tkinter import filedialog
import os
import sys
sys.path.append("/Users/phinix/projects/note/back_end")
os.system("clear")

from image_to_text import ImageToText
from summary import Summary

summary = Summary()
imconverter = ImageToText()
root = Tk()
root.title("Note.LLC")
global is_on, path
is_on=True

e = Label(root, text="To take notes, chose from a image, audio file or a website")
e.grid(row=0,column=0, columnspan=3, padx=10,pady=10)



def open_file():
    global path
    root.filename = filedialog.askopenfilename(initialdir="/Users/phinix", title="Select A File",)
    path = root.filename
    return root.filename

def switch():
    global is_on
    
    if is_on:
        on_button.config(image=off)
        is_on=False
    else:
        on_button.config(image=on)
        is_on=True

def image_to_notes():
        # print(root.filename)
        raw = imconverter.convert(path)
        if is_on:
            bullets = bullet_points.get()
            if type(bullets) != "int":
                bullets = 3
            show_text = summary.summarize(bullets)
        else:
            show_text=raw

        
        output_label = Label(root, text=show_text, wraplength=600)
        output_label.grid(row=10,column=0, columnspan=3)

def audio_to_notes():
    pass

def website_to_notes():
    pass



#def buttons

open_file_button= Button(root, text="Open File", padx=10,pady=10, command=open_file).grid(row=1,column=1)

# 3 big labels for 3 types of conversions

image_label = Label(root, text="Image into Notes").grid(row=2,column=0, padx=10,pady=10)
audio_label = Label(root, text="Audio into Notes").grid(row=2,column=1, padx=10,pady=10)
website_label = Label(root, text="Website into Notes").grid(row=2,column=2, padx=10,pady=10)

# place to enter num of points
bullet_label = Label(root, text="How many Bullet Points Would You Like? (Default: 3)").grid(row=3,column=1, padx=10,pady=10)
bullet_points = Entry(root, width=10)
bullet_points.grid(row=4,column=1, padx=10,pady=10)

#on or off summary
summ_label = Label(root, text="Summariazer").grid(row=5,column=1, padx=10,pady=10)

#def images
on = PhotoImage(file="on.png")
off = PhotoImage(file="off.png")

on_button = Button(root, image=on, command=switch)
on_button.grid(row=6,column=1, padx=10,pady=10)

#3 big buttons for the 3 main functions of app

image_button = Button(root, text="Convert Image To Notes", command=image_to_notes)
audio_button = Button(root, text="Convert Audio To Notes", command=audio_to_notes)
website_button = Button(root, text="Convert Website to notes", command=website_to_notes)

image_button.grid(row=7,column=0, padx=10,pady=10)
audio_button.grid(row=7,column=1, padx=10,pady=10)
website_button.grid(row=7,column=2, padx=10,pady=10)



root.mainloop()

