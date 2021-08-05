import pytube
url = str(input('Enter video url: '))

youtube = pytube.YouTube(url)
streams = youtube.streams
for stream in streams:
    print(stream)

which_stream = int(input('Enter itag for stream: '))
video = youtube.streams.get_by_itag(which_stream)
print('Downloading video...')
video.download('/home/jogi/Downloads')
print('Done')
