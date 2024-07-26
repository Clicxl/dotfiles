import os

DESTINATION = {
    "Photos": "/home/hrishikesh/Downloads/PHOTOS/",
    "Videos": "/home/hrishikesh/Downloads/VIDEOS/",
    "PDF": "/home/hrishikesh/Downloads/PDFs/",
    "Exe": "/home/hrishikesh/Downloads/EXE/",
    "Zip": "/home/hrishikesh/Downloads/COMPRESSED/",
    "Office": "/home/hrishikesh/Downloads/OFFICE/",
}
UNTOUCHABLES = ["PHOTOS", "VIDEOS", "PDFs", "EXE", "COMPRESSED", "OFFICE"]

path = "/home/hrishikesh/Downloads"

for i in range(len(UNTOUCHABLES)):
    Items = os.listdir(path)   





