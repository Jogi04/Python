import pytube


class YtPlaylistDownloader:
    def __init__(self, url, destination_path=".", stream=140, print_streams=False):
        self.url = url
        self.destination_path = destination_path
        self.stream = stream
        self.print_streams = print_streams
        self.download()

    def download(self):
        playlist = pytube.Playlist(self.url)
        count = 1
        for i in playlist.video_urls:
            youtube = pytube.YouTube(i)
            streams = youtube.streams
            if self.print_streams:
                for j in streams:
                    print(j)
            video = youtube.streams.get_by_itag(self.stream)
            print('Downloading video...')
            try:
                if count >= 10:
                    video.download(self.destination_path, filename=f'{count} - {video.title}')
                else:
                    video.download(self.destination_path, filename=f'0{count} - {video.title}')
            except FileNotFoundError:
                video.download(self.destination_path, filename=f'0{count} -  - Black Sabbath.mp3')
            print('Done')
            count += 1


if __name__ == '__main__':
    test = YtPlaylistDownloader(
        '',
        destination_path='.')
