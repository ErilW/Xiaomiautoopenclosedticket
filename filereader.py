import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
     def __init__(self):
         self.total_folders = 0
         self.total_files = 0
         self.last_updated_path = None
     def on_modified(self, event):
         self.last_updated_path = event.src_path
         self.update_totals()
     def update_totals(self):
         print(f"Last Updated Path: {self.last_updated_path}")
         

         
if __name__ == "__main__":
     # Tentukan direktori yang akan dipantau
     path =r"C:\Users\eril.sanjaya\Downloads\Drive D Model N6P line 9\Drive D\HUAQIN\AL6860\FAMMI\Slot01_COM22\20240314"
     event_handler = MyHandler()
     observer = Observer()
     observer.schedule(event_handler, path, recursive=True)
     observer.start()
     try:
         while True:
             time.sleep(1)
     except KeyboardInterrupt:
         observer.stop()
     observer.join()

