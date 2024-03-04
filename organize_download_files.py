import os
import collections
import time
from pprint import pprint

EXT_AUDIO = ["mp3", "wav", "raw", "wna", "mid", "midi"]
EXT_VIDEO = ["mp4", "mpg", "mpeg", "avi", "mov", "flv", "mkv", "mwv", "m4v", "h264"]
EXT_IMAGES = ["jpeg", "png", "gif", "tiff", "psd", "jpg", "svg", "tif", "bmp"]
EXT_DOCS = ["docx", "pdf", "txt", "xls", "xlsx", "csv", "doc", "ods", "html", "odt", "tex", "ppt", "pptx", "log", "PDF", "DOCX"]
EXT_COMPRESSION = ["zip", "z", "7z", "rar", "tar", "gz", "rpm", "pkg", "deb"]
EXT_INSTALLATION = ["exe", "dmb", "iso", "msi"]
EXT_CODE = ["py", "java", "js", "css", "html", "ipynb", "xml", "cs", "jar", "asm"]

DST_DIRS = ["Music", "Videos", "Pictures", "Documents", "Application", "ZipFiles", "Coding", "Other"]
# This is my dir for Documents - Change it to yours or another dir if you want to.
BASE_NAME = r"C:\Users\yuviv\Documents"

for d in DST_DIRS :
    dir_path = os.path.join(BASE_NAME, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# This is my dir for Downloads - Change it to yours.
DOWNLOADS_PATH = r"C:\Users\yuviv\Downloads"
files_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)

for file_name in files_list:
    if file_name[0] != '.':
        file_ext = file_name.split(".")[-1]
        files_mapping[file_ext].append(file_name)

for f_ext, f_list in files_mapping.items():

    for file in f_list:
        source_file = os.path.join(DOWNLOADS_PATH, file)
        destination_folder = ""

        if f_ext in EXT_INSTALLATION:
            destination_folder = os.path.join(BASE_NAME, "Application")
        elif f_ext in EXT_IMAGES:
            destination_folder = os.path.join(BASE_NAME, "Pictures")
        elif f_ext in EXT_DOCS:
            destination_folder = os.path.join(BASE_NAME, "Documents")
        elif f_ext in EXT_AUDIO:
            destination_folder = os.path.join(BASE_NAME, "Music")
        elif f_ext in EXT_COMPRESSION:
            destination_folder = os.path.join(BASE_NAME, "ZipFiles")
        elif f_ext in EXT_VIDEO:
            destination_folder = os.path.join(BASE_NAME, "Videos")
        elif f_ext in EXT_CODE:
            destination_folder = os.path.join(BASE_NAME, "Coding")
        else:
            destination_folder = os.path.join(BASE_NAME, "Other")

        destination_file = os.path.join(destination_folder, file)

        if os.path.exists(destination_file):
            filename, file_extension = os.path.splitext(file)
            suffix = 1
            new_filename = f"{filename}_duplicate{suffix}{file_extension}"
            while os.path.exists(os.path.join(destination_folder ,new_filename)):
                suffix += 1
                new_filename = f"{filename}_duplicate{suffix}{file_extension}"

            destination_file = os.path.join(destination_folder, new_filename)

        os.rename(source_file, destination_file)

