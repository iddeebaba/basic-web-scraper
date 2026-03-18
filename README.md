# Python Automation Scripts

Simple Python tools I created to automate repetitive tasks and save time.

## Included Scripts
- **file_organizer.py**  
  Automatically sorts files: moves PDFs to a "PDFs" folder and images (jpg/png/etc.) to an "Images" folder.

- **simple_task_reminder.py**  
  Sets a timed reminder that notifies you after a chosen delay (good for breaks, tasks, etc.).

## Technologies
- Python 3  
- Standard libraries only: os, shutil, time, datetime

No extra packages needed.

## How to Run

1. Download or copy the scripts from this repository  
2. For **file_organizer.py**:
   - Open the file in a text editor (Notepad, VS Code, etc.)
   - Change the `source_folder` path to your own folder (e.g. Downloads, Desktop, etc.)
   - Save the file
   - Open Command Prompt / Terminal
   - Go to the folder where the script is saved (example: `cd Desktop`)
   - Run:
python file_organizer.py
text3. For **simple_task_reminder.py**:
- Open Command Prompt / Terminal
- Go to the folder where the script is saved
- Run:
python simple_task_reminder.py
text- (You can change the minutes and message inside the code if you want)

## Example in Action

Files before running:  
![Before sorting](before.png)

Console output when running:  
![Console output](output.png)

After running (files organized):  
![After sorting](after.png)

## Why I built this
These are practice projects to learn file handling, paths, loops and timing — skills useful for real automation work.

Feel free to test them or ask me to add more features!
