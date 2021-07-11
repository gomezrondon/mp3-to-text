# importing libraries
import speech_recognition as sr
from pydub.utils import make_chunks
import os
from pydub import AudioSegment

#not al MP3 converters generate a good mp3
# use this: https://ytmp3.cc/youtubemp3/

# a function that splits the audio file into chunks
# and applies speech recognition
def wav_to_text_convertion(path):
    # create a directory to store the audio chunks.
    try:
        os.mkdir('audio_chunks')
    except(FileExistsError):
        pass
    myaudio = AudioSegment.from_file(path, "wav")
    chunk_length_ms = 5000  # pydub calculates in millisec
    chunks = make_chunks(myaudio, chunk_length_ms)  # Make chunks of one sec

    fh = open("recognized.txt", "w+")

    os.chdir('audio_chunks')

    # process each chunk
    for i, chunk in enumerate(chunks):
        chunk_name = "chunk{0}.wav".format(i)
        print("exporting", chunk_name)
        chunk.export(chunk_name, format="wav")


#----------------------------------

        # get the name of the newly created chunk
        # in the AUDIO_FILE variable for later use.
        file = chunk_name
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
            fh.write(chunk_name+" | "+rec + " \n")

        # catch any errors.
        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Could not request results. check your internet connection")



if __name__ == '__main__':
    print('Enter the audio file path')
    path = input()

    # convert mp3 file to wav
    sound = AudioSegment.from_mp3(path)
    sound.export("sound.wav", format="wav")

    wav_to_text_convertion("sound.wav")