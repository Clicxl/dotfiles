import os
from main import DESTINATION,UNTOUCHABLES


path = "/home/hrishikesh/Downloads"


for values in DESTINATION.values():
    Items = os.listdir(values)
    for item in Items:
        os.rename(f"{values}/{item}", f"{path}/{item}")

print("Reverting Complete!!")





