# এখন আমরা AI Mathematics-এর এমন একটি অধ্যায়ে এসেছি যেটা 
Modern Deep Learning, 
Large Language Models (ChatGPT), 
Stable Diffusion, 
BERT, 
GPT
—সবকিছুর হৃদয়।

# আগে পর্যন্ত আমরা শিখেছি

Calculus -> কীভাবে পরিবর্তন হয়

Probability -> অনিশ্চয়তা

Statistics -> ডেটা থেকে জ্ঞান

Optimization -> সেরা সমাধান

Numerical Methods -> কম্পিউটার কীভাবে সমাধান করে

# এখন নতুন প্রশ্ন। "Machine কীভাবে বুঝবে তার Prediction কতটা ভালো?" এই প্রশ্ন থেকেই Information Theory-এর জন্ম।

Information Theory (জন্ম) ইতিহাস: ১৯৪৮ সালে একজন বিজ্ঞানী, Claude Shannon একটি বড় প্রশ্ন করলেন। "Information আসলে কী?" তিনি Telephone কোম্পানিতে কাজ করতেন। তখন সমস্যা ছিল, Sender -> Telephone Line -> Receiver মাঝখানে Noise থাকত। 

তিনি জানতে চাইলেন "একটি Message-এর মধ্যে কত Information আছে?" 
এবং "কম Bit ব্যবহার করে Message পাঠানো যায়?" এই গবেষণা থেকেই Information Theory-এর জন্ম।

আজ Internet - ZIP Compression - JPEG - MP3 - ChatGPT - LLM - Deep Learning সবই Information Theory-এর উপর দাঁড়িয়ে।

# পুরো Information Theory Roadmap
Information Theory
│
├── Entropy
│
├── Cross Entropy Loss
│
└── KL Divergence

# পুরো Information Theory Evolution
Communication Problem (Claude Shannon)
                │
                ▼
          Entropy
                │
                ▼
Measure Uncertainty
                │
                ▼
Machine Learning
                │
                ▼
Cross Entropy Loss
                │
                ▼
Gradient Descent
                │
                ▼
Neural Networks Learn
                │
                ▼
KL Divergence
                │
                ▼
Compare Probability Distributions
                │
                ▼
Generative AI
                │
                ▼
ChatGPT

# এক লাইনে মনে রাখোঃ

| Concept                | মূল প্রশ্ন                                       |
| ---------------------- | ------------------------------------------------ |
| **Information Theory** | তথ্য (Information) কীভাবে পরিমাপ করব?            |
| **Entropy**            | একটি ঘটনার মধ্যে কতটা অনিশ্চয়তা বা তথ্য আছে?    |
| **Cross Entropy Loss** | Model-এর Prediction বাস্তব উত্তর থেকে কতটা দূরে? |
| **KL Divergence**      | দুটি Probability Distribution কতটা ভিন্ন?        |

Entropy -> "আমি কতটা অবাক হব?"
Cross Entropy -> "Model কতটা ভুল করেছে?"
KL Divergence -> "দুটি বিশ্বাস (Probability Distribution) কতটা আলাদা?"