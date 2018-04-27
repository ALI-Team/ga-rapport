import time
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
class Handler(FileSystemEventHandler):
    def dispatch(self, event):
        if event.is_directory:
            return
        if event.src_path != "./rapport.tex":
            return
        print(event)
        print("REGEN")
        os.system("pdflatex --halt-on-error rapport.tex")

#event_handler = LoggingEventHandler()
observer = Observer()
observer.schedule(Handler(), ".")
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
 
