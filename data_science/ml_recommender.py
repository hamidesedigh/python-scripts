# -*- coding: utf-8 -*-
"""
ml_recommender.py
-----------------------------------------------------------
A minimal recommender system using cosine similarity.
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def main():
    # Rows = users, Columns = movies (ratings)
    ratings = np.array([
        [5, 3, 0, 1],
        [4, 0, 0, 1],
        [1, 1, 0, 5],
        [0, 0, 5, 4],
    ])

    sim = cosine_similarity(ratings)
    print("User similarity matrix:\n", np.round(sim, 2))

if __name__ == "__main__":
    main()
