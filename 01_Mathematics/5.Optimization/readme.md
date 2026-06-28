এটি সম্ভবত Machine Learning-এর সবচেয়ে গুরুত্বপূর্ণ অধ্যায়।
এখন পর্যন্ত তুমি শিখেছো—
Mathematics
│
├── Calculus → Change
├── Probability → Uncertainty
├── Statistics → Data Analysis

কিন্তু একটি প্রশ্ন এখনো বাকি আছে।
"Machine কীভাবে শেখে?"
এই প্রশ্ন থেকেই Optimization-এর জন্ম।

# Optimization (জন্ম): ইতিহাস
প্রাচীনকাল থেকেই মানুষ একটি প্রশ্নের উত্তর খুঁজছিল—
"অনেকগুলো সম্ভাব্য সমাধানের মধ্যে সবচেয়ে ভালো সমাধান কোনটি?"

উদাহরণ:

সবচেয়ে ছোট রাস্তা কোনটি?
সবচেয়ে কম খরচে বাড়ি বানানো যায় কীভাবে?
সবচেয়ে বেশি লাভ কীভাবে হবে?

এই ধরনের প্রশ্ন থেকেই Optimization-এর জন্ম। Machine Learning-এ একই প্রশ্ন দাঁড়ায়— "কোন Weight-গুলো হলে Model সবচেয়ে কম ভুল করবে?"

Optimization
│
├── Convexity
│
├── Lagrange Multipliers
│
└── Stochastic Gradient Descent
        │
        ├── Mini Batch SGD
        ├── Momentum
        ├── AdaGrad
        ├── RMSProp
        └── Adam

# Optimization Evolution

Optimization
│
├── Convexity
│      │
│      ▼
│  সহজে Global Minimum খুঁজে পাওয়া
│
├── Lagrange Multipliers
│      │
│      ▼
│  Constraint সহ Optimization
│
└── Gradient Descent
        │
        ▼
 Stochastic Gradient Descent
        │
        ├── Mini Batch
        ├── Momentum
        ├── AdaGrad
        ├── RMSProp
        └── Adam

#####
| Concept                               | মূল প্রশ্ন                                                              |
| ------------------------------------- | ----------------------------------------------------------------------- |
| **Optimization**                      | সবচেয়ে ভালো সমাধান কী?                                                 |
| **Convexity**                         | সমস্যাটির কি একটি নিশ্চিত Global Minimum আছে?                           |
| **Lagrange Multipliers**              | শর্ত (Constraint) মেনে কীভাবে সর্বোত্তম সমাধান পাব?                     |
| **Gradient Descent**                  | Loss কমানোর জন্য কোন দিকে এগোব?                                         |
| **Stochastic Gradient Descent (SGD)** | পুরো Dataset না দেখে দ্রুত কীভাবে শিখব?                                 |
| **Mini-Batch SGD**                    | অল্প Data-এর Batch ব্যবহার করে স্থিতিশীলভাবে কীভাবে শিখব?               |
| **Momentum**                          | Gradient-এর দিক ধরে রেখে দ্রুত এগোব কীভাবে?                             |
| **AdaGrad**                           | প্রতিটি Parameter-এর জন্য আলাদা Learning Rate কীভাবে দেব?               |
| **RMSProp**                           | AdaGrad-এর Learning Rate খুব ছোট হয়ে যাওয়ার সমস্যা কীভাবে সমাধান করব? |
| **Adam**                              | Momentum + RMSProp মিলিয়ে সবচেয়ে কার্যকর Optimizer কীভাবে পাব?        |
