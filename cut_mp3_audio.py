import os


def cut_audio(start_time, end_time, audio_file, output_file):
    os.system(f'ffmpeg -i "{audio_file}" -ss {start_time} -to {end_time} -c:a libmp3lame "{output_file}"')


if __name__ == '__main__':
    cut_audio(0, 356, '/mnt/nas/johannes/Music/Various Artists/Live/Metallica/No Leaf Clover - Metallica - Live Cologne, Germany, June 13, 2019.mp3', '/mnt/nas/johannes/Music/Various Artists/Live/Metallica/cut.mp3')
