import time
import os
import sys

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
        regen()

def regen():
    os.system("pdflatex --halt-on-error rapport.tex")

#event_handler = LoggingEventHandler()
observer = Observer()
observer.schedule(Handler(), ".")
observer.start()
try:
    while True:
        cmd=input("cmd:")
        if cmd=="r":
            regen()
        elif cmd == "q":
            quit()
except KeyboardInterrupt:
    observer.stop()
observer.join()
 
