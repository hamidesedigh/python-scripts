# -*- coding: utf-8 -*-
"""
ml_regression.py
-----------------------------------------------------------
Performs simple linear regression on synthetic data using scikit-learn.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def main():
    X = np.random.rand(50, 1) * 10
    y = 3 * X.squeeze() + 5 + np.random.randn(50)

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    print(f"Coefficient: {model.coef_[0]:.2f}, Intercept: {model.intercept_:.2f}")

    plt.scatter(X, y, label="Data")
    plt.plot(X, y_pred, color="red", label="Regression Line")
    plt.legend()
    plt.title("Simple Linear Regression")
    plt.show()

if __name__ == "__main__":
    main()
