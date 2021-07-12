# importing libraries
import speech_recognition as sr
from pydub.utils import make_chunks
import os
from pydub import AudioSegment
import sys


def convert_mp3_to_wavs(file_path, chunk_length_ms = 50000):
    # create a directory to store the audio chunks.
    try:
        os.mkdir('audio_chunks')
    except(FileExistsError):
        pass

    myaudio = AudioSegment.from_file(file_path, "wav")
    # chunk_length_ms = 50000  # pydub calculates in millisec
    chunks = make_chunks(myaudio, chunk_length_ms)

    os.chdir('audio_chunks')
    # create each chunk
    i = 1
    for i, chunk in enumerate(chunks):
        chunk_name = "chunk{0}.wav".format(i)
        print("exporting", chunk_name)
        chunk.export(chunk_name, format="wav")
        i = i + 1

if __name__ == '__main__':
    arg = sys.argv[1:]
    print(arg[0])

    convert_mp3_to_wavs(arg[0], int(arg[1])) #mp3 location