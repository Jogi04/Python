import pytube


class YtDownloader:
    def __init__(self, url, destination_path=".", stream=140, print_streams=False):
        self.url = url
        self.destination_path = destination_path
        self.stream = stream
        self.print_streams = print_streams
        self.download()

    def download(self):
        youtube = pytube.YouTube(self.url)
        streams = youtube.streams
        if self.print_streams:
            for i in streams:
                print(i)
            self.stream = int(input('Enter itag number: '))
        video = youtube.streams.get_by_itag(self.stream)
        print('Downloading...')
        video.download(self.destination_path)
        print('Done')


if __name__ == '__main__':
    test = YtDownloader('',
                        destination_path='.')
