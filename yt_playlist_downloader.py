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
        for i in playlist.video_urls:
            youtube = pytube.YouTube(i)
            streams = youtube.streams
            if self.print_streams:
                for j in streams:
                    print(j)
            video = youtube.streams.get_by_itag(self.stream)
            print('Downloading video...')
            video.download(self.destination_path)
            print('Done')


if __name__ == '__main__':
    test = YtPlaylistDownloader(
        'https://www.youtube.com/watch?v=xeK1E1HaMdY&list=OLAK5uy_k4yeBNbCJLDBeqj_QsTlpRoncOxmGLQDo',
        destination_path='/mnt/nas/johannes/Music/Various Artists')
