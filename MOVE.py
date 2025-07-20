#Task 3


import os
import shutil

# Asking for folder names
source_folder = input("Enter source folder name: ").strip()
destination_folder = input("Enter destination folder name: ").strip()

# Checking if source exists
if not os.path.exists(source_folder):
    print(f"Source folder '{source_folder}' not found. Please check the name or path.")
else:
    os.makedirs(destination_folder, exist_ok=True)
    moved = 0

    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith(".jpg"):
            src = os.path.join(source_folder, file_name)
            dst = os.path.join(destination_folder, file_name)
            shutil.move(src, dst)
            moved += 1

    print(f"{moved} JPG file(s) moved successfully.")
