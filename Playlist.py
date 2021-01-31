from pytube import Playlist

link = "put your public playlist link here"
Playlist = Playlist(link)

for video in Playlist.videos:
    video.streams.get_highest_resolution().download(output_path="put Playlist link here")