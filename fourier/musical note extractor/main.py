from moviepy.editor import AudioFileClip

# Path to your MP3 file
mp3_path = r"D:\projects\python\fascinating-math\fourier\musical note extractor\fur elise.mp3"

# Load the MP3 file
audio = AudioFileClip(mp3_path)

# Extract audio properties
duration = audio.duration
print(f"Duration: {duration} seconds")

# Get audio samples
samples = audio.to_soundarray()

print(f"Samples: {samples[:10]}")  # Display the first 10 samples
