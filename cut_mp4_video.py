import os


def cut_video(start_time, end_time, video_file, output_file):
    os.system(f'ffmpeg -i "{video_file}" -ss {start_time} -to {end_time} -c copy "{output_file}"')


if __name__ == '__main__':
    cut_video(10, 20, 'video.mp4', 'cut.mp4')
