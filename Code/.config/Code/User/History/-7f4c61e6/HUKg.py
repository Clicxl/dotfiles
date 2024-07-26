from PIL import Image, ImageTk
import tkinter as tk
import ttkbootstrap as ttk
from os import remove
from icecream import ic

class Converter:
    def __init__(self,file_destiantion,type,scale=1):
        self.file_destiantion = file_destiantion
        self.type = type
        self.scale = scale


    def pil_img(self):
            self.image = Image.open(self.file_destiantion,'r')
            self.size = self.image.size


    def scale_img(self):
        self.image.resize((self.size[0]//self.scale,self.size[1]//self.scale)).save(f"resized.{self.type}")
        self.resized_img = f"resized.{self.type}"
        self.image = Image.open(f'resized.{self.type}')
        self.size = self.image.size

    def ascii(self):
        self.grid = []

        for i in range(self.size[1]):
            self.grid.append(["X"]* self.size[0])


        self.pix = self.image.load()
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if sum(self.pix[x,y]) == 0:
                    self.grid[y][x] = "+"
                elif sum(self.pix[x,y]) in range(1,100):
                    self.grid[y][x] = "'"
                elif sum(self.pix[x,y]) in range(100,200):
                    self.grid[y][x] = "*"
                elif sum(self.pix[x,y]) in range(200,300):
                    self.grid[y][x] = "%"
                elif sum(self.pix[x,y]) in range(300,400):
                    self.grid[y][x] = "/"
                elif sum(self.pix[x,y]) in range(400,500):
                    self.grid[y][x] = "$"
                elif sum(self.pix[x,y]) in range(500,600):
                    self.grid[y][x] = "&"
                elif sum(self.pix[x,y]) in range(600,700):
                    self.grid[y][x] = "X"
                elif sum(self.pix[x,y]) in range(700,750):
                    self.grid[y][x] = "#"
                else:
                    self.grid[y][x] = " "

        with open("saved.txt",'w') as file:
            for row in self.grid:
                file.write("".join(row)+"\n")
        remove(f"resized.{self.type}")



    def update(self):
        self.pil_img()
        self.scale_img()
        self.ascii()


class GUI:
    def __init__(self,size,file) -> None:
        self.size = size
        self.app = ttk.Window(themename='darkly')
        self.app.geometry(f"{size[0]}x{size[1]}")
        self.app.resizable(0,0)
        self.app.title("Image To ASCII")
        self.image = Image.open(file)
        self.image = self.image.resize((3*size[1]//4,size[0]//2 - 50))


    def img_place(self):
        self.image_frame = ttk.Frame(master=self.app)
        img = ImageTk.PhotoImage(self.image)
        img_lab =  ttk.Label(master=self.image_frame,image=img)
        img_lab.image = img
        img_lab.pack()
        self.image_frame.place(x=20,y=20)

    def text_frame(self):
        textframe = ttk.Frame(master=self.app)
        label = ttk.Label(master=textframe)
        label.pack()

        textframe.place(x= 3* self.size[1]// 4 + 50, y = 20)
        with open("saved.txt",'r') as file:
            contents = file.readlines()
            for i in contents:
                label["text"] = i
                ic(i)

    def update(self):
        self.img_place()
        self.text_frame()
        self.app.mainloop()

if __name__ == "__main__":


    GUI((1280,720),'image.jpg').update()
