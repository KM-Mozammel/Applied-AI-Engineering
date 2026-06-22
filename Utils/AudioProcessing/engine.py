import librosa
import matplotlib.pyplot as plt

audio, sr = librosa.load("sample.wav", sr=None)

plt.plot(audio)
plt.title("Audio Waveform")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.show()