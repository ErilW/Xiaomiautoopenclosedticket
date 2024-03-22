
from uisearchpath import*
from filereader import*
from openticket import*
from closeticket import*
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import configparser
# import os
import time
# import schedule
import threading

user_time = 0
open_tiket_objek = 0
close_tiket_objek = 0
last_check = int(time.time())
last_check_2 = int(time.time())
last_update_time = int(time.time())
ticket_is_open = False
config = configparser.ConfigParser()
class MyHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.total_folders = 0
        self.total_files = 0
        self.last_updated_path = False
        self.timer = None
        self.update_path= []

    def reset_timer(self):
        global user_time
        user_time = int(config['USER']['time'])
        self.last_updated_path = True
        if self.timer:
            self.timer.cancel()
        self.timer = threading.Timer(user_time, self.timeout)
        self.timer.start()

    def timeout(self):
        self.last_updated_path = False

    def on_modified(self, event):
        self.update_path.append(event.src_path)

        if event.is_directory:
            self.reset_timer()
         




def get_last_update_time_from_config():
    
    config.read('config.conf')
    user_time = int(config['USER']['time'])  # Ambil nilai time dari bagian [USER] dan ubah menjadi integer
    return user_time


def main ():
    global last_check
    global last_check_2
    global ticket_is_open
    global last_update_time
    root = tk.Tk()
    app = PathSelectorApp(root)
    root.mainloop()

    user_time = get_last_update_time_from_config()
    configpath = configparser.ConfigParser()
    configpath.read('config.conf')
    path_dir = configpath['USER']['path']
    print("User Time:", user_time)
    # Tentukan direktori yang akan dipantau
    path = path_dir
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()


    event_handler.last_updated_time = time.time()
    try:
        
        # current_time = time.time()
            # Timer 1 menit
        # past_time = int(time.time())
        # print(past_time)
        while True:
            millis = int(time.time())
            path_yang_berubah = event_handler.update_path
            if path_yang_berubah:
                path_pertama = path_yang_berubah[0].split(",")[0]
                print("path yang berubah saat ini\n", path_pertama)
            print("path dalam config", path_dir)
            # if(millis - last_check > 3 and ticket_is_open == True):
                

            if millis - last_check > 10 and event_handler.last_updated_path == False and ticket_is_open == False:
                global last_update_time
                last_update_time = int(time.time())
                openticket()
                ticket_is_open= True
                last_check = int(time.time())

            # if millis - last_check > 3 and   and event_handler.last_updated_path == False:  
            #     global last_update_time
            #     last_update_time = int(time.time())
            #     openticket()
            #     


            if  ticket_is_open == True and event_handler.last_updated_path == True:
                print()
                closetiket()
                ticket_is_open = False
                last_check = int(time.time())


                
            
            time.sleep(1)
            
            
                
            
            #ketika tutup tiket dan tidak ada perubahan maka buka tiket
            # if not ticket_is_open and not event_handler.last_updated_path:
            #     print("open tiket1")
            #     openticket()
            #     ticket_is_open = True
                # last_check = int(time.time())
        
            # time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()

   
