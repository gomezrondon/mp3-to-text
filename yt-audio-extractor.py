from pytube import YouTube
#install ffmpeg-python
import ffmpeg

text = 'https://www.youtube.com/watch?v=G13jBwRaRsU&t=309s'

yt = YouTube(text)

# https://github.com/pytube/pytube/issues/301
stream_url = yt.streams[0].url  # Get the URL of the video stream

# Probe the audio streams (use it in case you need information like sample rate):
#probe = ffmpeg.probe(stream_url)
#audio_streams = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)
#sample_rate = audio_streams['sample_rate']

# Read audio into memory buffer.
# Get the audio using stdout pipe of ffmpeg sub-process.
# The audio is transcoded to PCM codec in WAC container.
audio, err = (
    ffmpeg
    .input(stream_url)
    .output("pipe:", format='wav', acodec='pcm_s16le')  # Select WAV output format, and pcm_s16le auidio codec. My add ar=sample_rate
    .run(capture_stdout=True)
)

# Write the audio buffer to file for testing
with open('audio.wav', 'wb') as f:
    f.write(audio)