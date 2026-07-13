import math

for x in range(10):
    print(round(math.sin(x), 2))
    
# Sound is a sine wave

# This oscillation creates:

# Sound
# Radio signals
# WiFi
# Image compression
# Fourier transforms


# Generate a Pure Tone
import numpy as np
import sounddevice as sd

# Parameters
duration = 2.0   # seconds
freq = 440.0     # Hz (A4 note)
sample_rate = 44100

# Time axis
t = np.linspace(0, duration, int(sample_rate*duration), endpoint=False)

# Generate sine wave
wave = 0.5 * np.sin(2*np.pi*freq*t)

# Play sound
sd.play(wave, sample_rate)
sd.wait()


# Major Scale
import numpy as np
import sounddevice as sd

# Parameters
sample_rate = 44100
duration = 0.5  # seconds per note

# Frequencies for C major scale (C4 to C5)
frequencies = [261.63, 293.66, 329.63, 349.23,
               392.00, 440.00, 493.88, 523.25]  # Up
frequencies += frequencies[::-1]  # Down

# Generate and play each note
for freq in frequencies:
    t = np.linspace(0, duration, int(sample_rate*duration), endpoint=False)
    wave = 0.5 * np.sin(2*np.pi*freq*t)
    sd.play(wave, sample_rate)
    sd.wait()
    
    
# Generate Human Voice
from gtts import gTTS
import os

# Text to speak
text = "C major scale up and down"

# Generate speech
tts = gTTS(text=text, lang='en')
tts.save("scale.mp3")

# Play the audio
os.system("start scale.mp3")  # Windows



"""
===========================================================
Waves and Signal Processing
(তরঙ্গ ও সিগন্যাল প্রসেসিং)
===========================================================

Structure:
01_Introduction
02_WhyThisConceptExistsInRealtionTohistory
03_RealLifeIntuition
04_Definition
05_Formula
06_Derivation (How the formula comes)
07_InternalWorking / Visualization
08_Examples
09_CommonMistakes
10_Exercises
11_AIUsage (Machine Learning / AI)
===========================================================
"""

# ===========================================================
# 01_Introduction
# ===========================================================

"""
এখন পর্যন্ত আমরা শিখেছি

✔ Unit Circle

✔ Sine

✔ Cosine

✔ Tangent

✔ Rotation

এখন প্রশ্ন হলো,

Sine এবং Cosine
বাস্তবে কোথায় ব্যবহৃত হয়?

উত্তর:

প্রায় সব ধরনের

Wave (তরঙ্গ)

এবং

Signal (সিগন্যাল)

এ।

যেমন,

✔ শব্দ (Sound)

✔ রেডিও সিগন্যাল

✔ WiFi

✔ Bluetooth

✔ ECG

✔ EEG

✔ Image Compression

সবকিছুর পেছনে

Wave Mathematics

কাজ করে।

আর Wave-এর ভিত্তি হলো

Sine এবং Cosine।
"""

# ===========================================================
# 02_WhyThisConceptExistsInRealtionTohistory
# ===========================================================

"""
প্রাচীনকাল থেকেই মানুষ

তরঙ্গ (Wave)

পর্যবেক্ষণ করেছে।

যেমন,

✔ সমুদ্রের ঢেউ

✔ শব্দ

✔ আলো

✔ কম্পন

পরে,

Joseph Fourier

দেখান,

যে কোনো জটিল Signal

অনেকগুলো

Sine এবং Cosine Wave

এর সমষ্টি হিসেবে প্রকাশ করা যায়।

এটি

Fourier Analysis

নামে পরিচিত।

বর্তমানে,

Communication,

Audio Processing,

AI,

Medical Devices,

Computer Vision

সবখানে এটি ব্যবহৃত হয়।
"""

# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
ধরো,

একটি পুকুরে
পাথর ছুঁড়ে দিলে,

বৃত্তাকার ঢেউ তৈরি হয়।

আবার,

গিটার বাজালে,

বাতাসে শব্দ তরঙ্গ ছড়ায়।

আবার,

WiFi Router

তোমার মোবাইলে
তথ্য পাঠায়।

এসবই Signal।

Wave হলো

তথ্য বহন করার একটি মাধ্যম।

আর Signal Processing হলো

এই Signal-কে

বিশ্লেষণ,

পরিবর্তন,

এবং

ব্যবহার করার বিজ্ঞান।
"""

# ===========================================================
# 04_Definition
# ===========================================================

"""
Wave (তরঙ্গ)

হলো

একটি পুনরাবৃত্ত (Periodic)

Pattern

যা সময় বা স্থানের সাথে পরিবর্তিত হয়।

------------------------------------

Signal

হলো

তথ্য বহনকারী Wave।

------------------------------------

Signal Processing

হলো

Signal

কে

Analyze,

Filter,

Transform,

এবং

Interpret

করার প্রক্রিয়া।
"""

# ===========================================================
# 05_Formula
# ===========================================================

"""
সবচেয়ে মৌলিক Wave Formula

y = A sin(ωt + φ)

------------------------------------

যেখানে,

A = Amplitude

ω = Angular Frequency

t = Time

φ = Phase Shift

------------------------------------

Cosine Wave

y = A cos(ωt + φ)

------------------------------------

Frequency

f

=

Number of Cycles per Second

------------------------------------

Angular Frequency

