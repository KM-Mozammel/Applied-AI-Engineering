# Backpropagation : Neural Network কীভাবে শিখবে?

"""
===========================================================
Backpropagation (ব্যাকপ্রোপাগেশন)
===========================================================

Structure:
01_Introduction
02_WhyThisConceptExistsInRelationToHistory
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
Backpropagation হলো Neural Network শেখানোর
সবচেয়ে গুরুত্বপূর্ণ algorithm।


এটি ব্যবহার করে:

Neural Network-এর weight এবং bias update করা হয়।


মূল ধারণা:


Prediction

↓

Error Calculate

↓

Error-এর কারণ খুঁজে বের করা

↓

Weights update করা



Backpropagation নামের অর্থ:


Back

=

পিছনের দিকে


Propagation

=

ছড়িয়ে দেওয়া



অর্থাৎ:

Output error-কে network-এর পিছনের দিকে
propagate করা।


Backpropagation মূলত:


Chain Rule + Gradient Descent


এর combination।
"""


# ===========================================================
# 02_WhyThisConceptExistsInRelationToHistory
# ===========================================================

"""
ইতিহাস:


প্রথম Neural Network ধারণা:

Perceptron (1950s)


সমস্যা:

Simple network train করা গেলেও
deep network train করা কঠিন ছিল।


কারণ:

অনেক layer থাকলে কোন weight-এর কারণে
error হয়েছে বোঝা কঠিন।



1980s:

Backpropagation algorithm জনপ্রিয় হয়।


মূল সমস্যা:


Output error

কীভাবে

আগের layer-এর weight-এ পাঠানো হবে?



সমাধান:


Chain Rule ব্যবহার করে
error-এর gradient calculate করা।



এর ফলে:

Deep Neural Network train করা সম্ভব হয়।
"""


# ===========================================================
# 03_RealLifeIntuition
# ===========================================================

"""
বাস্তব জীবনের intuition:


Example 1:

একজন ছাত্র পরীক্ষায় ভুল করেছে।


Teacher দেখে:


Final answer ভুল।


তারপর খুঁজে বের করে:


কোন step-এ ভুল হয়েছে।


তারপর সেই জায়গা ঠিক করে।



এটাই Backpropagation।



--------------------------------


Example 2:

Neural Network:


Input:

ছবি


↓

Layers


↓

Prediction:

Cat



যদি ভুল হয়:


Prediction:

Dog



Network পিছনে যায়:


Output error

↓

Last layer weight

↓

Hidden layer weight

↓

Input layer



সব weight adjust করে।



--------------------------------


Example 3:

কারখানায়:


Product quality খারাপ।


Manager খুঁজে বের করে:

কোন machine parameter সমস্যা করেছে।


তারপর adjustment করে।
"""


# ===========================================================
# 04_Definition
# ===========================================================

"""
Backpropagation হলো:

একটি algorithm যা Neural Network-এর
output error ব্যবহার করে
প্রতিটি weight-এর gradient বের করে।


এর মাধ্যমে:


Weight update

↓

Loss কমানো

↓

Model শেখা



Backpropagation-এর প্রধান ধাপ:


1. Forward Pass


2. Loss Calculation


3. Backward Pass


4. Weight Update
"""


# ===========================================================
# 05_Formula
# ===========================================================

"""
Basic Idea:


Weight Update:


w_new

=

w_old - α∂L/∂w



যেখানে:


w

=

Weight



α

=

Learning Rate



L

=

Loss Function



∂L/∂w

=

Weight-এর gradient



--------------------------------


Chain Rule:


যদি:


L → y → z → w



তাহলে:


∂L/∂w


=

∂L/∂y

×

∂y/∂z

×

∂z/∂w



এইভাবেই error পিছনে যায়।



--------------------------------


Neuron Formula:


z=w*x+b


a=f(z)



Output error:


∂L/∂w


=

∂L/∂a

×

∂a/∂z

×

∂z/∂w
"""


# ===========================================================
# 06_Derivation (How the formula comes)
# ===========================================================

"""
Simple Neural Network:


Input:

x


Weight:

w


Output:


y=wx



Loss:


L=(y-target)²



Step 1:


Loss derivative:


∂L/∂y



যদি:


L=(y-t)²



তাহলে:


∂L/∂y=2(y-t)



--------------------------------


Step 2:


Output derivative:


y=wx



∂y/∂w=x



--------------------------------


Step 3:


Chain Rule:


∂L/∂w

=

∂L/∂y × ∂y/∂w



Therefore:


∂L/∂w

=

2(y-t)x



এই gradient দিয়ে weight update হয়।
"""


# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================

"""
Neural Network:


Forward:


Input

 ↓

Layer 1

 ↓

Layer 2

 ↓

Output



Prediction তৈরি হয়।



--------------------------------


Backward:


Loss

 ↓

Output Layer Gradient

 ↓

Hidden Layer Gradient

 ↓

Input Layer Gradient



--------------------------------


Internal Process:


Step 1:

Forward pass


প্রতিটি neuron value calculate করে।



Step 2:

Loss calculate করে।



Step 3:

Chain Rule দিয়ে gradient বের করে।



Step 4:

Gradient Descent দিয়ে weight update করে।



--------------------------------


Computational Graph:


w

↓

z

↓

activation

↓

output

↓

loss



Backpropagation এই graph-এর
উল্টো দিকে যায়।
"""


# ===========================================================
# 08_Examples
# ===========================================================

"""
Example 1:


Single Neuron:


Input:

x=2


Weight:

w=3


Prediction:


y=wx


=6



Target:

y=10



Error:


Loss=(6-10)²


=16



Gradient:


∂L/∂w


=

2(y-target)x



=

2(6-10)(2)



=

-16



Weight update:


w_new

=

3-0.1(-16)



=

4.6



Weight পরিবর্তিত হলো।



--------------------------------


Example 2:


Image Classification:


Input:

Image pixels


↓

CNN layers


↓

Prediction:

Cat 0.2

Dog 0.8



Wrong prediction হলে:


Loss calculate


Backpropagation:

CNN filter weight update করে।



--------------------------------


Example 3:


Language Model:


Input:

Sentence


↓

Transformer


↓

Next word prediction


↓

Loss


↓

Backpropagation


↓

Attention weights update
"""


# ===========================================================
# 09_CommonMistakes
# ===========================================================

"""
Common Mistakes:


1. Backpropagation এবং Gradient Descent
একই ভাবা


Backpropagation:

Gradient বের করে।


Gradient Descent:

Gradient ব্যবহার করে weight update করে।



--------------------------------


2. Forward pass এবং backward pass
মিশিয়ে ফেলা


Forward:

Prediction


Backward:

Learning



--------------------------------


3. Chain Rule ভুল করা


Backpropagation পুরোপুরি
Chain Rule-এর উপর নির্ভরশীল।



--------------------------------


4. Learning rate ভুল নির্বাচন


Too high:

Training unstable


Too low:

Slow learning



--------------------------------


5. Vanishing Gradient সমস্যা ভুলে যাওয়া


Deep network-এ gradient ছোট হয়ে যেতে পারে।
"""


# ===========================================================
# 10_Exercises
# ===========================================================

"""
Practice Problems:


1.


Explain:

Why Chain Rule is needed in Backpropagation?



--------------------------------


2.


Difference between:


Forward Propagation

Backpropagation



--------------------------------


3.


For:


y=wx


Find:


∂y/∂w



--------------------------------


4.


Why does backpropagation update weights?



--------------------------------


5.


Explain:

Gradient Descent + Backpropagation relationship
"""


# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================

"""
AI এবং Deep Learning-এ Backpropagation:


1. Neural Network Training


সব ধরনের neural network:


- MLP
- CNN
- RNN
- Transformer


train করতে ব্যবহার হয়।



--------------------------------


2. Computer Vision


CNN:


Image

↓

Feature extraction

↓

Classification


Filter weight শেখার জন্য
backpropagation প্রয়োজন।



--------------------------------


3. Natural Language Processing


Transformer model:

GPT

BERT


training-এ backpropagation ব্যবহার হয়।



--------------------------------


4. Large Language Models


LLM training:


Forward:


Token prediction


↓

Loss


↓

Backpropagation


↓

Billions of parameters update



--------------------------------


5. Reinforcement Learning


Policy network এবং value network
train করতে ব্যবহৃত হয়।



--------------------------------


6. Automatic Differentiation


PyTorch এবং TensorFlow:


Gradient automatically calculate করে।


ভিতরে:

Chain Rule + Backpropagation


ব্যবহার হয়।



--------------------------------


Summary:


Backpropagation শেখায়:


✓ Neural network কীভাবে শেখে
✓ Error কীভাবে পিছনে যায়
✓ Gradient কীভাবে তৈরি হয়
✓ Weight কীভাবে update হয়


Deep Learning revolution-এর মূল
algorithm হলো Backpropagation।
"""


# ===========================================================
# End of Backpropagation
# ===========================================================