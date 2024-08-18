import librosa
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.playback import play
import threading

# Load the audio file
audio_path = r'D:\projects\python\fascinating-math\fourier\musical note extractor\fur elise.mp3'
y, sr = librosa.load(audio_path)

# Function to play audio
def play_audio():
    audio = AudioSegment.from_mp3(audio_path)
    play(audio)

# Set up the plot
plt.ion()
fig, ax = plt.subplots()
x = np.arange(0, 1024)
line, = ax.plot(x, np.zeros(1024))

ax.set_ylim([0, 1])
ax.set_xlim([0, 1024])
ax.set_title('Real-time Frequency Spectrum')
ax.set_xlabel('Frequency Bin')
ax.set_ylabel('Magnitude')

# Start audio playback in a separate thread
audio_thread = threading.Thread(target=play_audio)
audio_thread.start()

# Main loop for updating the plot
hop_length = 512
for i in range(0, len(y) - hop_length, hop_length):
    # Compute the short-time Fourier transform
    D = librosa.stft(y[i:i+hop_length], n_fft=2048, hop_length=hop_length)
    
    # Compute the magnitude spectrum
    S = np.abs(D)
    
    # Update the plot
    line.set_ydata(librosa.amplitude_to_db(S[:1024, 0], ref=np.max))
    fig.canvas.draw()
    fig.canvas.flush_events()
    
    plt.pause(hop_length / sr)  # Pause to sync with audio

plt.ioff()
plt.show()