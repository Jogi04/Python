import os


def merge(video_file, audio_file, output_file):
    os.system(f'ffmpeg -i "{video_file}" -i "{audio_file}" -shortest "{output_file}"')


if __name__ == '__main__':
    merge('video.mp4', 'audio.mp4', 'merged.mp4')
