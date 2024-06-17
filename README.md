
# My MP3 Player

My MP3 Player is a simple GUI-based music player built using Python, Tkinter, and Pygame. It allows you to load, play, 
pause, stop, and navigate through a playlist of MP3 files.

## Features

- Add single or multiple songs to the playlist.
- Play, pause, stop, and navigate through the songs.
- Loop around the playlist when navigating forward or backward.
- Display the elapsed and total time of the currently playing song.
- Smoothly move the slider to reflect the current position in the song.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Tkinter (usually comes with Python)
- Pygame
- Mutagen

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/my-mp3-player.git
    cd my-mp3-player
    ```

2. Install Pygame:

    ```bash
    pip install pygame mutagen
    ```
   
3. Place your MP3 files in the `audio/` directory.

## Usage

Run the MP3 player:

```bash
python mp3_player.py
```

### GUI Controls

- **Add Songs**: Use the menu to add one or multiple songs to the playlist.
- **Delete Songs**: Use the menu to delete one or all songs off the playlist.
- **Backward Button**: Play the previous song in the playlist.
- **Play Button**: Play the selected song.
- **Pause Button**: Pause or unpause the current song.
- **Stop Button**: Stop the current song.
- **Forward Button**: Play the next song in the playlist.

### Slider Control

The slider allows you to navigate through the currently playing song. It displays the current position in the song and 
lets you manually adjust the playback position. The slider updates smoothly to reflect the elapsed time of the song, 
providing a visual representation of the song's progress.

### Menu Options

- **Add a Song to Playlist**: Opens a file dialog to add a single MP3 file to the playlist.
- **Add Many Songs to Playlist**: Opens a file dialog to add multiple MP3 files to the playlist.
- **Delete a Song from Playlist**:  Deletes the currently selected song from the playlist.
- **Delete All Songs from Playlist**: Deletes all songs from the playlist.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Enjoy your music with My MP3 Player! If you have any questions or need further assistance, 
feel free to contact me at edwardzou10@gmail.com.
