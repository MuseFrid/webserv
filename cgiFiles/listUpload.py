#!/usr/bin/python3

import os
print("Content-Type: text/plain;charset=utf-8\r\n\r\n") # specifies the type of content to be displayed

def list_files(directory):
    files = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            files.append('"' + filename + '"')
    
    print("[", end="")
    print(",".join(files), end="")
    print("]")

upload_folder = "./upload"
list_files(upload_folder)