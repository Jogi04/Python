import os


def merge():
    video_file = input('Enter the path of the video file: ')
    audio_file = input('Enter the path of the audio file: ')
    output_file = input('Enter the filename of the output file: ')
    os.system(f'ffmpeg -i "{video_file}" -i "{audio_file}" -shortest {output_file}.mp4')


if __name__ == '__main__':
    merge()
