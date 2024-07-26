import tkinter as tk
import customtkinter as ctk 
from pytube import YouTube,Playlist
from SETTINGS import *
from os import rename,path,chdir

# System Settings

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry(f"{WIDTH}x{HEIGHT}")
app.title("Youtube Downloader")

class Downloader:
    def __init__(self,link):
        self.link = link
        
    def start(self,type):
        self.type = type
        # try:
        self.link = Input.get()
        if self.link.startswith("https://www.youtube.com/watch?v="):
            ic("Video")
            self.player(self.link)
        elif self.link.startswith("https://www.youtube.com/playlist?list="):
            ic("Playlist")
            self.playlist()
        else: 
            finishLable.configure(text='Invalid Link',text_color='Red')            
            finishLable.update()

        # except Exception as e:
        #     finishLable.configure(
        #         text=f"Download Error: {e}", text_color='red')

    def player(self,link):
        youtube = YouTube(link,on_progress_callback=self.callback)
        ic(self.type)
        if youtube.length <= 600:
            if self.type == 'mp4 (Video)':
                youtube.streams.filter(file_extension='mp4').first()
                video = youtube.streams.get_highest_resolution()
                video.download("Youtube/videos")
                
            elif self.type == 'mp3 (Audio)':
                youtube.streams.filter(file_extension='mp3')
                video = youtube.streams.get_audio_only()
                video.download("Youtube/videos")
                ic(video.get_file_path())
                base, ext = path.splitext(video.get_file_path())
                new_base = ((base - video.title) + 'Youtube/videos') + video.title
                new_file = base + '.mp3'
                rename(video.get_file_path(), new_file)
            else: ic("Somethings wrong")
            
            Title.configure(text=youtube.title,text_color='white')
            Title.update()
            finishLable.configure(text="")
            finishLable.configure(text='Downloaded!',text_color='green')            
            finishLable.update()
        else: ic(youtube.length)

    def playlist(self):
        playlist = Playlist(self.link)

        self.urls = playlist.video_urls
        for url in self.urls:
            self.player(url)

    def callback(self,stream,chunk,bytes):
        total_size = stream.filesize
        bytes_down = total_size - bytes
        completeper = int(bytes_down / total_size * 100)
        pPercent.configure(text=str(completeper)+'%')
        pPercent.update()
        pBar.set(float(completeper/100))


app.bind("<Escape>", lambda x: app.destroy())

# Adding UI 
Title = ctk.CTkLabel(app,text="Insert The Video Link")
Title.pack(padx = 10 ,pady = 30)

url = tk.StringVar()
Input = ctk.CTkEntry(app,350,40,textvariable=url)   
Input.pack()

# option menu
type = ctk.CTkOptionMenu(app, values=['mp4 (Video)', 'mp3 (Audio)'])
type.pack(padx = 10, pady = 10)

#Classes
downloader = Downloader(Input.get())

# Finished Download
finishLable = ctk.CTkLabel(app,text="",text_color='white')
finishLable.pack(padx = 10,pady = 10)

# Progress %
pPercent = ctk.CTkLabel(app,text="0%",text_color='white')
pPercent.pack(padx = 10,pady = 10)

pBar = ctk.CTkProgressBar(app,400)
pBar.set(0)
pBar.pack(pady=10)

# Download Button
dlButton = ctk.CTkButton(app, text="Download",command=lambda: downloader.start(type.get()))
dlButton.pack()


# Run App
if "__main__" == __name__:
    app.mainloop()



