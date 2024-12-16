import os
from flask import Flask, render_template
import eyed3

app = Flask(__name__)

# Path to the music directory
MUSIC_DIR = 'static/music'

def get_songs():
    songs = []
    # List all files in the music directory
    for filename in os.listdir(MUSIC_DIR):
        if filename.endswith('.mp3'):
            # Extract metadata from MP3 file
            audio_file = eyed3.load(os.path.join(MUSIC_DIR, filename))
            song_info = {
                'name': audio_file.tag.title if audio_file.tag.title else filename,
                'artist': audio_file.tag.artist if audio_file.tag.artist else 'Unknown Artist',
                'album': audio_file.tag.album if audio_file.tag.album else 'Unknown Album',
                'file': filename
            }
            songs.append(song_info)
    return songs

@app.route('/')
def home():
    songs = get_songs()  # Get the list of songs from the directory
    return render_template('index.html', songs=songs)

if __name__ == '__main__':
    app.run(debug=True)
