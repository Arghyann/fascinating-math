from pydub import AudioSegment
import os

# Set the path to the ffmpeg executable
os.environ["FFMPEG_BINARY"] = r"C:\libraries\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"

# Now you can use pydub to load your mp3 file
mp3_path = r"D:\projects\python\fascinating-math\fourier\musical note extractor\fur elise.mp3"
audio = AudioSegment.from_mp3(mp3_path)

print("Audio loaded successfully!")
