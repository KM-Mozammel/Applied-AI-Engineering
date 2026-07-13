# Day 1 – Calculus (8h)
Morning (3h): Derivatives, chain rule, partial derivatives (manual practice).

Afternoon (3h): Gradient descent in Python (from scratch + NumPy).

Evening (2h): Interview Q&A + cheat sheet consolidation.

Definition: Calculus studies change. Derivatives measure how fast something changes.
Analogy: Speedometer in a car = derivative of distance.
Python Example:

python
Derivative of f(x) = x^2 at x=3
def f(x): return x**2
h = 1e-5
derivative = (f(3+h) - f(3)) / h
print(derivative)  # ~6
# Day 2 – Linear Algebra (8h)
Morning (3h): Vectors, dot/cross product, matrix operations (manual).

Afternoon (3h): Matrix multiplication, eigenvalues, SVD in Python.

Evening (2h): Connect to embeddings, PCA, transformers.

Definition: Linear algebra is math of vectors and matrices.
Analogy: A spreadsheet grid where rows/columns interact.
Python Example:

python
import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[2,0],[1,2]])
print(A @ B)  # Matrix multiplication
# Day 3 – Probability (8h)
Morning (3h): Bayes theorem, priors/posteriors, Gaussian distributions.

Afternoon (3h): Sampling, Markov chains (Python simulations).

Evening (2h): Interview prep: spam filtering, uncertainty in ML.

Definition: Probability measures uncertainty.
Analogy: Rolling dice → chance of outcomes.
Python Example:

python
import random
trials = [random.choice([0,1]) for _ in range(1000)]
print(sum(trials)/1000)  # Approx probability of 1
# Day 4 – Statistics (8h)
Morning (3h): Mean, variance, covariance, correlation (manual).

Afternoon (3h): Hypothesis testing, confidence intervals, p-values.

Evening (2h): Case studies: model evaluation metrics.

Definition: Statistics summarizes data.
Analogy: Average exam score = mean. Spread of scores = variance.
Python Example:

python
import numpy as np
data = np.array([10,20,30,40])
print("Mean:", np.mean(data))
print("Variance:", np.var(data))
# Day 5 – Optimization (8h)
Morning (3h): Convexity, Lagrange multipliers (manual derivations).

Afternoon (3h): SGD variants (Adam, RMSProp) in Python.

Evening (2h): Connect to deep learning training stability.

Definition: Optimization finds best solutions.
Analogy: Finding the lowest point in a valley.
Python Example (Gradient Descent):

python
x = 10
lr = 0.1
for _ in range(20):
    grad = 2*x  # derivative of f(x)=x^2
    x -= lr*grad
print(x)  # ~0
# Day 6 – Numerical Methods (8h)
Morning (3h): Approximation, iterative solvers, floating-point stability.

Afternoon (3h): Implement iterative solver in Python.

Evening (2h): Discuss numerical stability in ML pipelines.

Definition: Numerical methods approximate solutions when exact math is hard.
Analogy: Using a calculator for square roots instead of exact formula.
Python Example (Newton’s method):

python
def sqrt_newton(n, iterations=10):
    x = n/2
    for _ in range(iterations):
        x = 0.5*(x + n/x)
    return x
print(sqrt_newton(16))  # ~4
# Day 7 – Information Theory (8h)
Morning (3h): Entropy, KL divergence (manual derivations).

Afternoon (3h): Cross-entropy loss in Python.

Evening (2h): Connect to LLM training, embeddings, RAG scoring.

Definition: Information theory measures uncertainty and information.
Analogy: A coin flip is less surprising than lottery numbers.
Python Example (Entropy):

python
import math
p = [0.5, 0.5]
entropy = -sum(pi*math.log2(pi) for pi in p)
print(entropy)  # 1 bit

# Interview Prep Notes
Calculus: Why do we need derivatives in ML? → For optimization.

Linear Algebra: How does SVD relate to embeddings? → Dimensionality reduction.

Probability: How does Bayes theorem apply to spam filtering? → Posterior probability.

Statistics: Why use p-values? → To test significance.

Optimization: Why Adam over SGD? → Faster convergence, adaptive learning rates.

Numerical Methods: Why care about floating-point stability? → Prevent exploding/vanishing gradients.

Information Theory: Why cross-entropy loss? → Measures difference between predicted and true distributions.



# !-- Recommended Order -->
# Linear Algebra
Foundation for vectors, matrices, embeddings, PCA, and neural networks.
Learn matrix multiplication, eigenvalues, and singular value decomposition before moving on.

# Calculus
Essential for understanding gradients, optimization, and backpropagation.
Focus on derivatives, partial derivatives, and integrals.

# Probability
Builds intuition for uncertainty, distributions, and Bayesian reasoning.
Crucial for generative models and decision-making systems.

# Statistics
Extends probability into data analysis.
Covers hypothesis testing, confidence intervals, regression, and evaluation metrics.

# Optimization
Connects calculus + linear algebra into practical algorithms.
Learn gradient descent, convex optimization, and modern optimizers (Adam, RMSProp).

# Numerical Methods
Teaches stability, approximation, and iterative solvers.
Important for implementing algorithms efficiently in code.

# Information Theory
The most abstract, but critical for modern AI.
Entropy, KL divergence, and cross-entropy loss connect directly to deep learning and LLMs.

# 01_Introduction
# 02_WhyThisConceptExistsInRealtionTohistory
# 03_RealLifeIntuition
# 04_Definition
# 05_Formula
# 06_Derivation (How the formula comes)
# 07_InternalWorking / Visualization
# 08_Examples
# 09_CommonMistakes
# 10_Exercises
# 11_AIUsage (Machine Learning / AI)