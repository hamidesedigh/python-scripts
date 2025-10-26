# -*- coding: utf-8 -*-
"""
@author: Hamideh
Created on Sat Nov 18 12:34:13 2025

numpy_basics.py
-----------------------------------------------------------
Comprehensive NumPy guide for Data Science practice.

Main Topics:
1️⃣ Creating Arrays (1D, 2D, 3D, placeholders)
2️⃣ Array Attributes & Data Types
3️⃣ Indexing, Slicing, and Subsetting
4️⃣ Array Operations & Mathematics
5️⃣ Array Functions & Inspection
6️⃣ Copying, Sorting, and Manipulating Arrays
7️⃣ I/O: Saving and Loading Arrays

⚙️ This script was AI-assisted, generated and refined with the help of ChatGPT to accelerate learning and documentation.
"""

import numpy as np


def main():
    # ======================================================
    # 1️⃣ Creating Arrays (1D, 2D, 3D, placeholders)
    # ======================================================
    print("\n=== 1️⃣ Creating Arrays ===")

    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    arr3 = np.arange(8).reshape(2, 2, 2)

    print("1D:", arr1)
    print("2D:\n", arr2)
    print("3D:\n", arr3)

    # Placeholder arrays
    print("Zeros:\n", np.zeros((2, 3)))
    print("Ones:\n", np.ones((3, 2)))
    print("Identity:\n", np.eye(3))
    print("Full:\n", np.full((3, 3), 9))
    print("Arange:", np.arange(0, 10, 2))
    print("Linspace:", np.linspace(0, 1, 5))
    print("Random:\n", np.random.rand(2, 2))
    print("Empty:\n", np.empty((3, 2)))

    # ======================================================
    # 2️⃣ Array Attributes & Data Types
    # ======================================================
    print("\n=== 2️⃣ Attributes & Data Types ===")

    print("Shape:", arr2.shape)
    print("Dimensions:", arr2.ndim)
    print("Length of array:", len(arr2))
    print("Number of elements:", arr2.size)
    print("Data type:", arr2.dtype)
    print("Name of data type:", arr2.dtype.name)

    arr_int = np.array([1, 2, 3], dtype=np.int16)
    arr_float = arr_int.astype(float)
    print("Converted dtype:", arr_float.dtype)

    # ======================================================
    # 3️⃣ Indexing, Slicing, and Subsetting
    # ======================================================
    print("\n=== 3️⃣ Indexing, Slicing, and Subsetting ===")

    a = np.arange(10)
    print("Array:", a)
    print("a[2:7]:", a[2:7])
    print("a[::-1] (reversed):", a[::-1])

    b = np.arange(1, 13).reshape(3, 4)
    print("2D array:\n", b)
    print("Row 1:", b[1, :])
    print("Column 2:", b[:, 2])
    print("Slice [0:2, 1:3]:\n", b[0:2, 1:3])
    print("Conditional subset (b>5):", b[b > 5])

    # ======================================================
    # 4️⃣ Array Operations & Mathematics
    # ======================================================
    print("\n=== 4️⃣ Array Operations & Mathematics ===")

    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    b = np.array([[2.5, 2., 3.],
                  [1., 2., 3.]])

    # ---- Basic Arithmetic ----
    print("\n-- Basic Arithmetic --")
    print("Addition (a+b):\n", a + b)
    print("Addition (np.add):\n", np.add(a, b))
    print("Subtraction:\n", np.subtract(a, b))
    print("Multiplication:\n", np.multiply(a, b))
    print("Division:\n", np.divide(a, b))

    # ---- Element-wise Math ----
    print("\n-- Element-wise Math Functions --")
    print("Exponentiation np.exp(b):\n", np.exp(b))
    print("Square Root np.sqrt(b):\n", np.sqrt(b))
    print("Sine np.sin(a):\n", np.sin(a))
    print("Cosine np.cos(b):\n", np.cos(b))
    print("Natural Logarithm np.log(a):\n", np.log(a))

    # ---- Statistics & Aggregations ----
    print("\n-- Aggregations and Stats --")
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    print("Addition:", x + y, "\t or \t", np.add(x, y))
    print("Multiplication:", x * y)
    print("Power (x**2):", x ** 2)
    print("Dot product:", np.dot(x, y))
    print("Elementwise sqrt:", np.sqrt(x))
    print("Sum:", x.sum(), "Mean:", x.mean(), "Std:", x.std())
    print("Min:", np.min(x), "Max:", np.max(x))
    print("Cumulative Sum:", np.cumsum(x))
    print("Cumulative Product:", np.cumprod(x))
    print("Correlation Coefficient:\n", np.corrcoef(x, y))
    print("Covariance Matrix:\n", np.cov(x, y))

    # ---- Matrix Operations ----
    print("\n-- Matrix Dot Product --")
    e = np.array([[1, 2], [3, 4]])
    f = np.array([[2, 0], [1, 3]])
    print("Matrix e:\n", e)
    print("Matrix f:\n", f)
    print("Dot product (e.dot(f)):\n", e.dot(f))
    print("Matrix product (np.matmul):\n", np.matmul(e, f))

    # ======================================================
    # 5️⃣ Array Functions & Inspection
    # ======================================================
    print("\n=== 5️⃣ Functions & Inspection ===")

    m = np.random.randint(1, 10, (3, 3))
    print("Array:\n", m)
    print("Min/Max:", m.min(), "/", m.max())
    print("Argmin/Argmax:", m.argmin(), "/", m.argmax())
    print("Cumulative Sum:", m.cumsum())
    print("Axis-wise Sum:", m.sum(axis=0))
    print("Flattened:", m.flatten())

    # ======================================================
    # 6️⃣ Copying, Sorting, and Manipulating Arrays
    # ======================================================
    print("\n=== 6️⃣ Copying, Sorting, and Manipulating Arrays ===")

    a = np.array([[3, 1, 2], [9, 5, 6]])
    b = a.copy()
    a[0, 0] = 99
    print("Original modified a:\n", a)
    print("Deep copy b (unchanged):\n", b)

    print("Sorted (row-wise):\n", np.sort(a, axis=1))
    print("Reshaped (3x2):\n", a.reshape(3, 2))
    print("Transpose:\n", a.T)
    print("Concatenate horizontally:\n", np.hstack((a, b)))
    print("Concatenate vertically:\n", np.vstack((a, b)))
    print("Flattened (ravel):", b.ravel())

    # Boolean & Fancy Indexing
    a = np.array([1, 2, 3, 4, 5, 6])
    print("\n-- Boolean & Fancy Indexing --")
    print("Elements > 3:", a[a > 3])
    print("Even elements:", a[a % 2 == 0])
    idx = [0, 2, 4]
    print("Selected indices [0, 2, 4]:", a[idx])

    # Reshaping, Adding, Removing
    g = np.arange(6)
    h = np.arange(6)
    h.resize((2, 3))
    print("Resized h (2x3):\n", h)
    print("Append items to h:\n", np.append(h, g))
    print("Insert 5 at index 1:", np.insert(a, 1, 5))
    print("Delete index 1 from a:", np.delete(a, [1]))

    # Splitting
    a = np.array([1, 2, 3])
    print("Horizontal split:", np.hsplit(a, 3))
    c = np.array([[[1.5, 2., 1.],
                   [4., 5., 6.]]])
    print("Vertical split:", np.vsplit(c, 1))

    # ======================================================
    # 7️⃣ I/O: Saving and Loading Arrays
    # ======================================================
    print("\n=== 7️⃣ Saving and Loading Arrays ===")

    np.save("array_example.npy", b)
    loaded = np.load("array_example.npy")
    print("Loaded from file:\n", loaded)

    np.savez("arrays_bundle.npz", first=a, second=b)
    data = np.load("arrays_bundle.npz")
    print("Loaded bundle keys:", data.files)
    print("Second array:\n", data["second"])


if __name__ == "__main__":
    main()
