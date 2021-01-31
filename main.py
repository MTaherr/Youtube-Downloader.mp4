from pytube import YouTube

link = 'put your link here'

video = YouTube(link)

# vidoe quality will be 720p
video.streams.get_highest_resolution().download(output_path="put the output location")


# video quality will be 360p
video.streams.get_highest_resolution().download(output_path="put the output location")