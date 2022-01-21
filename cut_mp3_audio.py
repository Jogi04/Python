from pydub import AudioSegment


def cut_audio(file_path, start_secs, end_secs, output_file_name):
    start_time = start_secs * 1000
    end_time = end_secs * 1000
    audio = AudioSegment.from_mp3(file_path)
    output = audio[start_time:end_time]
    output.export(f'{output_file_name}', format='mp3')


if __name__ == '__main__':
    cut_audio('test.mp3', 0, 0, 'test-cut.mp3')
