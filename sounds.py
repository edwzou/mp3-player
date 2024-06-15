from tkinter import *
import pygame

root = Tk()
root.title("My MP3 Player")
root.geometry("300x200")

pygame.mixer.init()


def play():
    pygame.mixer.music.load("audio/song1.mp3")
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()


play_button = Button(root, text="Play", font=("Helvetica", 32), command=play)
play_button.pack(pady=20)

stop_button = Button(root, text="Stop", font=("Helvetica", 32), command=stop)
stop_button.pack(pady=20)

root.mainloop()
