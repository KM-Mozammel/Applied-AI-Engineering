import numpy as np
from pypdf import PdfReader

pdf_path = "sample.pdf"
reader = PdfReader(pdf_path)

text = ""
for page in reader.pages:
    text += page.extract_text() or ""
    
print ("Extracted Text:\n", text[:300])

char_array = np.array([ord(c) for c in text])

print("\nNumpy Array Shape:", char_array.shape)
print("First 50 values:", char_array[:50])