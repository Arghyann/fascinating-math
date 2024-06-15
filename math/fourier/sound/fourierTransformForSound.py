import matplotlib.pyplot as plt
import numpy as np
import librosa


audio_file=r"D:\projects\python\fascinating-math\math\fourier\sound\file_example_WAV_1MG.wav"
y, sr = librosa.load(audio_file, sr=None)
N=len(y)

amplitudes=np.fft.fft(y)
frequencies=np.fft.fftfreq(N,d=1/sr)
#getting the top five frequencies

print(amplitudes)
plt.plot(frequencies, np.abs(amplitudes))
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()