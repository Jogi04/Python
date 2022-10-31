import os
import pytube


class Yt_Aio_Downloader:
    def __init__(self):
        self.print_streams = None
        self.is_playlist = None
        self.url = None
        self.destination_path = None
        self.convert = None
        self.get_is_playlist()
        self.get_url()
        self.get_destination_path()
        self.get_convert()
        self.get_print_streams()
        self.download()
        if self.convert:
            self.convert_mp4_to_mp3()

    def get_is_playlist(self):
        if str(input('Is it a playlist you want to download? [y/n]: ')) == 'y':
            self.is_playlist = True
        else:
            self.is_playlist = False

    def get_url(self):
        self.url = str(input('Enter the youtube url: '))

    def get_destination_path(self):
        self.destination_path = str(input('Enter the destination path for the file(s): '))

    def get_convert(self):
        if str(input('Do you want to convert the file to mp3 after downloading? [y/n]: ')) == 'y':
            self.convert = True
        else:
            self.convert = False

    def get_print_streams(self):
        if str(input('Do you want to print the streams? [y/n]: ')) == 'y':
            self.print_streams = True
        else:
            self.print_streams = False

    def download(self):
        """
        downloads video specified by the url to the destination path
        default stream is 140 (stream with the highest audio only quality)
        """
        if self.is_playlist:
            playlist = pytube.Playlist(self.url)
            count = 1
            stream = 140
            append_to_title = str(input('Do you want to append the video title? [Empty for none]: '))
            for i in playlist.video_urls:
                youtube = pytube.YouTube(i)
                streams = youtube.streams
                if self.print_streams:
                    for j in streams:
                        print(j)
                    stream = int(input('Enter itag number: '))
                video = youtube.streams.get_by_itag(stream)
                try:
                    if count >= 10:
                        print(f'Downloading video {count} - {video.title}{append_to_title}.mp4')
                        video.download(self.destination_path, filename=f'{count} - {video.title}{append_to_title}.mp4')
                    else:
                        print(f'Downloading video 0{count} - {video.title}{append_to_title}.mp4')
                        video.download(self.destination_path, filename=f'0{count} - {video.title}{append_to_title}.mp4')
                except FileNotFoundError:
                    video.download(self.destination_path, filename=f'0{count}')
                print('Done')
                count += 1

        else:
            youtube = pytube.YouTube(self.url)
            streams = youtube.streams
            stream = 140
            if self.print_streams:
                for i in streams:
                    print(i)
                stream = int(input('Enter itag number: '))
            change_title = str(input('Do you want to change the title? [Empty for default title]: '))
            video = youtube.streams.get_by_itag(stream)
            if change_title == '':
                print(f'Downloading {video.title}')
                video.download(self.destination_path)
            else:
                print(f'Downloading {change_title}.mp4')
                video.download(self.destination_path, filename=f'{change_title}.mp4')
            print('Done')

    def convert_mp4_to_mp3(self):
        """
        converts mp4 files to mp3 files using ffmpeg
        """
        files = os.listdir(self.destination_path)
        for i in range(len(files)):
            file_name, file_ext = os.path.splitext(files[i])
            print(f'Converting {files[i]}')
            os.system(f'ffmpeg -loglevel quiet -i "{self.destination_path}{files[i]}" "{self.destination_path}{file_name}.mp3"')

        files = os.listdir(self.destination_path)
        for i in range(len(files)):
            file_name, file_ext = os.path.splitext(files[i])
            if file_ext == '.mp4':
                os.remove(f'{self.destination_path}{files[i]}')


if __name__ == '__main__':
    test = Yt_Aio_Downloader()
