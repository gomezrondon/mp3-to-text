import os
import wave



with wave.open("chunk23.wav", "rb") as wave_file:
    frame_rate = wave_file.getframerate()
    print(frame_rate)