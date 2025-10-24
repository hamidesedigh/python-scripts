# -*- coding: utf-8 -*-
"""
ml_classification.py
-----------------------------------------------------------
Binary classification example using Logistic Regression.
"""

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def main():
    # Adjusted parameters so they match n_features=2
    X, y = make_classification(
        n_samples=100,
        n_features=2,
        n_informative=2,
        n_redundant=0,
        n_clusters_per_class=1,
        random_state=42
    )

    model = LogisticRegression()
    model.fit(X, y)
    preds = model.predict(X)
    print(f"Accuracy: {accuracy_score(y, preds):.2f}")


    # After fitting:
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', alpha=0.7)
    plt.title("Logistic Regression Classification")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()


if __name__ == "__main__":
    main()
