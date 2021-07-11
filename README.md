# mp3-to-text
Convert a MP3 file to text 

### clone repo
### cd to repo
### import libreries speech_recognition, pydub
python -m pip install SpeechRecognition
pip install pydub
### also needs to install FFmpeg
go to https://ffmpeg.org/download.html
download a tz file (ffmpeg-4.4-full_build.7z) unzip it
configure the "ffmpeg-PATH/bin" in the class path (for windows) 

### to run execute: 
python main.py

### the program will generate  a file "recognized.txt" with the transcriptions.
