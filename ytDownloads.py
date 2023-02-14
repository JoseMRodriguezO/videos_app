import ssl

ssl._create_default_https_context = ssl._create_unverified_context


from pytube import YouTube
from sys import argv


link = argv[1]
yt = YouTube(link)
print("Title: ", yt.title)
print("View: ", yt.views)
yd = yt.streams.get_highest_resolution()
yd.download("/Users/spiner/Documents/YoutubeVideos/")
