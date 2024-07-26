from pytube import YouTube

link = input("Enter link ")

video = youtube.streams.get_highest_resolution()
video.download("Youtube/videos")
