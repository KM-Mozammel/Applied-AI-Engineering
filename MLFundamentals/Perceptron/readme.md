# Perceptron (1957)
Invented by Frank Rosenblatt. The simplest neural network possible.

# Dataset (AND gate):

x1	x2	Output
0	0	0
0	1	0
1	0	0
1	1	1

# Perceptron Equation
y = w1*x1 + w2*x2 + bias


# Training Algorithm
Perceptron Learning Rule:

error = expected - prediction
weight = weight + learning_rate * error * input
bias   = bias   + learning_rate * error