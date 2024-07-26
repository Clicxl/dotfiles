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


# for index,item in enumerate(Items):
#         if item in UNTOUCHABLES:
#             Items.pop(index)

for file in UNTOUCHABLES:
    Items = os.listdir(f"{path}/{file}")
    print(Items)
    for item in Items:
        os.rename(f"{path}/{item}", f"{DESTINATION['Photos']}{item}")





