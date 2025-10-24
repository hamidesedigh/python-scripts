# -*- coding: utf-8 -*-
"""
ml_clustering.py
-----------------------------------------------------------
Performs K-Means clustering on synthetic 2D data.
"""

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def main():
    X, _ = make_blobs(n_samples=200, centers=3, random_state=42)
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X)
    labels = kmeans.labels_

    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis")
    plt.title("K-Means Clustering")
    plt.show()

if __name__ == "__main__":
    main()
