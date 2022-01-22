import os


def cut_audio():
    start_time = input('Enter the start time in seconds: ')
    end_time = input('Enter the end time in seconds: ')
    audio_file = input('Enter the path of the audio file: ')
    output_file = input('Enter the filename of the output file: ')
    os.system(f'ffmpeg -i {audio_file} -ss {start_time} -to {end_time} -c:a libmp3lame {output_file}')


if __name__ == '__main__':
    cut_audio()
