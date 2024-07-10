import yt_dlp
from ffpyplayer.player import MediaPlayer
import re

# Function to stream music from YouTube
class MusicStreamer:
    def stream_music(self, song_name):
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True
        }

        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            info_dict = ydl.extract_info(f"ytsearch:{song_name}", download=False)
            video_info = info_dict['entries'][0]
            stream_url = video_info['url']
            
        self.player = MediaPlayer(stream_url)
        self.player.set_pause(False)
        return self.player
    def get_song_name(self, text):
        self.match = re.search(r'play\s+(.*)', text, re.IGNORECASE)
        if self.match:
            return self.match.group(1).strip()
        return None

# Main function
# if __name__ == "__main__":
#     song_name = input("Enter the song name: ")  # Get the song name from the user
#     print(f"Streaming '{song_name}'...")

#     player = MusicStreamer.stream_music(song_name)

#     # Keep the script running to allow the music to play
#     input("Press Enter to stop playback and exit...")
#     player.close_player()