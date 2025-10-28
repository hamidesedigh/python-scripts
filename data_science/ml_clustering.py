# customer_segmentation.py
"""
Customer Segmentation Analysis
Clustering-Based Customer Profiling using Multiple ML Algorithms

⚙️ This script was AI-assisted, generated and refined with the help of ChatGPT to accelerate learning and documentation.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, davies_bouldin_score


def load_and_preprocess_data():
    """
    Load and preprocess customer data from CSV file

    Returns:
        tuple: Processed feature matrix (X) and original DataFrame
    """
    print("Loading customer data...")
    df = pd.read_csv("customer.csv")
    print("Data description:")
    print(df.describe())

    # Rename columns for simplicity
    mapping = {'Annual Income (k$)': 'AnnualIncome', 'Spending Score (1-100)': 'SpendingScore'}
    df = df.rename(columns=mapping)

    # Encode Gender (Male=1, Female=0)
    df["Gender"] = LabelEncoder().fit_transform(df["Gender"])

    # Select features (drop CustomerID)
    X = df.drop(columns=["CustomerID"])

    print("\nFirst 5 rows of processed data:")
    print(X.head())

    # Data cleaning - convert to numeric and remove NaN values
    print(f"\nShape of Data before cleaning: {X.shape}")
    X[['Gender', 'Age', 'AnnualIncome', 'SpendingScore']] = X[['Gender', 'Age', 'AnnualIncome', 'SpendingScore']].apply(
        pd.to_numeric, errors='coerce')
    X = X.dropna()
    print(f"Shape of Data after cleaning: {X.shape}")

    print("\nFirst 5 rows after cleaning:")
    print(X.head())

    return X, df


def exploratory_data_analysis(X):
    """
    Perform exploratory data analysis including correlation analysis

    Args:
        X (DataFrame): Processed customer data

    Returns:
        DataFrame: Correlation matrix
    """
    print("\nPerforming Exploratory Data Analysis...")

    # Correlation matrix and heatmap
    print("Generating correlation heatmap...")
    f, ax = plt.subplots(figsize=(10, 8))
    corr = X.corr()
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=bool),
                cmap=sns.diverging_palette(220, 10, as_cmap=True),
                square=True, ax=ax)
    plt.title("Correlation Matrix Heatmap")
    plt.tight_layout()
    plt.show()

    # Display data info
    print("Data shape:", X.shape)
    print("\nData info:")
    print(X.info())

    return corr


def prepare_clustering_data(X):
    """
    Prepare data for clustering algorithms by scaling and applying PCA

    Args:
        X (DataFrame): Original feature data

    Returns:
        tuple: Scaled data, PCA transformed data, scaler, and PCA object
    """
    print("\nPreparing data for clustering...")

    # Scale the data for clustering algorithms
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Apply PCA for dimensionality reduction and visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
    print(f"Total explained variance: {sum(pca.explained_variance_ratio_):.4f}")

    return X_scaled, X_pca, scaler, pca


def apply_clustering_algorithms(X_scaled):
    """
    Apply multiple clustering algorithms to the scaled data

    Args:
        X_scaled (array): Scaled feature matrix

    Returns:
        dict: Results from all clustering algorithms including labels and metrics
    """
    print("\nApplying clustering algorithms...")

    results = {}

    # 1. KMeans Clustering - Partition-based algorithm
    print("1. Applying KMeans clustering...")
    kmeans = KMeans(n_clusters=5, random_state=42)
    kmeans_labels = kmeans.fit_predict(X_scaled)
    results['kmeans'] = {
        'model': kmeans,
        'labels': kmeans_labels,
        'silhouette': silhouette_score(X_scaled, kmeans_labels),
        'davies_bouldin': davies_bouldin_score(X_scaled, kmeans_labels)
    }

    # 2. Agglomerative Clustering - Hierarchical clustering
    print("2. Applying Agglomerative clustering...")
    agglo = AgglomerativeClustering(n_clusters=5)
    agglo_labels = agglo.fit_predict(X_scaled)
    results['agglo'] = {
        'model': agglo,
        'labels': agglo_labels,
        'silhouette': silhouette_score(X_scaled, agglo_labels),
        'davies_bouldin': davies_bouldin_score(X_scaled, agglo_labels)
    }

    # 3. DBSCAN Clustering - Density-based clustering
    print("3. Applying DBSCAN clustering...")
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    dbscan_labels = dbscan.fit_predict(X_scaled)
    # Only calculate metrics if more than 1 cluster found
    if len(set(dbscan_labels)) > 1:
        results['dbscan'] = {
            'model': dbscan,
            'labels': dbscan_labels,
            'silhouette': silhouette_score(X_scaled, dbscan_labels),
            'davies_bouldin': davies_bouldin_score(X_scaled, dbscan_labels)
        }
    else:
        results['dbscan'] = {
            'model': dbscan,
            'labels': dbscan_labels,
            'silhouette': None,
            'davies_bouldin': None
        }

    # 4. Gaussian Mixture Model - Probabilistic clustering
    print("4. Applying Gaussian Mixture Model...")
    gmm = GaussianMixture(n_components=5, random_state=42)
    gmm_labels = gmm.fit_predict(X_scaled)
    results['gmm'] = {
        'model': gmm,
        'labels': gmm_labels,
        'silhouette': silhouette_score(X_scaled, gmm_labels),
        'davies_bouldin': davies_bouldin_score(X_scaled, gmm_labels)
    }

    return results


def evaluate_clustering_results(results):
    """
    Evaluate and compare performance of all clustering algorithms

    Args:
        results (dict): Dictionary containing clustering results
    """
    print("\n" + "=" * 50)
    print("CLUSTERING RESULTS EVALUATION")
    print("=" * 50)

    for algo_name, result in results.items():
        print(f"\n{algo_name.upper()} Results:")
        print(f"  Silhouette Score: {result['silhouette']:.4f}" if result[
                                                                       'silhouette'] is not None else "  Silhouette Score: N/A")
        print(f"  Davies-Bouldin Score: {result['davies_bouldin']:.4f}" if result[
                                                                               'davies_bouldin'] is not None else "  Davies-Bouldin Score: N/A")
        print(f"  Number of clusters found: {len(set(result['labels']))}")


def visualize_clustering_results(X, X_pca, results):
    """
    Create visualizations comparing different clustering algorithms

    Args:
        X (DataFrame): Original feature data
        X_pca (array): PCA-transformed data for 2D visualization
        results (dict): Clustering results from all algorithms
    """
    print("\nGenerating clustering visualizations...")

    # Create subplots for different clustering results
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    axes = axes.ravel()

    algorithms = list(results.keys())

    for i, algo_name in enumerate(algorithms):
        if i < len(axes):
            labels = results[algo_name]['labels']

            # Create scatter plot using PCA components
            scatter = axes[i].scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', alpha=0.7)
            axes[i].set_title(f'{algo_name.upper()} Clustering')
            axes[i].set_xlabel('Principal Component 1')
            axes[i].set_ylabel('Principal Component 2')
            plt.colorbar(scatter, ax=axes[i])

            # Add silhouette score to plot if available
            silhouette = results[algo_name]['silhouette']
            if silhouette is not None:
                axes[i].text(0.05, 0.95, f'Silhouette: {silhouette:.3f}',
                             transform=axes[i].transAxes, bbox=dict(boxstyle="round", facecolor='wheat', alpha=0.5))

    # Hide any unused subplots
    for i in range(len(algorithms), len(axes)):
        axes[i].set_visible(False)

    plt.tight_layout()
    plt.show()


def main():
    """
    Main function to execute the complete customer segmentation analysis pipeline

    Workflow:
    1. Data Loading & Preprocessing
    2. Exploratory Data Analysis
    3. Data Preparation for Clustering
    4. Apply Multiple Clustering Algorithms
    5. Evaluate & Compare Results
    6. Visualize Clustering Outcomes
    """
    print("CUSTOMER SEGMENTATION ANALYSIS")
    print("=" * 40)

    try:
        # 1. Load and preprocess data
        X, original_df = load_and_preprocess_data()

        # 2. Exploratory Data Analysis
        corr_matrix = exploratory_data_analysis(X)

        # 3. Prepare data for clustering
        X_scaled, X_pca, scaler, pca = prepare_clustering_data(X)

        # 4. Apply clustering algorithms
        clustering_results = apply_clustering_algorithms(X_scaled)

        # 5. Evaluate results
        evaluate_clustering_results(clustering_results)

        # 6. Visualize results
        visualize_clustering_results(X, X_pca, clustering_results)

        print("\n" + "=" * 50)
        print("ANALYSIS COMPLETED SUCCESSFULLY!")
        print("=" * 50)

    except FileNotFoundError:
        print("Error: 'customer.csv' file not found. Please ensure the file is in the same directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please check your data and try again.")


if __name__ == "__main__":
    main()