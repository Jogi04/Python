import os

path = ""
files = os.listdir(path)

for i in range(len(files)):
    file_name, file_ext = os.path.splitext(files[i])
    os.rename(path + files[i], f"{path}{file_name}.mp3")
