import os

try:
    os.mkdir("Files")
    os.chdir("Files/")
except FileExistsError:
    os.chdir("Files/")
print(f"Current working Directory {os.getcwd()}")
f = open("files.txt" "r")