ω = 2πf
"""

# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Unit Circle থেকে

একটি Point

ঘুরছে।

ধরি,

Radius = A

Angle = θ

তাহলে,

x = A cosθ

y = A sinθ

এখন,

θ

সময়ের সাথে পরিবর্তিত হয়।

ধরি,

θ = ωt

তাহলে,

y = A sin(ωt)

এইভাবেই

Sine Wave

তৈরি হয়।

অর্থাৎ,

একটি Rotating Point-এর

Vertical Projection

হলো

Sine Wave।

এ কারণেই

Unit Circle

থেকে

Signal Processing

শুরু হয়।
"""

# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Unit Circle

           ●
        .-' '-.
      .'       '.
     |     O----●
      '.       .'
        '-._.-'

Point Rotate করছে

↓

Vertical Position নিচ্ছি

↓

Time-এর সাথে Plot করছি

↓

      /\      /\
     /  \    /  \
    /    \  /    \
---/------\/------\-----

↓

Sine Wave

------------------------------------

Amplitude

Wave কত উঁচু হবে

------------------------------------

Frequency

Wave কত দ্রুত পুনরাবৃত্ত হবে

------------------------------------

Phase

Wave কোথা থেকে শুরু হবে
"""

# ===========================================================
# 08_Examples
# ===========================================================

import math

print("=" * 60)
print("Example 1 : Simple Sine Wave")
print("=" * 60)

A = 1
f = 1

for t in range(6):
    y = A * math.sin(2 * math.pi * f * t)
    print(f"t={t}, y={round(y,4)}")

print()

print("=" * 60)
print("Example 2 : Higher Frequency")
print("=" * 60)

A = 1
f = 3

for t in range(6):
    y = A * math.sin(2 * math.pi * f * t)
    print(f"t={t}, y={round(y,4)}")

print()

print("=" * 60)
print("Example 3 : Audio Signal")
print("=" * 60)

A = 2
f = 2

for t in range(5):
    y = A * math.sin(2 * math.pi * f * t)
    print(f"t={t}, y={round(y,4)}")

"""
Output

Wave Values

t=0, y=0

t=1, y=0

t=2, y=0

...

(বাস্তবে ছোট Time Step ব্যবহার করা হয়,
যেমন 0.01 sec)
"""

# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
❌ ভুল ১

Amplitude

এবং

Frequency

গুলিয়ে ফেলা।

Amplitude

→ উচ্চতা

Frequency

→ গতি

------------------------------------

❌ ভুল ২

ω

এবং

f

এক মনে করা।

সঠিক

ω = 2πf

------------------------------------

❌ ভুল ৩

সব Signal

Sine Wave

মনে করা।

বাস্তবে অনেক Signal
জটিল Wave-এর সমষ্টি।

------------------------------------

❌ ভুল ৪

Phase Shift

উপেক্ষা করা।

------------------------------------

❌ ভুল ৫

Unit Circle

এবং

Wave-এর সম্পর্ক না বোঝা।
"""

# ===========================================================
# 10_Exercises
# ===========================================================

"""
১।

Amplitude = 3

Frequency = 2

এর Wave Equation লেখো।

----------------------------------

২।

ω = 10

হলে

Frequency বের করো।

----------------------------------

৩।

নিজের

sine_wave()

Function লেখো।

----------------------------------

৪।

User থেকে

Amplitude

এবং

Frequency

Input নিয়ে

Wave Value Print করো।

----------------------------------

৫।

0 থেকে 2π

পর্যন্ত

Sine Value Print করো।

----------------------------------

৬।

Cosine Wave-এর জন্যও
একই Program লেখো।
"""

# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
Wave এবং Signal Processing
AI-এর অনেক ক্ষেত্রের ভিত্তি।

১।

Speech Recognition

মানুষের কণ্ঠ বিশ্লেষণ।

----------------------------------

২।

Voice Biometrics

Speaker Identification।

----------------------------------

৩।

Music AI

Beat Detection,

Pitch Detection,

Audio Generation।

----------------------------------

৪।

Computer Vision

Image Compression

(JPEG)

Fourier Transform ব্যবহার করে।

----------------------------------

৫।

Medical AI

ECG,

EEG,

Heart Signal Analysis।

----------------------------------

৬।

Radar এবং Sonar

Signal Interpretation।

----------------------------------

৭।

Deep Learning

Transformer Positional Encoding

Sine এবং Cosine ব্যবহার করে।

----------------------------------

৮।

Generative AI

Audio Generation,

Music Generation,

Speech Synthesis।

----------------------------------

৯।

Fourier Transform

যে কোনো Signal

↓

Frequency Components

এ ভেঙে ফেলে।

এটি Signal Processing-এর
সবচেয়ে গুরুত্বপূর্ণ ধারণা।

----------------------------------

তুমি যেহেতু

Voice Biometrics,

Audio AI,

Music AI,

Signal Processing

শিখছো,

তাই এই অধ্যায়টি
তোমার জন্য অত্যন্ত গুরুত্বপূর্ণ।

এর পরে শেখার আদর্শ ক্রম হবে:

1. FourierTransform.py
2. FrequencyDomain.py
3. SamplingRate.py
4. AudioSignals.py
5. DigitalSignalProcessing.py
6. FFT.py
7. VoiceBiometricsMath.py
"""

# ===========================================================
# End of File
# ===========================================================