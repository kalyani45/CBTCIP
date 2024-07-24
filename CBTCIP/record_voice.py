import sounddevice as sd
from scipy.io.wavfile import write

# Sample rate
fs = 44100

# Recording time in seconds
second = 10

print("Recording.....\n")

# Record the voice
record_voice = sd.rec(int(second * fs), samplerate=fs, channels=2)
sd.wait()

# Save the recording as a WAV file
filename = "audio_record.wav"
write(filename, fs, record_voice)

print(f"Recording is done. Please check your folder to listen to the recording: {filename}")
