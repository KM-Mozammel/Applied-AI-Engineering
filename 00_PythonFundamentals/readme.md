# ML Data Flow
Raw Data
   ↓
dict
   ↓
list
   ↓
numpy array
   ↓
Model
   ↓
float probability


# উদাহরনঃ 
student = {
    "age": 20,
    "study_hours": 5.5
}

features = [20, 5.5]

X = np.array(features)

prediction = 0.89

print(X)
print(prediction)

এখানে:

dict → ছাত্রের তথ্য
list → feature vector
numpy array → model input
float → prediction probability