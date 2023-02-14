import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from pytube import YouTube
import tkinter as tk
from tkinter import (
    Button,
    Entry,
    Label,
    Menu,
    Menubutton,
    PhotoImage,
    messagebox as MessageBox,
)


def action():
    link = videos.get()
    yt = YouTube(link)
    yd = yt.streams.get_highest_resolution()
    yd.download("/Users/spiner/Documents/YoutubeVideos/")


root = tk.Tk()
root.config(bd=15)
root.title("Videos App")

label = tk.Label(root, text="Youtube Forever")

image = PhotoImage(file="youtubelogo.png")
photo = Label(root, image=image, bd=0)
photo.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="More Videos Here", menu=helpmenu)
instructions = Label(root, text="Here take videos for free")
instructions.grid(row=0, column=1)


videos = Entry(root)
videos.grid(row=1, column=1)

button = Button(root, text="Download :)", command=action)
button.grid(row=2, column=1)
root.mainloop()
