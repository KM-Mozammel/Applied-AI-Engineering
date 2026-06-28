import librosa
import numpy as np

def extract_features(file_path):
    # অডিও লোড করা
    y, sr = librosa.load(file_path, sr=None)
    # MFCC ফিচার বের করা
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    # গড় মান নেওয়া (সাধারণীকরণের জন্য)
    mfcc_mean = np.mean(mfcc, axis=1)
    return mfcc_mean

def compare_voice(file1, file2, threshold=50):
    f1 = extract_features(file1)
    f2 = extract_features(file2)
    # ইউক্লিডিয়ান দূরত্ব বের করা
    distance = np.linalg.norm(f1 - f2)
    print("Distance:", distance)
    if distance < threshold:
        print("✅ Same person (likely)")
    else:
        print("❌ Different person")

# উদাহরণ ব্যবহার
compare_voice("voice1.wav", "voice2.wav")
