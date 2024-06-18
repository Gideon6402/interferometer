import os

def mkdir(filename):
    if not os.path.isdir(filename):
        os.system(f"mkdir {filename}")