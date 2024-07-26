from PIL import Image
from os import remove


class Converter:
    def __init__(self, file_destiantion, type, scale=1):
        self.file_destiantion = file_destiantion
        self.type = type
        self.scale = scale

    def pil_img(self):
        try:
            self.image = Image.open(self.file_destiantion, "r")
        except FileNotFoundError:
            print("Enter Proper File Destination")
            
        self.size = self.image.size

    def scale_img(self):
        self.image.resize(
            (self.size[0] // self.scale, self.size[1] // self.scale)
        ).save(f"resized.{self.type}")
        self.resized_img = f"resized.{self.type}"
        self.image = Image.open(f"resized.{self.type}")
        self.size = self.image.size

    def ascii(self):
        self.grid = []

        for i in range(self.size[1]):
            self.grid.append(["X"] * self.size[0])

        self.pix = self.image.load()
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if sum(self.pix[x, y]) == 0:
                    self.grid[y][x] = "+"
                elif sum(self.pix[x, y]) in range(1, 100):
                    self.grid[y][x] = "'"
                elif sum(self.pix[x, y]) in range(100, 200):
                    self.grid[y][x] = "*"
                elif sum(self.pix[x, y]) in range(200, 300):
                    self.grid[y][x] = "%"
                elif sum(self.pix[x, y]) in range(300, 400):
                    self.grid[y][x] = "/"
                elif sum(self.pix[x, y]) in range(400, 500):
                    self.grid[y][x] = "$"
                elif sum(self.pix[x, y]) in range(500, 600):
                    self.grid[y][x] = "&"
                elif sum(self.pix[x, y]) in range(600, 700):
                    self.grid[y][x] = "X"
                elif sum(self.pix[x, y]) in range(700, 750):
                    self.grid[y][x] = "#"
                else:
                    self.grid[y][x] = " "

        with open("saved.txt", "w") as file:
            for row in self.grid:
                file.write("".join(row) + "\n")
        remove(f"resized.{self.type}")

    def update(self):
        self.pil_img()
        self.scale_img()
        self.ascii()


if __name__ == "__main__":

    try:
        destiantion = str(input("Enter File Destination to be ASCIIified: "))
        scale = int(input("Enter Sacle Amount: (1 is default): "))
    except TypeError:
        print("Please Enter Proper Values for the above")

    Converter(destiantion, "jpg", scale).update()
