import os
import shutil

# Yahan apna folder path daalo jisko organize karna hai
folder_path = "/storage/emulated/0/Download"

# File type ke hisaab se categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Others": []
}

def organize_files(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            
            for category, extensions in file_types.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(path, category)
                    if not os.path.exists(dest_folder):
                        os.makedirs(dest_folder)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"Moved: {filename} -> {category}")
                    moved = True
                    break
            
            if not moved:
                dest_folder = os.path.join(path, "Others")
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"Moved: {filename} -> Others")

organize_files(folder_path)
print("Organizing complete!")