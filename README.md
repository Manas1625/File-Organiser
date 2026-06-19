# 📂 File Organizer (Python Automation Tool)

A simple Python automation script that organizes files in a directory into categorized folders based on their file extensions. It helps keep folders clean, structured, and easy to manage.

---

## 🚀 Features

- Automatically sorts files into categories
- Creates folders if they do not exist
- Organizes files based on extensions
- Moves unknown file types to an `Others` folder
- Works on any directory path provided by the user

---

## 📁 Supported Categories

- **Images** → .jpg, .jpeg, .png, .gif, .bmp  
- **Documents** → .pdf, .docx, .txt, .xlsx, .pptx  
- **Audio** → .mp3, .wav, .aac, .flac  
- **Videos** → .mp4, .avi, .mkv, .mov  
- **Archives** → .zip, .rar, .tar, .gz  
- **Others** → any unsupported file type  

---

## ▶️ How to Run

Run the script in terminal:

python File-Organiser.py "path_to_folder"

Example:
python File-Organiser.py "D:\Downloads"

---

## 🧠 How It Works

1. Scans all files in the given folder  
2. Checks file extension  
3. Matches extension with category list  
4. Creates category folder if not present  
5. Moves file into correct folder  

---

## 🛠️ Technologies Used

- Python
- os module
- shutil module
- sys module

---

## 🔮 Future Improvements

- GUI version (drag & drop folder support)
- Undo feature (restore original structure)
- Duplicate file detection
- Scheduled auto-cleaner
- Log file generation

---

## 👨‍💻 Author

Manas Pant
