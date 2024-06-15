from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title("My MP3 Player")
root.geometry("400x300")

pygame.mixer.init()  # Initialize Pygame Mixer


def add_song():  # Add song into the playlist
    song = filedialog.askopenfilename(
        initialdir="audio/",
        title="Choose a Song",
        filetypes=(("mp3 Files", "*.mp3"),)
    ).replace("/Users/edwzou/Projects/mp3-player/audio/", "").replace(".mp3", "")  # Trim song
    playlist.insert(END, song)


def play_song():  # Play the selected song
    song = playlist.get(ACTIVE)
    song = f'/Users/edwzou/Projects/mp3-player/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


def pause_song():  # Pause the song that currently playing
    pass


def stop_song():  # Stop the song that's currently playing
    pygame.mixer.music.stop()
    playlist.selection_clear(ACTIVE)


playlist = Listbox(root, bg="black", fg="white", width=60, selectbackground="Grey")  # Create song box
playlist.pack(pady=20, padx=20)

skip_to_start_btn_img = PhotoImage(file="buttons/skip-to-start-btn.png")
play_btn_img = PhotoImage(file="buttons/play-btn.png")
pause_btn_img = PhotoImage(file="buttons/pause-btn.png")
stop_btn_img = PhotoImage(file="buttons/stop-btn.png")
forward_btn_img = PhotoImage(file="buttons/forward-btn.png")

control_frame = Frame(root)  # Create player control frame
control_frame.pack()

skip_to_start_button = Button(control_frame, image=skip_to_start_btn_img, borderwidth=0)
play_button = Button(control_frame, image=play_btn_img, borderwidth=0, command=play_song)
pause_button = Button(control_frame, image=pause_btn_img, borderwidth=0, command=pause_song)
stop_button = Button(control_frame, image=stop_btn_img, borderwidth=0, command=stop_song)
forward_button = Button(control_frame, image=forward_btn_img, borderwidth=0)

skip_to_start_button.grid(row=0, column=0, padx=5)
play_button.grid(row=0, column=1, padx=5)
pause_button.grid(row=0, column=2, padx=5)
stop_button.grid(row=0, column=3, padx=5)
forward_button.grid(row=0, column=4, padx=5)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)  # Create menu
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song to Playlist", command=add_song)

root.mainloop()
