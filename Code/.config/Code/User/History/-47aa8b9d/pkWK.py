import os

UNTOUCHABLES = ["PHOTOS", "VIDEOS", "PDFs", "EXE", "COMPRESSED", "OFFICE"]

DESTINATION = {
    "Photos": "/home/hrishikesh/Downloads/PHOTOS/",
    "Videos": "/home/hrishikesh/Downloads/VIDEOS/",
    "PDF": "/home/hrishikesh/Downloads/PDFs/",
    "Exe": "/home/hrishikesh/Downloads/EXE/",
    "Zip": "/home/hrishikesh/Downloads/COMPRESSED/",
    "Office": "/home/hrishikesh/Downloads/OFFCIE/",
}

path = str(input("Enter The Path of The File: "))

Items = os.listdir(path)

for item in Items:
    file = os.path.splitext(item)

    new_name = item.replace(" ", "-").lower()
    os.rename(os.path.join(file[0], file[1]), os.path.join(file[0], new_name))

    if file[1] in [".png", ".jpg", ".jpeg", ".svg", ".wepg", "gif"]:
        os.rename(f"{path}{item}", f"{DESTINATION['Photos']}{item}")
    elif file[1] in [".mp4", ".mp3", ".mov", ".mkv", ".webm"]:
        os.rename(path + item, f"{DESTINATION['Videos']}{item}")
    elif file[1] in [".zip", ".tar.xz", ".rar"]:
        os.rename(path + item, f"{DESTINATION['Zip']}{item}")
    elif file[1] in [".exe",".deb",'.appimage','.iso']:
        os.rename(f"{path}{item}", f"{DESTINATION['Exe']}{item}")
    elif file[1] in [".pdf"]:
        os.rename(f"{path}{item}", f"{DESTINATION['PDF']}{item}")
    elif file[1] in [".doc", ".docx", ".csv", ".xls",".pptx"]:
        os.rename(f"{path}{item}", f"{DESTINATION['Office']}{item}")
    else:
        print("Unknown File Type")

print("All Items are sorted")
