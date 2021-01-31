# Youtube-Downloader.mp4
we should install pypi with pip: (source)

$ python -m pip install git+https://github.com/pytube/pytube

and we should install pytube library

For videos:

He put a code to download the highest quality which is 720p ( its gonna be vcodec and acodec together)

    video.streams.get\_highest\_resolution().download(output\_path="put the output location")


we use the (output\_path="put the output location") to pick the location so make sure to choose the exact location that you want so you will be able to find it easily


and he put a code for lowest quality and its gonna be 360p 

    video.streams.get\_lowest\_resolution().download(output\_path="put the output location")


For playlist:

for video in Playlist.videos:

    video.streams.get\_highest\_resolution().download(output\_path="put Playlist link here")

as we know that will make the quality 720p

and don't forget to double-check the location

I hope that I helped to explain his code a little bit 

Have a good one

Thank you in advance...
