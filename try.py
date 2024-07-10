from Features.Features import features

musicStreamer = features()

recognized_text = "Play Ae dil hai mushkil"

song_name = musicStreamer.get_song_name(recognized_text)
print(f"Streaming '{song_name}'...")

player = musicStreamer.stream_music(song_name)

input("Press Enter to stop playback and exit...")
player.close_player()