File Organizer

A Python script that automatically organizes files into folders based on their file extensions.

Features
Sorts files into categories automatically
Creates folders when they do not exist
Supports Images, Documents, Audio, Videos, and Archives
Places unsupported file types into an "Others" folder
Allows users to specify the target directory
Supported Categories
Images: .jpg, .jpeg, .png, .gif, .bmp
Documents: .pdf, .docx, .txt, .xlsx, .pptx
Audio: .mp3, .wav, .aac, .flac
Videos: .mp4, .avi, .mkv, .mov
Archives: .zip, .rar, .tar, .gz
Usage
python File-Organiser.py "D:\Downloads"

If no path is provided, the script organizes files in the current working directory.

Technologies Used
Python
os
shutil
sys
Future Improvements
Graphical User Interface (GUI)
Custom file categories
Duplicate file detection
Activity logging
