"""
===========================================================
Mathematics Fundamentals - Arithmetic - Order of Operations
===========================================================
Order of Operations হলো Arithmetic Expression Solve করার নির্দিষ্ট নিয়ম। যখন একটি Expression-এ একাধিক Operation থাকে, তখন কোন Operation আগে এবং কোনটি পরে হবে, সেটিই Order of Operations নির্ধারণ করে। 
Example: 2 + 3 × 4
Wrong: (2 + 3) × 4 = 20
Correct: 2 + (3 × 4) = 14
এই নিয়মকে BODMAS বা PEMDAS বলা হয়।
"""
# ===========================================================
# 01_Introduction
# ===========================================================
"""
Arithmetic Operations জানার পরে সবচেয়ে গুরুত্বপূর্ণ বিষয় হলো, কোন Operation আগে হবে। ধরো, 2 + 3 × 4 এখন প্রশ্ন, আগে Addition হবে? নাকি Multiplication? যদি সবাই নিজের মতো Solve করে, তাহলে ভিন্ন ভিন্ন Answer আসবে। তাই Mathematics একটি Standard Rule তৈরি করেছে। এটাই Order of Operations।
"""
# ===========================================================
# 02_WhyThisConceptExists
# ===========================================================
"""
ধরো, একটি দোকানে ২টি Chocolate এবং ৩টি Box; প্রতি Box-এ ৪টি Chocolate। 
Expression: 2 + 3 × 4; যদি আগে Addition করি (2 + 3) × 4 -> 20 এটি ভুল। কারণ, আগে ৩টি Box-এর Chocolate বের করতে হবে। 
3 × 4 ↓ 12; তারপর 2 + 12 -> 14 সঠিক Answer। এই সমস্যা সমাধানের জন্যই Order of Operations তৈরি হয়েছে।
"""
# ===========================================================
# 03_RealLifeIntuition
# ===========================================================
"""
ধরো, তুমি রান্না করছো। 
Step 1 -> চাল ধুবে।
Step 2 ->পানি দিবে।
Step 3 -> রান্না করবে।

যদি, আগে রান্না পরে পানি দাও, তাহলে খাবার নষ্ট হবে। ঠিক তেমনি Mathematics-এও সব Operation-এর নির্দিষ্ট Order আছে।
Wrong Order -> Wrong Answer
Correct Order -> Correct Answer
"""
# ===========================================================
# 04_Definition
# ===========================================================
"""
Definition: Order of Operations হলো একটি Mathematical Rule যা নির্ধারণ করে একাধিক Operation থাকলে কোনটি আগে সম্পন্ন হবে। সবচেয়ে পরিচিত নিয়ম BODMAS_
B = Brackets
O = Orders (Power, Root)
D = Division
M = Multiplication
A = Addition
S = Subtraction
--------------------------------
আরেকটি নাম, PEMDAS_
P = Parentheses
E = Exponents
M = Multiplication
D = Division
A = Addition
S = Subtraction
"""
# ===========================================================
# 05_Formula
# ===========================================================
"""
Solve করার Order_
1. Brackets -> ()
2. Power / Root
3. Division এবং Multiplication (বাম থেকে ডানে)
4. Addition এবং Subtraction (বাম থেকে ডানে)
"""
# ===========================================================
# 06_Derivation (How the Formula Comes)
# ===========================================================
"""
Example: 2 + 3 × 4

Step 1: Multiplication আগে 3 × 4 -> 12
Step 2: Addition 2 + 12 -> 14
--------------------------------
আরেকটি, (8 - 2) × 5

Step 1: Bracket: 8 - 2 -> 6
Step 2: Multiplication: 6 × 5 ->30

Bracket সবসময় আগে Solve হয়।
"""
# ===========================================================
# 07_InternalWorking / Visualization
# ===========================================================
"""
Expression: 2 + 3 × 4²
Step 1: Power - 4² -> 16; 2 + 3 × 16
Step 2: Multiplication - 3 × 16 -> 48
Step 3: Addition - 2 + 48 -> 50
--------------------------------
Flow: Expression -> Bracket -> Power -> Division / Multiplication -> Addition / Subtraction -> Final Answer
"""
# ===========================================================
# 08_Examples
# ===========================================================
"""
Example 1: 2 + 3 × 4 = 14
----------------------------
Example 2: (5 + 3) × 2 = 16
----------------------------
Example 3: 18 ÷ 3 × 2 = 6 × 2 = 12
----------------------------
Example 4: 2² + 5 = 4 + 5 = 9
----------------------------
Example 5: 20 - 8 ÷ 2 = 20 - 4 = 16
----------------------------
Example 6: (10 - 4)² = 6² = 36
"""
# ===========================================================
# 09_CommonMistakes
# ===========================================================
"""
Mistake 1: 2 + 3 × 4 = 20 Wrong; Correct - 14
----------------------------
Mistake 2: 20 - 8 ÷ 2 = 6 Wrong; Correct - 16
----------------------------
Mistake 3: (5 + 3)² = 5 + 9 Wrong; Correct 8² = 64
----------------------------
Mistake 4: Division সবসময় Multiplication-এর আগে। Wrong; Division এবং Multiplication একই Priority। বাম থেকে ডানে Solve করতে হবে।
----------------------------
Mistake 5: Addition সবসময় Subtraction-এর আগে। Wrong; Addition এবং Subtraction একই Priority। বাম থেকে ডানে Solve করতে হবে।
"""
# ===========================================================
# 10_Exercises
# ===========================================================
"""
Level 1: 
1) 5 + 4 × 3
----------------------------
2) 20 - 12 ÷ 4
----------------------------
3) (6 + 2) × 5
----------------------------
4) 3² + 7
----------------------------
5) 30 ÷ 5 × 2
============================
Level 2::

1) 2 + 3 × 4²
----------------------------
2) (10 + 5) ÷ 3
----------------------------
3) 5 × (6 - 2) + 1
----------------------------
4) 50 - 12 ÷ 3 × 2
----------------------------
5) (8 + 2)² - 10
============================
Challenge: নিজে এমন ৫টি Expression তৈরি কর, যেখানে Bracket, Power, Multiplication, Division, Addition সবগুলো Operation থাকবে।
"""
# ===========================================================
# 11_AIUsage (Machine Learning / AI)
# ===========================================================
"""
Programming Language এবং AI Framework-গুলো Order of Operations অনুসরণ করে। 
Example: Python; result = 2 + 3 * 4 Python আগে 3 * 4 -> 12; 2 + 12 -> 14
--------------------------------
Neural Network: Output = W × X + B; আগে Weight × Input তারপর Bias যোগ হয়। যদি Order পরিবর্তন হয়, Model-এর Output ভুল হবে।
--------------------------------
সব Programming Language Python, C, Java, JavaScript, MATLAB সবই Mathematics-এর Order of Operations অনুসরণ করে।
"""
# ===========================================================
# Summary
# ===========================================================
"""
✔ Order of Operations একটি Standard Mathematical Rule।
✔ BODMAS / PEMDAS মনে রাখা গুরুত্বপূর্ণ।
✔ Solve করার Order: BracketPower -> Division / Multiplication -> Addition / Subtraction
✔ একই Priority হলে বাম থেকে ডানে Solve করতে হবে।
✔ Programming Language, Scientific Computing, Machine Learning এবং AI সবই এই নিয়ম অনুসরণ করে।
"""