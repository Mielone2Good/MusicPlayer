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





songsLab = tkinter.Text(root,width=35,height=16,relief=RIDGE,bg="deepskyblue")
songsLab.place(x=450, y=10)

print(type(songsLab))

def zaladuj(listbox):
    global Loaded
    Loaded = False
    songsLab.config(state=NORMAL)
    songsNum = 0
    os.chdir(filedialog.askdirectory(title='Open a songs directory'))
    tracks = os.listdir()
    print(tracks)
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
        mixer.music.play()
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
    mixer.music.play()
    mixer.music.unpause()

def previous_song():
    global kPiosenka
    kPiosenka -= 1
    SongName["text"] = songs[kPiosenka]
    mixer.music.load(songs[kPiosenka])
    mixer.music.play()
    mixer.music.unpause()



def load_song():
    zaladuj(songs)




loadB = Button(root,text="                    LOAD PLAYLIST🔽                  ",bg="#303030",relief=GROOVE,activebackground="#303030",activeforeground="#aeb0b0",bd="3px",fg="#aeb0b0",font=("Fantasy", "10", "bold"),command=load_song).place(x=450,y=270)
stop = Button(root,text="▶️",bg="#303030",relief=GROOVE,activebackground="#303030",activeforeground="#aeb0b0",bd="0px",fg="#aeb0b0",font=("Fantasy", "30", "bold"),command=stopp_song)
stop.place(x=170,y=230)
nextSong = Button(root,text="⏭",bg="#303030",relief=GROOVE,activebackground="#303030",activeforeground="#aeb0b0",bd="0px",fg="#aeb0b0",font=("Fantasy", "15", "bold"),command=next_song).place(x=250,y=250)
previousSong = Button(root,text="⏮",bg="#303030",relief=GROOVE,activebackground="#303030",activeforeground="#aeb0b0",bd="0px",fg="#aeb0b0",font=("Fantasy", "15", "bold"),command=previous_song).place(x=110,y=250)
SongName = Label(root,text="song name",bg="#303030",relief=GROOVE,width=25,bd="1px",fg="#aeb0b0",font=("Fantasy", "15", "bold italic"))
SongName.place(x=50,y=210)






root.mainloop()