import os
from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title("My MP3 Player")
root.geometry("400x300")

pygame.mixer.init()  # Initialize Pygame Mixer
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'audio'))  # Base path for audio files
paused = False


def add_song():  # Add song into the playlist
    song_path = filedialog.askopenfilename(
        initialdir=base_path,
        title="Choose a Song",
        filetypes=(("mp3 Files", "*.mp3"),)
    )
    if song_path:  # If a song was selected
        song = os.path.relpath(song_path, base_path).replace(".mp3", "")  # Get relative path and trim .mp3
        playlist.insert(END, song)


def add_many_songs():  # Add many songs into the playlist
    song_paths = filedialog.askopenfilenames(
        initialdir=base_path,
        title="Choose a Song",
        filetypes=(("mp3 Files", "*.mp3"),)
    )
    for song_path in song_paths:
        song = os.path.relpath(song_path, base_path).replace(".mp3", "")  # Get relative path and trim .mp3
        playlist.insert(END, song)


def play():  # Play the selected song
    song = playlist.get(ACTIVE)
    song_path = os.path.join(base_path, f'{song}.mp3')
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(loops=0)


def pause():  # Pause the song that currently playing
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


def stop():  # Stop the song that's currently playing
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
play_button = Button(control_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(control_frame, image=pause_btn_img, borderwidth=0, command=pause)
stop_button = Button(control_frame, image=stop_btn_img, borderwidth=0, command=stop)
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
add_song_menu.add_command(label="Add One Song to Playlist", command=add_song)  # Add one song at a time to the playlist
add_song_menu.add_command(label="Add Many Songs to Playlist", command=add_many_songs)  # Add many songs to the playlist

root.mainloop()
