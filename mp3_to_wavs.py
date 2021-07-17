# importing libraries
from pydub import AudioSegment
import sys


def mp3_to_wavs(file_path, output_path):
    # convert mp3 file to wav
    sound = AudioSegment.from_mp3(file_path)
    sound.export(output_path, format="wav")


if __name__ == '__main__':
    arg = sys.argv[1:]
    print(arg[0])

    mp3_to_wavs(arg[0], arg[1]) #mp3 location