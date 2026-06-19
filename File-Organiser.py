import os
import shutil
import sys

source_folder = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

def organise_files():
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            moved = False

            for category, extensions in folders.items():
                if file_extension in extensions:
                    category_folder = os.path.join(source_folder, category)
                    os.makedirs(category_folder, exist_ok=True)

                    shutil.move(
                        file_path,
                        os.path.join(category_folder, file)
                    )

                    moved = True
                    break

            if not moved:
                others_folder = os.path.join(source_folder, "Others")
                os.makedirs(others_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(others_folder, file)
                )

organise_files()