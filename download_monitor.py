# Made by yuval24 - Yuval Shaham
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess


class DownloadHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.processed_files = set()

    def on_created(self, event):
        # When a new file is created in the directory
        self.process_file(event.src_path)

    def on_modified(self, event):
        # When a file is modified in the directory
        self.process_file(event.src_path)

    def process_file(self, file_path):
        # Check if the file extension is no longer .tmp
        if not file_path.endswith(".tmp") and file_path not in self.processed_files:
            # This delay is here because it lets the antivirus work properly
            time.sleep(2)
            file_name = os.path.basename(file_path)
            file_extension = os.path.splitext(file_name)[1]
            file_type = file_extension[1:]  # Remove the leading dot

            # Runs a script which organizes the downloads folder to specific folders according to their extension type
            # Modify the path according to yours
            subprocess.run(["python", r"C:\Users\yuviv\Documents\ProjectsFile\PythonAutomationScript\organize_download_files.py"])

            # Add the file to the set of processed files
            # so that this won't be called multiple times
            self.processed_files.add(file_path)


if __name__ == "__main__":
    # Directory to monitor
    # This is my directory for downloads - change it to yours ------
    directory_to_watch = r"C:\Users\yuviv\Downloads"

    # Create an observer and associate it with the handler
    observer = Observer()
    observer.schedule(DownloadHandler(), path=directory_to_watch, recursive=False)

    # Start the observer
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop the observer on keyboard interrupt
        observer.stop()

    # Wait until the observer thread completes its work
    observer.join()
