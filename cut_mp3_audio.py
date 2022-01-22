import os


def cut_audio(start_time, end_time, audio_file, output_file):
    os.system(f'ffmpeg -i "{audio_file}" -ss {start_time} -to {end_time} -c:a libmp3lame "{output_file}"')


if __name__ == '__main__':
    cut_audio(10, 20, 'test.mp3', 'cut.mp3')
