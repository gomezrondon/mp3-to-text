#pip install ibm_watson
#pip install ibm-watson
#pip install ibm-cloud-sdk-core
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import subprocess
import os

apikey = '9E****m2'
url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/08***53'

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator = authenticator)
stt.set_service_url(url)

#------------------------
try:
    os.mkdir('audio_chunks')
except(FileExistsError):
    pass

#split mp3 in segment of 5 minutes
command = 'ffmpeg -i yt-video.mp3 -f segment -segment_time 300 -c copy audio_chunks/%03d.mp3'
subprocess.call(command, shell=True)

#------------------------

files = []
for filename in os.listdir('./audio_chunks'):
    if filename.endswith(".mp3"):
        files.append(filename)
        # print(filename)

#------------------------
#https://cloud.ibm.com/apidocs/speech-to-text?code=python
results= []
for filename in files:
    with open('./audio_chunks/'+filename, 'rb') as f:
        res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_BroadbandModel',inactivity_timeout=360).get_result()
        results.append(res)
        print(res)