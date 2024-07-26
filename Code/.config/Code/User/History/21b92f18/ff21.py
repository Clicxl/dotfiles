import os
from main import DESTINATION,UNTOUCHABLES


path = "    "


# for index,item in enumerate(Items):
#         if item in UNTOUCHABLES:
#             Items.pop(index)

for values in DESTINATION.values():
    Items = os.listdir(values)
    print(Items)
    for item in Items:
        os.rename(f"{values}/{item}", f"{path}/{item}")

print("Reverting Complete!!")





