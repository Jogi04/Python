import os

path = ""

files = os.listdir(path)
for i in range(len(files)):
    file_name, file_ext = os.path.splitext(files[i])
    os.system(f'ffmpeg -i "{path}{files[i]}" "{path}{file_name}.mp3"')

files = os.listdir(path)
for i in range(len(files)):
    file_name, file_ext = os.path.splitext(files[i])
    if file_ext == '.mp4':
        os.remove(f'{path}{files[i]}')
