from pytube import YouTube

link = input("Enter link ")
youtube = YouTube(link)
video = youtube.streams.get_highest_resolution()
video.download()
