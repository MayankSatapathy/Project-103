import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Manoj/Downloads"
to_dir = "D:/C102"

list_of_files = os.listdir(from_dir)

class FileMovementHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_modified(self, event):
        print(f"{event.src_path} has been succesfully modified!")

    def on_moved(self, event):
        print(f"{event.src_path} has been moved!")   

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")   

for file_name in list_of_files:
    name,ext = os.path.splitext(file_name)
    
    if(ext == ""):
        continue
    if ext in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + 'Document_Files'
        path3 = to_dir + "/" + "Document_Files" + "/" + file_name
        
        if os.path.exists(path2):
            print("Moving " + file_name + ".............")
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving " + file_name + "............. to " + path3 )
            shutil.move(path1,path3)    

# Initialise Event Handler Class
event_handler = FileMovementHandler()

# Initialise Observer
observer = Observer()

# Schedule Observer
observer.schedule(event_handler, from_dir, recursive = True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()    