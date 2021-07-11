
# importing libraries
import speech_recognition as sr
from pydub.utils import make_chunks
import os
from pydub import AudioSegment
import sys

#example:python convert_wav_to_text.py <PATH>\audio_chunks\chunk8.wav

# a function that splits the audio file into chunks
# and applies speech recognition
def wav_to_text_convertion(file_url):
    try:
        os.mkdir('text_chunks')
    except(FileExistsError):
        pass
#----------------------------------
    file_path = os.path.dirname(file_url)
    only_name_file = os.path.basename(os.path.splitext(file_url)[0])
    file = os.path.basename(file_url)
    fh = open("text_chunks/"+only_name_file+".txt", "w+")

    os.chdir(file_path)
    # get the name of the newly created chunk
    # in the AUDIO_FILE variable for later use.

    print("Processing chunk " + file)

    # create a speech recognition object
    r = sr.Recognizer()

    # recognize the chunk
    with sr.AudioFile(file) as source:
        # remove this if it is not working
        # correctly.
        # r.adjust_for_ambient_noise(source)
        audio_listened = r.listen(source)

    try:
        # try converting it to text
        rec = r.recognize_google(audio_listened)
        # write the output to the file.
        fh.write(rec + " \n")

    # catch any errors.
    except sr.UnknownValueError:
        print("Could not understand audio")

    except sr.RequestError as e:
        print("Could not request results. check your internet connection")



if __name__ == '__main__':
    arg = sys.argv[1:]
    print(arg[0])
    wav_to_text_convertion(arg[0])