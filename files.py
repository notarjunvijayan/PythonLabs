import os

try:
    os.mkdir("Files")
    os.chdir("Files/")
except FileExistsError:
    os.chdir("Files/")
print(f"Current working Directory {os.getcwd()}")
file = open("files.txt", "a")
if file:
    print("File created/opened successfully")
string = input("Enter the input for the string: ")
file.write(string)
print("Entered string written successfully: ")
file.close()
file = open("files.txt", "r")
filetxt = file.read()
print(filetxt)





