import tkinter
from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os


songsNum = 0
kPiosenka = 0
songs = []
mixer.init()

Loaded = False
root = Tk()
root.geometry('750x320')
root.title('Music Player')
root.resizable(0, 0)
root.configure(bg="#303030")


songStopped = 1


volu = Label(root,text="Volume",bg="#303030",fg="#909191",bd="0px",font=("Fantasy", "10", "bold italic")).place(x=10,y=190)



songsLab = tkinter.Text(root,width=35,fg="white",height=16,relief=RIDGE,bg="#383a3b")
songsLab.place(x=450, y=10)



def zaladuj(listbox):
    global Loaded
    Loaded = False
    songsLab.config(state=NORMAL)
    songsNum = 0
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))
    tracks = os.listdir()
    for track in tracks:
            listbox.append(track)
    for song in songs:
        songsNum += 1
        songsLab.insert(END,str(songsNum) + ". " + song + '\n')
    songsLab.config(state=DISABLED)



def stopp_song():
    global songStopped
    global srButton
    global  Loaded
    SongName["text"]=songs[kPiosenka]
    if Loaded == False:
        mixer.music.load(songs[0])
        mixer.music.play(-1)
        mixer.music.unpause()

        Loaded = True
    songStopped += 1
    if songStopped % 2 == 0:
        mixer.music.pause()
        stop['text'] = '▶️'
    else:
        mixer.music.unpause()
        songStopped = 1
        stop['text'] = '⏸️'


def next_song():
    global kPiosenka
    kPiosenka += 1
    SongName["text"] = songs[kPiosenka]
    mixer.music.load(songs[kPiosenka])
    mixer.music.play(-1)
    mixer.music.unpause()


def previous_song():
    global kPiosenka
    kPiosenka -= 1
    SongName["text"] = songs[kPiosenka]
    mixer.music.load(songs[kPiosenka])
    mixer.music.play(-1)
    mixer.music.unpause()

def zmien_g(_=None):
    vol = var.get()
    vol = vol/10
    vol = vol/10
    mixer.music.set_volume(vol)

def load_song():
    zaladuj(songs)

var = DoubleVar()








loadB = Button(root,text="                    LOAD PLAYLIST🔽                  ",bg="#303030",relief=GROOVE,activebackground="#303030",activeforeground="#aeb0b0",bd="3px",fg="#aeb0b0",font=("Fantasy", "10", "bold"),command=load_song).place(x=450,y=270)
stop = Button(root,text="▶️",bg="#303030",relief=GROOVE,activebackground="#303030",activeforeground="#aeb0b0",bd="0px",fg="#aeb0b0",font=("Fantasy", "30", "bold"),command=stopp_song)
stop.place(x=170,y=230)
nextSong = Button(root,text="⏭",bg="#303030",relief=GROOVE,activebackground="#303030",activeforeground="#aeb0b0",bd="0px",fg="#aeb0b0",font=("Fantasy", "15", "bold"),command=next_song).place(x=250,y=250)
previousSong = Button(root,text="⏮",bg="#303030",relief=GROOVE,activebackground="#303030",activeforeground="#aeb0b0",bd="0px",fg="#aeb0b0",font=("Fantasy", "15", "bold"),command=previous_song).place(x=110,y=250)
SongName = Label(root,text="song name",bg="#303030",relief=GROOVE,width=25,bd="1px",fg="#aeb0b0",font=("Fantasy", "15", "bold italic"))
SongName.place(x=80,y=210)

suwak = tkinter.Scale(root,from_=10,to=1,orient="vertical",bd="0px",width=15,highlightcolor="#4a5052",command=zmien_g,activebackground="#4a5052",highlightbackground="#525454",showvalue=0,troughcolor="#4a5052",bg="#303030",variable=var)
suwak.place(x=25,y=210)

suwak.set(10)


root.mainloop()