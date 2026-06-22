NumPy is used for
    1. Data Science
    2. Machine Learning
    3. Scientific Computing

NumPy introduces the ndarray (N-dimensional array), which is blindingly fast because it's written in C and use contiguous memory blocks.

# NumPy stores numbers in continuous memory blocks, similar to C/C++, making operations much faster.

Python List Memory
numbers = [10, 20, 30, 40]

Memory looks roughly like:

List
 |
 +----> Address A --> 10
 |
 +----> Address B --> 20
 |
 +----> Address C --> 30
 |
 +----> Address D --> 40

Each value is a separate Python object.

Extra memory is needed for:

Object metadata
Type information
References

This is flexible but slower.

# NumPy introduces the ndarray (N-dimensional array), which solves these issues:

Speed: Arrays are stored in contiguous memory and use optimized C code under the hood. Operations run hundreds of times faster than Python loops.

True multidimensionality: You can easily create 1D, 2D, 3D, or higher arrays — perfect for images, audio, or scientific data.

Vectorized operations: Instead of looping, you apply math to the whole array at once.

Broadcasting: Smaller arrays automatically expand to match larger ones during operations.

Rich math toolkit: Built-in functions for dot products, eigenvalues, Fourier transforms, statistics, etc.

Interoperability: NumPy arrays are the foundation for libraries like TensorFlow, PyTorch, and scikit-learn.


# So, NumPy’s magic is that it reduces every kind of real-world data into structured arrays of numbers, making them ready for computation.