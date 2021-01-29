import os
import shutil

def make_folder(folder):
    try:
        shutil.rmtree(folder)
        os.mkdir(folder)
    except FileNotFoundError:
        os.mkdir(folder)
    return folder