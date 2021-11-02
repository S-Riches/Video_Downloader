from tkinter import *
from pytube import YouTube
import random
from pathlib import Path

# get video folder
path = str(Path.home() / "Videos")

# initialise window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Video downloader")

#title
Label(root, text = 'Video Downloader', font ="consolas 20 bold").pack()

#input
link = StringVar()
Label(root, text='put your link here: ', font = 'consolas 15 bold').pack()
link_enter = Entry(root, width=70, textvariable = link).place(x = 32, y = 100)

# name generator
def generation(strlen):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for i in range(strlen):
        res = res + alphabet[random.randrange(52)]

    return res

# download function
def downloaderFunc():   
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download( path , generation(10) + '.mp4')
    Label(root, text='downloaded', font='consolas 15').pack()
    

# button that tells the program to start downloading the video
Button(root, text = 'Download!', font="consolas 15 bold", bg = 'green', padx = 2, command = downloaderFunc).place(x=190, y=125)


# makes the window appear
root.mainloop()