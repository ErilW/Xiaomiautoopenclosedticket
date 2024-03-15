import os
from pathlib import Path
import re

def f_path(path):
    home = str(Path.home())
    path_reg = "^"+re.sub("[^/]+$","", home) + "[^/]+"
    return re.sub(path_reg,home,path)

file = open("D:\Rafles\Xauto openclose ticket Xiaomi\sampleread.txt", "r")
print(file.read())

oldpath = "D:\Rafles\Xauto openclose ticket Xiaomi\sampleread.txt"
newpath = f_path(oldpath)


