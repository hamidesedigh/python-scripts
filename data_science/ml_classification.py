"""
Heart Disease Prediction Project - Improved Version

This script performs exploratory data analysis and feature selection
for heart disease prediction using the heart.csv dataset.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_selection import SelectKBest, f_regression


class HeartDiseaseAnalyzer:
    """
    A class to analyze heart disease data and perform feature selection.
    """

    def __init__(self, data_path="heart.csv"):
        """
        Initialize the analyzer with data path.

        Args:
            data_path (str): Path to the heart disease dataset
        """
        self.data_path = data_path
        self.df = None
        self.cdf = None
        self.X = None
        self.y = None
        self.selected_features = None

    def load_data(self):
        """
        Load and prepare the heart disease dataset.
        """
        try:
            self.df = pd.read_csv(self.data_path)
            print(f"Dataset loaded successfully with shape: {self.df.shape}")
            return True
        except FileNotFoundError:
            print(f"Error: File '{self.data_path}' not found.")
            return False
        except Exception as e:
            print(f"Error loading data: {e}")
            return False

    def prepare_data(self):
        """
        Prepare the data by creating a clean DataFrame and separating features from target.
        """
        if self.df is None:
            print("Please load data first using load_data()")
            return False

        # Create a clean DataFrame with all columns
        self.cdf = self.df.copy()

        # Separate features and target
        self.X = self.cdf.drop("output", axis=1)
        self.y = self.cdf["output"]

        print("Data preparation completed.")
        print(f"Features shape: {self.X.shape}")
        print(f"Target shape: {self.y.shape}")

        return True

    def display_data_info(self, n_rows=5):
        """
        Display basic information about the dataset.

        Args:
            n_rows (int): Number of rows to display in head()
        """
        if self.df is None:
            print("No data loaded.")
            return

        print("\n" + "=" * 50)
        print("DATASET INFORMATION")
        print("=" * 50)

        print(f"\nFirst {n_rows} rows:")
        print(self.df.head(n_rows))

        print(f"\nDataset shape: {self.df.shape}")
        print(f"\nColumn names: {list(self.df.columns)}")

        print("\nData types:")
        print(self.df.dtypes)

        print("\nBasic statistics:")
        print(self.df.describe())

        print(f"\nMissing values:\n{self.df.isnull().sum()}")

        print(f"\nTarget variable distribution:")
        print(self.df['output'].value_counts())

    def plot_correlation_heatmap(self, figsize=(12, 10)):
        """
        Plot correlation heatmap for the dataset.

        Args:
            figsize (tuple): Figure size for the heatmap
        """
        if self.cdf is None:
            print("Please prepare data first using prepare_data()")
            return

        print("\n" + "=" * 50)
        print("CORRELATION ANALYSIS")
        print("=" * 50)

        # Calculate correlation matrix
        corr_matrix = self.cdf.corr()

        # Create heatmap
        plt.figure(figsize=figsize)
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

        sns.heatmap(
            corr_matrix,
            mask=mask,
            cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True,
            annot=True,
            fmt=".2f",
            center=0,
            cbar_kws={"shrink": .8}
        )

        plt.title("Correlation Matrix of Heart Disease Features", fontsize=16, pad=20)
        plt.tight_layout()
        plt.show()

        # Display top correlations with target variable
        target_correlations = corr_matrix['output'].sort_values(ascending=False)
        print("\nTop correlations with target variable (output):")
        print(target_correlations)

    def perform_feature_selection(self, p_value_threshold=0.05, score_threshold=5):
        """
        Perform univariate feature selection using f_regression.

        Args:
            p_value_threshold (float): Maximum p-value for feature selection
            score_threshold (float): Minimum f-score for feature selection
        """
        if self.X is None or self.y is None:
            print("Please prepare data first using prepare_data()")
            return

        print("\n" + "=" * 50)
        print("FEATURE SELECTION RESULTS")
        print("=" * 50)

        # Perform feature selection
        feature_selector = SelectKBest(f_regression, k="all")
        fit = feature_selector.fit(self.X, self.y)

        # Create summary statistics
        p_values = pd.DataFrame(fit.pvalues_)
        scores = pd.DataFrame(fit.scores_)
        input_variable_names = pd.DataFrame(self.X.columns)

        summary_stats = pd.concat([input_variable_names, p_values, scores], axis=1)
        summary_stats.columns = ["feature", "p_value", "f_score"]
        summary_stats = summary_stats.sort_values("p_value")

        # Display all features statistics
        print("\nAll features (sorted by p-value):")
        print(summary_stats.to_string(index=False, float_format="%.4f"))

        # Select significant features
        significant_features = summary_stats.loc[
            (summary_stats["f_score"] >= score_threshold) &
            (summary_stats["p_value"] <= p_value_threshold)
            ]

        self.selected_features = significant_features["feature"].tolist()

        print(f"\nSelected features (p-value <= {p_value_threshold}, f-score >= {score_threshold}):")
        print(f"Number of selected features: {len(self.selected_features)}")
        print(f"Selected features: {self.selected_features}")

        # Create feature subset
        X_selected = self.X[self.selected_features]

        print(f"\nSelected features dataset shape: {X_selected.shape}")
        print("\nFirst 5 rows of selected features:")
        print(X_selected.head())

        return X_selected

    def plot_feature_importance(self):
        """
        Plot feature importance based on f-scores from feature selection.
        """
        if self.X is None or self.y is None:
            print("Please prepare data first using prepare_data()")
            return

        # Perform feature selection to get scores
        feature_selector = SelectKBest(f_regression, k="all")
        fit = feature_selector.fit(self.X, self.y)

        # Create feature importance dataframe
        feature_importance = pd.DataFrame({
            'feature': self.X.columns,
            'f_score': fit.scores_
        }).sort_values('f_score', ascending=True)

        # Plot feature importance
        plt.figure(figsize=(10, 8))
        plt.barh(feature_importance['feature'], feature_importance['f_score'])
        plt.xlabel('F-score (Higher = More Important)')
        plt.title('Feature Importance for Heart Disease Prediction')
        plt.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        plt.show()

    def run_complete_analysis(self):
        """
        Run the complete analysis pipeline.
        """
        print("HEART DISEASE PREDICTION - COMPLETE ANALYSIS")
        print("=" * 60)

        # Load data
        if not self.load_data():
            return

        # Prepare data
        if not self.prepare_data():
            return

        # Display data information
        self.display_data_info()

        # Plot correlation heatmap
        self.plot_correlation_heatmap()

        # Perform feature selection
        selected_features_data = self.perform_feature_selection()

        # Plot feature importance
        self.plot_feature_importance()

        print("\n" + "=" * 60)
        print("ANALYSIS COMPLETED SUCCESSFULLY!")
        print("=" * 60)

        return selected_features_data


def main():
    """
    Main function to run the heart disease analysis.
    """
    # Initialize analyzer
    analyzer = HeartDiseaseAnalyzer("heart.csv")

    # Run complete analysis
    selected_features = analyzer.run_complete_analysis()

    # You can now use selected_features for modeling
    if selected_features is not None:
        print(f"\nThe selected features dataset is ready for modeling.")
        print(f"Shape: {selected_features.shape}")
        print(f"Target variable shape: {analyzer.y.shape}")


if __name__ == "__main__":
    main()