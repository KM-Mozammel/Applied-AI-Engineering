import librosa
import numpy as np
import soundfile as sf

vocal, sr = librosa.load("count.wav", sr=None)
kick, _ = librosa.load("Kick.wav")

tempo, beats = librosa.beat.beat_track(y=vocal, sr=sr)

print("Tempo:", tempo)

output = vocal.copy()

for beat in beats:
    start = librosa.frames_to_samples(beat)
    
    end = min(
        start + len(kick),
        len(output)
    )
    
    output[start:end] += kick[:end-start]

output = output / np.max(np.abs(output))

sf.write(
    "vocal_with_kick.wav",
    output,
    sr
)

print("Exported: vocal_with_kick.wav")