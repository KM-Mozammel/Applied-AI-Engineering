# SGD Variants (Evolution): Gradient Descent-এরও সমস্যা ছিল। তাই একে একে নতুন Algorithm তৈরি হলো।

# Mini Batch SGD: 
# সমস্যা: একটি Sample -> Noise বেশি।
# সমাধান: একসাথে 32-64-128 Sample ব্যবহার করো।

batch_size = 32


# Momentum: 
    # সমস্যা: Gradient এদিক-ওদিক লাফায়।
    # সমাধান: আগের Direction মনে রাখো।
    # Visualization: Without Momentum -> ↙↗↘↖↙↗ . With Momentum -> ↓↓↓↓↓


# AdaGrad: 
    # সমস্যা: সব Parameter-এর Learning Rate এক।
    # সমাধান: প্রতিটি Parameter-এর জন্য আলাদা Learning Rate।

# RMSProp: 
    # AdaGrad-এর সমস্যা, Learning Rate ধীরে ধীরে খুব ছোট হয়ে যায়।
    # RMSProp -> Learning Rate-কে Balance করে।

# Adam: 
    # সবচেয়ে জনপ্রিয় Optimizer।
    # Adam = Momentum + RMSProp
    
import torch

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

# ML Relation: ChatGPT, Claude, Gemini, Llama, DeepSeek প্রায় সব আধুনিক Deep Learning Model Adam বা AdamW Optimizer ব্যবহার করে Training করা হয়।

