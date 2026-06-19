import os 
import shutil
import sys
# import time
# import 


#Taking source folder from command line argument, if not provided using current working directory as source folder 
# source_folder = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()  
source_folder = r"D:\TESTFOLDER"

folder = {
    "Images" : [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents" : [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio" : [".mp3", ".wav", ".aac", ".flac"],
    "Videos" : [ ".mp4", ".avi", ".mkv", ".mov"],
    "Archives" : [".zip", ".rar", ".tar", ".gz"],
    "Others" : []    
}

def organise_files():
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()   #Taking extension of the file and converting it into lowercase
            moved = False
            for category, extensions in folder.items():
                if file_extension in extensions:
                    category_folder = os.path.join(source_folder, category)
                    if not os.path.exists(category_folder):
                        os.makedirs(category_folder)
                    shutil.move(file_path, category_folder)
                    moved = True
                    break
            if not moved:
                others_folder = os.path.join(source_folder, "Others")
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, others_folder)
organise_files()
