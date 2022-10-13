import os
import time
import shutil
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

dir = "C:/Users/Dhruv/Downloads"

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name = os.path.basename(event.src_path)
        path , ext  = os.path.splitext(event.src_path)
        print("Hey," , name, "has been created!")

    def on_modified(self, event):
        name = os.path.basename(event.src_path)
        path , ext  = os.path.splitext(event.src_path)
        print("Hey," , name , "has been modified!")

    def on_moved(self, event):
        name = os.path.basename(event.src_path)
        path , ext  = os.path.splitext(event.src_path)
        print("Hey," , name , "has been moved!")

    def on_deleted(self, event):
        name = os.path.basename(event.src_path)
        path , ext  = os.path.splitext(event.src_path)
        print("Hey," , name , "has been deleted!")
        


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, dir, recursive=True)


# Start the Observer
observer.start()

try :
    while True:
        time.sleep(2)
        print("running...")

    
except KeyboardInterrupt :
    print("Stopped")
    observer.stop()
