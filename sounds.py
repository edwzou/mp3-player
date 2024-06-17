import os
from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title("My MP3 Player")
root.geometry("400x350")

pygame.mixer.init()  # Initialize Pygame Mixer
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'audio'))  # Base path for audio files
paused = False
stopped = False
song_len = 0


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


def delete_song():  # Delete the currently selected song in the playlist
    stop()
    playlist.delete(ANCHOR)
    pygame.mixer.music.stop()


def delete_all_songs():  # Delete all songs in the playlist
    stop()
    playlist.delete(0, END)
    pygame.mixer.music.stop()


def song_time():  # Grab song length time
    if stopped:
        return

    curr_time = pygame.mixer.music.get_pos() / 1000  # Grab current song elapsed time
    converted_curr_time = time.strftime('%M:%S', time.gmtime(curr_time))  # Convert to time format
    song = playlist.get(ACTIVE)  # Get song title from playlist
    song_path = os.path.join(base_path, f'{song}.mp3')
    song_mut = MP3(song_path)  # Load song with mutagen
    global song_len
    song_len = song_mut.info.length  # Get song length in seconds
    converted_song_len = time.strftime('%M:%S', time.gmtime(song_len))  # Convert to time format
    curr_time += 1  # Synchronize the slider position and song position

    if int(my_slider.get()) == int(song_len):  # You've reached the end of the song
        status_bar.config(
            text=f'Time Elapsed: {converted_song_len} of {converted_song_len} ')  # Output to status bar
    elif paused:
        pass
    elif int(my_slider.get()) == int(curr_time):  # Slider hasn't been moved
        slider_pos = int(song_len)  # Update slide to position
        my_slider.config(to=slider_pos, value=int(curr_time))
    else:  # Slider has been moved
        slider_pos = int(song_len)  # Update slide to position
        my_slider.config(to=slider_pos, value=int(my_slider.get()))
        converted_curr_time = time.strftime('%M:%S', time.gmtime(my_slider.get()))  # Convert to time format
        status_bar.config(
            text=f'Time Elapsed: {converted_curr_time} of {converted_song_len} ')  # Output to status bar
        next_time = int(my_slider.get()) + 1  # Move along by one second
        my_slider.config(value=next_time)

    status_bar.after(1000, song_time)  # Update time


def backward():
    curr_song = playlist.curselection()  # Get the current song tuple number
    if curr_song:
        status_bar.config(text='')  # Reset status bar
        my_slider.config(value=0)  # Reset slider
        prev_song = (curr_song[0] - 1) % playlist.size()  # Minus one to the current song number, wrap around
        song = playlist.get(prev_song)  # Grab song title from playlist
        song_path = os.path.join(base_path, f'{song}.mp3')
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(loops=0)
        playlist.selection_clear(0, END)  # Clear active bar in playlist listbox
        playlist.activate(prev_song)  # Activate new song bar
        playlist.selection_set(prev_song, last=None)  # Set active bar to prev song
        song_time()  # Call song_time() to get the song time


def play():  # Play the selected song
    global stopped
    stopped = False
    song = playlist.get(ACTIVE)
    song_path = os.path.join(base_path, f'{song}.mp3')
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(loops=0)
    status_bar.config(text='')  # Reset status bar
    my_slider.config(value=0)  # Reset slider
    song_time()  # Call song_time() to get the song time


def pause():  # Pause the song that currently playing
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


def stop():  # Stop the song that's currently playing
    status_bar.config(text='')  # Reset status bar
    my_slider.config(value=0)  # Reset slider
    pygame.mixer.music.stop()
    playlist.selection_clear(ACTIVE)
    global stopped
    stopped = True


def forward():
    curr_song = playlist.curselection()  # Get the current song tuple number
    if curr_song:
        status_bar.config(text='')  # Reset status bar
        my_slider.config(value=0)  # Reset slider
        next_song = (curr_song[0] + 1) % playlist.size()  # Add one to the current song number, wrap around
        song = playlist.get(next_song)  # Grab song title from playlist
        song_path = os.path.join(base_path, f'{song}.mp3')
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(loops=0)
        playlist.selection_clear(0, END)  # Clear active bar in playlist listbox
        playlist.activate(next_song)  # Activate new song bar
        playlist.selection_set(next_song, last=None)  # Set active bar to next song
        song_time()  # Call song_time() to get the song time


def slide(x):
    # slider_label.config(text=f'{int(my_slider.get())} of {int(song_len)}')
    song = playlist.get(ACTIVE)
    song_path = os.path.join(base_path, f'{song}.mp3')
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))


playlist = Listbox(root, bg="black", fg="white", width=60, selectbackground="Grey")  # Create song box
playlist.pack(pady=20, padx=20)

backward_btn_img = PhotoImage(file="buttons/backward-btn.png")
play_btn_img = PhotoImage(file="buttons/play-btn.png")
pause_btn_img = PhotoImage(file="buttons/pause-btn.png")
stop_btn_img = PhotoImage(file="buttons/stop-btn.png")
forward_btn_img = PhotoImage(file="buttons/forward-btn.png")

control_frame = Frame(root)  # Create player control frame
control_frame.pack()

skip_to_start_button = Button(control_frame, image=backward_btn_img, borderwidth=0, command=backward)
play_button = Button(control_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(control_frame, image=pause_btn_img, borderwidth=0, command=pause)
stop_button = Button(control_frame, image=stop_btn_img, borderwidth=0, command=stop)
forward_button = Button(control_frame, image=forward_btn_img, borderwidth=0, command=forward)

skip_to_start_button.grid(row=0, column=0, padx=5)
play_button.grid(row=0, column=1, padx=5)
pause_button.grid(row=0, column=2, padx=5)
stop_button.grid(row=0, column=3, padx=5)
forward_button.grid(row=0, column=4, padx=5)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)  # Create add song menu
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add a Song to Playlist", command=add_song)  # Add a song at a time to the playlist
add_song_menu.add_command(label="Add Many Songs to Playlist", command=add_many_songs)  # Add many songs to the playlist

delete_song_menu = Menu(my_menu)  # Create delete song menu
my_menu.add_cascade(label="Delete Songs", menu=delete_song_menu)
delete_song_menu.add_command(label="Delete a Song from Playlist", command=delete_song)  # Delete a song
delete_song_menu.add_command(label="Delete All Songs from Playlist", command=delete_all_songs)  # Delete all songs

status_bar = Label(root, text="", borderwidth=1, relief=GROOVE, anchor=E)  # Create status bar
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.pack(pady=20)

root.mainloop()
