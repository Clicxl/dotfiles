import os

path = "/home/hrishikesh/Downloads"
filenames = [f for f in os.listdir(path) if not f.startswith('.')]

for filename in filenames:
    new_name = filename.replace(" ", "-").lower()
    try:
        os.rename(os.path.join(path, filename), os.path.join(path, new_name))
        print(f"Renamed: {filename} to {new_name}")
    except Exception as e:
        print(f"Error renaming {filename}: {e}")

