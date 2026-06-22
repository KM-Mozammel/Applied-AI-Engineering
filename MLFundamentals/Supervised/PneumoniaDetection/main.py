import numpy as np
from PIL import Image

normal_path = "normal.jpg"
pneumonia_path = "Pneumonia.jpeg"

img_normal = Image.open(normal_path).convert("L")
img_pneumonia = Image.open(pneumonia_path).convert("L")

# Convert images into raw NumPy pixel matrices
arr_normal = np.array(img_normal)
arr_pneumonia = np.array(img_pneumonia)

print("--- Data Inspection ---")
print(f"Normal X-ray Matrix Shape:    {arr_normal.shape}")
print(f"Pneumonia X-ray Matrix Shape: {arr_pneumonia.shape}")

# STEP 2: FEATURE EXTRACTION (Compressing data for our basic model)
# We use NumPy to calculate the average brightness of each image
brightness_normal = np.mean(arr_normal)
brightness_pneumonia = np.mean(arr_pneumonia)

print(f"\nExtracted Feature - Normal Avg Brightness:    {brightness_normal:.2f}")
print(f"Extracted Feature - Pneumonia Avg Brightness: {brightness_pneumonia:.2f}")

# STEP 3: THE SUPERVISED TRAINING PHASE (The Machine "Learns")
# We group our training features (X) and their corresponding labels (y)
# Label 0 = Healthy/Normal, Label 1 = Sick/Pneumonia
X_train = np.array([brightness_normal, brightness_pneumonia])
y_train = np.array([0, 1])

# Our Supervised Learning Algorithm:
# Instead of hardcoding 120.0, the computer calculates the exact mid-point
# between the normal and pneumonia data points to establish a decision boundary.
learned_threshold = np.mean(X_train)

print("\n--- Training Complete ---")
print(f"The model analyzed X_train & y_train and learned the threshold: {learned_threshold:.2f}")

# =====================================================================
# STEP 4: PREDICTION FUNCTION USING THE LEARNED MODEL
# =====================================================================
def predict_pneumonia_ml(image_array, threshold=learned_threshold):
    """
    Takes an unseen X-ray image array, extracts its mean brightness,
    and classifies it based on the threshold learned during training.
    """
    # 1. Extract feature from the input image
    avg_brightness = np.mean(image_array)
    
    # 2. Apply the learned decision boundary
    if avg_brightness > threshold:
        return f"Prediction: PNEUMONIA (Brightness: {avg_brightness:.2f} > Threshold: {threshold:.2f})"
    else:
        return f"Prediction: NORMAL (Brightness: {avg_brightness:.2f} <= Threshold: {threshold:.2f})"

# =====================================================================
# STEP 5: TESTING THE MODEL
# =====================================================================
print("\n--- Running Model Predictions ---")
print("Testing with Normal Image file:")
print(predict_pneumonia_ml(arr_normal))

print("\nTesting with Pneumonia Image file:")
print(predict_pneumonia_ml(arr_pneumonia))