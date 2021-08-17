from tkinter import *
from tkinter import filedialog
import os
import sys
import time
from tkinter import ttk
from ttkthemes import themed_tk as tk

sys.path.append("/Users/phinix/projects/note/back_end")
sys.path.append("/Users/phinix/projects/note/gui")
os.system("clear")

from image_to_text import ImageToText
from summary import Summary
from audio_to_text import AudioToText

summary = Summary()
audio = AudioToText()
imconverter = ImageToText()
root = tk.ThemedTk()
root.set_theme("breeze")
root.title("Note")
#root.iconphoto('/Users/phinix/projects/note/gui/icon.png')
root.call('wm', 'iconphoto', root._w, PhotoImage(file='/Users/phinix/projects/note/gui/icon.png'))

global is_on, path, output_label, path_label
is_on=True

e = ttk.Label(root,font=('Helvetica bold',20), text="To take notes, chose from a image, audio file or a website")
e.grid(row=0,column=0, columnspan=3, padx=10,pady=10)

output_label = ttk.Label(root, text="",font=('Helvetica bold',20), wraplength=600)
output_label.grid(row=10,column=0, columnspan=3)

path_label = ttk.Label(root,font=('Helvetica bold',10), text="")
path_label.grid(row=2,column=2, columnspan=1)

url_label = ttk.Label(root,font=('Helvetica bold',20), text="Paste the url here").grid(row=3,column=2, padx=10,pady=10)
url_entry = ttk.Entry(root, width=15)
url_entry.grid(row=4,column=2,padx=10,pady=10)

def open_file():
    global path
    root.filename = filedialog.askopenfilename(initialdir="/Users/phinix/Desktop", title="Select A File",)
    path = root.filename
    show_selected_path()
    return root.filename

def switch():
    global is_on
    
    if is_on:
        on_button.config(image=off)
        is_on=False
    else:
        on_button.config(image=on)
        is_on=True

def loading():
    print("should have shown text")
    show_text("working...")
    root.update_idletasks()

def image_to_notes():

    global output_label, is_on
        # print(root.filename)
    raw = imconverter.convert(path)
    loading()
    if is_on:
        bullets = bullet_points.get()
        if type(bullets) != "int":
            bullets = 3
        text = summary.summarize_doc(bullets)
        show_text(raw)
    else:
        show_text(raw)


def audio_to_notes():
    global path, is_on

    bullets = bullet_points.get()
    loading()

    if is_on:

        print("starting transcription")
        time.sleep(1)
        f = open("document.txt", "a")
        f.write( audio.get_large_audio_transcription(path))
        f.close()
        text = summary.summarize_doc(bullets=3)
        show_text(text)
    else:
        time.sleep(1)
        show_text(audio.get_large_audio_transcription(path))


    

def website_to_notes():
    loading()
    url = url_entry.get()

    bullets = bullet_points.get()

    text = summary.summarize_website(url, bullets=3)
    show_text(text)

def show_text(show_text):
    global output_label
    output_label.after(1, output_label.destroy) 
    output_label = ttk.Label(root,font=('Helvetica bold',20), text=show_text, wraplength=600)
    output_label.grid(row=10,column=0, columnspan=3)

def show_selected_path():
    global path_label, path
    path_label.after(1, path_label.destroy) 
    path_label = ttk.Label(root,font=('Helvetica bold',10), text="Selected path:{}".format(path))
    path_label.grid(row=1,column=2, columnspan=1)



#def buttons

open_file_button= ttk.Button(root, text="Open File", command=open_file).grid(row=1,column=1)

# 3 big labels for 3 types of conversions

image_label = ttk.Label(root, text="Image into Notes",font=('Helvetica bold',20)).grid(row=2,column=0, padx=10,pady=10)
audio_label = ttk.Label(root, text="Audio into Notes",font=('Helvetica bold',20)).grid(row=2,column=1, padx=10,pady=10)
website_label = ttk.Label(root, text="Website into Notes",font=('Helvetica bold',20)).grid(row=2,column=2, padx=10,pady=10)

# place to enter num of points
bullet_label = ttk.Label(root, text="How many Bullets (Default: 3)",font=('Helvetica bold',20)).grid(row=3,column=1, padx=10,pady=10)
bullet_points = ttk.Entry(root, width=10)
bullet_points.grid(row=4,column=1, padx=10,pady=10)


#on or off summary
summ_label = ttk.Label(root, text="Summariazer",font=('Helvetica bold',20)).grid(row=5,column=1, padx=10,pady=10)

#def images
on = PhotoImage(file="/Users/phinix/projects/note/gui/on.png")
off = PhotoImage(file="/Users/phinix/projects/note/gui/off.png")

on_button = ttk.Button(root, image=on, command=switch)
on_button.grid(row=6,column=1, padx=10,pady=10)

#3 big buttons for the 3 main functions of app

image_button = ttk.Button(root, text="Convert Image To Notes", command=image_to_notes)
audio_button = ttk.Button(root, text="Convert Audio To Notes", command=audio_to_notes)
website_button = ttk.Button(root, text="Convert Website to notes", command=website_to_notes)

image_button.grid(row=7,column=0, padx=10,pady=10)
audio_button.grid(row=7,column=1, padx=10,pady=10)
website_button.grid(row=7,column=2, padx=10,pady=10)



root.mainloop()

