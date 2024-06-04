import librosa
import numpy as np
import matplotlib.pyplot as plt
from fastfourierTransform import fourier

# Load the audio signal
audio_file = r'D:\projects\python\fascinating-math\math\fourier\sound\file_example_WAV_1MG.wav'
y, sr = librosa.load(audio_file, sr=None)  # y is the audio signal, sr is the original sampling rate

#N can be thought of as sr*t
magnitudes=fourier(y)
frequencies= [2*np.pi*n for n in range(-len(y)//2,len(y))]

plt.plot(frequencies, np.abs(magnitudes))
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency (radians/sample)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()