#pip install pytube
from pytube import YouTube
#pip install ffmpeg-python
import ffmpeg
import sys
# text = 'https://www.youtube.com/watch?v=G13jBwRaRsU&t=309s'


def extract_audio_from_video(yt_url):
    yt = YouTube(yt_url)
    # https://github.com/pytube/pytube/issues/301
    stream_url = yt.streams[0].url  # Get the URL of the video stream
    # Read audio into memory buffer.
    # Get the audio using stdout pipe of ffmpeg sub-process.
    # The audio is transcoded to PCM codec in WAC container.
    audio, err = (
        ffmpeg
            .input(stream_url)
            .output("pipe:", format='wav',
                    acodec='pcm_s16le')  # Select WAV output format, and pcm_s16le auidio codec. My add ar=sample_rate
            .run(capture_stdout=True)
    )
    # Write the audio buffer to file for testing
    with open('audio.wav', 'wb') as f:
        f.write(audio)

if __name__ == '__main__':
    arg = sys.argv[1:]
    print(arg[0]) #yt video url

    extract_audio_from_video(arg[0])
