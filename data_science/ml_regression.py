"""
House Price Prediction Project
Machine Learning Project - Multiple Linear Regression with Feature Engineering

⚙️ This script was AI-assisted, generated and refined with the help of ChatGPT to accelerate learning and documentation.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler, PolynomialFeatures
from sklearn.feature_selection import SelectKBest, f_regression, RFECV
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


class HousePricePredictor:
    def __init__(self, file_path="housePrice.csv"):
        self.file_path = file_path
        self.df = None
        self.cdf = None
        self.cdf_scaled = None
        self.scaler = None
        self.models = {}

    def load_data(self):
        """Load and display initial data"""
        self.df = pd.read_csv(self.file_path)
        print("Dataset shape:", self.df.shape)
        print("\nFirst 5 rows:")
        print(self.df.head())
        return self.df

    def clean_data(self, max_area_threshold=300):
        """Clean and preprocess the data"""
        # Select relevant columns
        self.cdf = self.df[['Area', 'Room', 'Parking', 'Warehouse', 'Elevator',
                           'Address', 'Price', 'Price(USD)']].copy()

        # Remove empty addresses
        self.cdf = self.cdf[self.cdf['Address'].notna()]

        # Encode address
        le = LabelEncoder()
        self.cdf['Address_encoded'] = le.fit_transform(self.cdf['Address'])

        # Convert area to numeric and filter unreasonable values
        self.cdf['Area'] = pd.to_numeric(self.cdf['Area'], errors='coerce')
        self.cdf = self.cdf[(self.cdf['Area'] > 10) & (self.cdf['Area'] <= max_area_threshold)]

        # Convert boolean columns to integers
        self.cdf['Parking'] = self.cdf['Parking'].astype(int)
        self.cdf['Warehouse'] = self.cdf['Warehouse'].astype(int)
        self.cdf['Elevator'] = self.cdf['Elevator'].astype(int)

        # Drop original address column
        self.cdf = self.cdf.drop(["Address"], axis=1)

        print("Cleaned data shape:", self.cdf.shape)
        print("\nCleaned data summary:")
        print(self.cdf.describe())

        return self.cdf

    def explore_data(self):
        """Explore data through visualization"""
        # Histogram of Area
        plt.figure(figsize=(10, 6))
        self.cdf['Area'].hist(bins=30)
        plt.title('Distribution of Area')
        plt.xlabel('Area')
        plt.ylabel('Frequency')
        plt.show()

        # Correlation heatmap
        plt.figure(figsize=(12, 8))
        corr = self.cdf.corr()
        sns.heatmap(corr, mask=np.zeros_like(corr, dtype=bool),
                   cmap=sns.diverging_palette(220, 10, as_cmap=True),
                   square=True, annot=True, fmt=".2f")
        plt.title('Feature Correlation Heatmap')
        plt.tight_layout()
        plt.show()

    def feature_selection(self):
        """Perform feature selection"""
        X_all = self.cdf.drop(["Price(USD)", "Price"], axis=1)
        y = self.cdf["Price"]

        # Univariate feature selection
        print("=== Univariate Feature Selection ===")
        feature_selector = SelectKBest(f_regression, k="all")
        fit = feature_selector.fit(X_all, y)

        p_values = pd.DataFrame(fit.pvalues_)
        scores = pd.DataFrame(fit.scores_)
        input_variable_names = pd.DataFrame(X_all.columns)
        summary_stats = pd.concat([input_variable_names, p_values, scores], axis=1)
        summary_stats.columns = ["input_variable", "p_value", "f_score"]
        summary_stats.sort_values(by="p_value", inplace=True)

        p_value_threshold = 0.05
        score_threshold = 4
        selected_variables = summary_stats.loc[
            (summary_stats["f_score"] >= score_threshold) &
            (summary_stats["p_value"] <= p_value_threshold)
        ]
        selected_variables = selected_variables["input_variable"].tolist()

        print("Selected features:", selected_variables)
        print("\nFeature statistics:")
        print(summary_stats)

        # Recursive Feature Elimination
        print("\n=== Recursive Feature Elimination with CV ===")
        regressor = LinearRegression()
        feature_selector_rfe = RFECV(regressor, cv=5)
        fit_rfe = feature_selector_rfe.fit(X_all, y)

        optimal_feature_count = feature_selector_rfe.n_features_
        print(f"Optimal number of features: {optimal_feature_count}")

        # Plot RFECV results
        plt.figure(figsize=(10, 6))
        mean_scores = fit_rfe.cv_results_['mean_test_score']
        plt.plot(range(1, len(mean_scores) + 1), mean_scores, marker="o")
        plt.ylabel("Model Score")
        plt.xlabel("Number of Features")
        plt.title(f"Feature Selection using RFECV\nOptimal features: {optimal_feature_count} "
                 f"(score: {round(max(mean_scores), 4)})")
        plt.tight_layout()
        plt.show()

        return selected_variables

    def normalize_data(self, method='standard'):
        """Normalize the data"""
        cols = ['Area', 'Room', 'Parking', 'Warehouse', 'Elevator', 'Price']

        self.cdf_scaled = self.cdf.copy()

        if method == 'standard':
            self.scaler = StandardScaler()
        elif method == 'minmax':
            self.scaler = MinMaxScaler()

        self.cdf_scaled[cols] = self.scaler.fit_transform(self.cdf[cols])

        print(f"Data normalized using {method} scaling")
        print(self.cdf_scaled.head())

        # Plot normalized distributions
        self.cdf_scaled.hist(figsize=(12, 10))
        plt.suptitle('Normalized Feature Distributions')
        plt.tight_layout()
        plt.show()

        return self.cdf_scaled

    def visualize_relationships(self):
        """Visualize relationships between features and target"""
        plt.figure(figsize=(12, 8))

        colors = ['b', 'r', 'y', 'm', 'k']
        features = ['Area', 'Room', 'Parking', 'Warehouse', 'Elevator']

        for feature, color in zip(features, colors):
            plt.scatter(self.cdf_scaled[feature], self.cdf_scaled['Price'],
                       color=color, alpha=0.6, label=feature)

        plt.xlabel('Features (Normalized)')
        plt.ylabel('Price (Normalized)')
        plt.title('Feature vs Price Relationships')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

    def prepare_data(self, test_size=0.2):
        """Prepare train-test split"""
        # Use all features for modeling
        features = ['Area', 'Room', 'Parking', 'Warehouse', 'Elevator']

        X = np.asanyarray(self.cdf_scaled[features])
        y = np.asanyarray(self.cdf_scaled[['Price']])

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )

        print(f"Training set: {X_train.shape}")
        print(f"Test set: {X_test.shape}")

        return X_train, X_test, y_train, y_test

    def train_multiple_linear_regression(self, X_train, X_test, y_train, y_test):
        """Train multiple linear regression model"""
        print("=== Multiple Linear Regression ===")

        regr = LinearRegression()
        regr.fit(X_train, y_train)
        y_pred = regr.predict(X_test)

        # Store model
        self.models['multiple_linear'] = {
            'model': regr,
            'predictions': y_pred,
            'X_test': X_test,  # Store X_test for evaluation
            'y_test': y_test,  # Store y_test for evaluation
            'features': ['Area', 'Room', 'Parking', 'Warehouse', 'Elevator']
        }

        # Plot results
        self._plot_predictions(y_test, y_pred, "Multiple Linear Regression")

        # Print evaluation
        self._print_evaluation(regr, X_test, y_test, y_pred, "Multiple Linear Regression")

        return regr, y_pred

    def train_polynomial_regression_area(self, train_data, test_data, y_train, y_test):
        """Train polynomial regression with Area feature"""
        print("\n=== Polynomial Regression (Area only) ===")

        # Select variables
        lin_col = ['Parking', 'Warehouse', 'Elevator', 'Room']
        poly_col = ['Area']

        linear_x_train = np.asanyarray(train_data[lin_col])
        linear_x_test = np.asanyarray(test_data[lin_col])
        poly_x_train = np.asanyarray(train_data[poly_col])
        poly_x_test = np.asanyarray(test_data[poly_col])

        # Generate polynomial features
        poly = PolynomialFeatures(degree=2, include_bias=False)
        poly_x_area = poly.fit_transform(poly_x_train)
        poly_x_area_t = poly.fit_transform(poly_x_test)

        # Combine features
        X_train_poly = np.append(linear_x_train, poly_x_area, axis=1)
        X_test_poly = np.append(linear_x_test, poly_x_area_t, axis=1)

        # Train model
        clf = LinearRegression()
        clf.fit(X_train_poly, y_train)
        y_pred = clf.predict(X_test_poly)

        # Store model
        self.models['poly_area'] = {
            'model': clf,
            'predictions': y_pred,
            'X_test': X_test_poly,  # Store X_test for evaluation
            'y_test': y_test,       # Store y_test for evaluation
            'features': lin_col + ['Area', 'Area^2']
        }

        # Plot results
        self._plot_predictions(y_test, y_pred, "Polynomial Regression (Area)")

        # Print evaluation
        self._print_evaluation(clf, X_test_poly, y_test, y_pred, "Polynomial Regression (Area)")

        return clf, y_pred

    def train_advanced_polynomial_regression(self, train_data, test_data, y_train, y_test):
        """Train advanced polynomial regression with feature engineering"""
        print("\n=== Advanced Polynomial Regression ===")

        # Select variables
        lin_col = ['Room']
        poly_col = ['Area']
        non_lin_col = ['Parking', 'Warehouse', 'Elevator']

        linear_x_train = np.asanyarray(train_data[lin_col])
        linear_x_test = np.asanyarray(test_data[lin_col])
        poly_x_train = np.asanyarray(train_data[poly_col])
        poly_x_test = np.asanyarray(test_data[poly_col])
        non_lin_x_train = np.asanyarray(train_data[non_lin_col])
        non_lin_x_test = np.asanyarray(test_data[non_lin_col])

        # Generate polynomial features for Area
        poly_area = PolynomialFeatures(degree=2, include_bias=False)
        poly_x_area = poly_area.fit_transform(poly_x_train)
        poly_x_area_t = poly_area.fit_transform(poly_x_test)

        # Generate interaction features for non-linear variables
        poly_interaction = PolynomialFeatures(degree=3, interaction_only=True, include_bias=False)
        non_linear_features = poly_interaction.fit_transform(non_lin_x_train)
        non_linear_features_t = poly_interaction.fit_transform(non_lin_x_test)

        # Combine all features
        X_train_adv = np.concatenate((linear_x_train, poly_x_area, non_linear_features), axis=1)
        X_test_adv = np.concatenate((linear_x_test, poly_x_area_t, non_linear_features_t), axis=1)

        # Train model
        clf_adv = LinearRegression()
        clf_adv.fit(X_train_adv, y_train)
        y_pred = clf_adv.predict(X_test_adv)

        # Store model
        self.models['advanced_poly'] = {
            'model': clf_adv,
            'predictions': y_pred,
            'X_test': X_test_adv,  # Store X_test for evaluation
            'y_test': y_test,      # Store y_test for evaluation
            'features': lin_col + ['Area', 'Area^2'] + ['Interaction_features']
        }

        # Plot results
        self._plot_predictions(y_test, y_pred, "Advanced Polynomial Regression")

        # Print evaluation
        self._print_evaluation(clf_adv, X_test_adv, y_test, y_pred, "Advanced Polynomial Regression")

        return clf_adv, y_pred

    def _plot_predictions(self, y_true, y_pred, title):
        """Helper function to plot predictions vs actual values"""
        plt.figure(figsize=(10, 6))
        plt.scatter(np.arange(len(y_true)), y_true, color='red', alpha=0.7, label='Actual', s=20)
        plt.scatter(np.arange(len(y_pred)), y_pred, color='blue', alpha=0.7, label='Predicted', s=20)
        plt.ylabel('Price (Normalized)')
        plt.xlabel('Sample Index')
        plt.title(f'{title} - Predictions vs Actual')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

    def _print_evaluation(self, model, X_test, y_true, y_pred, model_name):
        """Helper function to print model evaluation metrics"""
        mse = mean_squared_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)

        print(f"\n{model_name} Evaluation:")
        print(f"Coefficients shape: {model.coef_.shape}")
        print(f"Intercept: {model.intercept_}")
        print(f"Mean Squared Error: {mse:.6f}")
        print(f"R² Score: {r2:.4f}")
        print("-" * 50)

    def compare_models(self):
        """Compare performance of all trained models"""
        if not self.models:
            print("No models trained yet!")
            return

        print("\n" + "="*60)
        print("MODEL COMPARISON SUMMARY")
        print("="*60)

        comparison_data = []

        for model_name, model_info in self.models.items():
            y_true = model_info['y_test']
            y_pred = model_info['predictions']

            mse = mean_squared_error(y_true, y_pred)
            r2 = r2_score(y_true, y_pred)

            comparison_data.append({
                'Model': model_name,
                'MSE': mse,
                'R² Score': r2,
                'Features': ', '.join(str(f) for f in model_info['features'][:3]) + '...'
            })

            print(f"\n{model_name.upper():<40}")
            print(f"  Features: {model_info['features']}")
            print(f"  MSE: {mse:.6f}")
            print(f"  R² Score: {r2:.4f}")

        # Create comparison dataframe
        comparison_df = pd.DataFrame(comparison_data)
        print("\nComparison Table:")
        print(comparison_df.to_string(index=False))

        print("\n" + "="*60)


def main():
    """Main function to run the house price prediction project"""

    # Initialize predictor
    predictor = HousePricePredictor("housePrice.csv")

    try:
        # Step 1: Load and clean data
        print("STEP 1: Loading and cleaning data...")
        predictor.load_data()
        predictor.clean_data()

        # Step 2: Explore data
        print("\nSTEP 2: Exploring data...")
        predictor.explore_data()

        # Step 3: Feature selection
        print("\nSTEP 3: Performing feature selection...")
        selected_features = predictor.feature_selection()

        # Step 4: Normalize data
        print("\nSTEP 4: Normalizing data...")
        predictor.normalize_data(method='minmax')

        # Step 5: Visualize relationships
        print("\nSTEP 5: Visualizing feature relationships...")
        predictor.visualize_relationships()

        # Step 6: Prepare data
        print("\nSTEP 6: Preparing data for modeling...")
        X_train, X_test, y_train, y_test = predictor.prepare_data(test_size=0.2)

        # Create consistent train/test split for all models
        train_mask = np.random.rand(len(predictor.cdf_scaled)) < 0.8
        train_data = predictor.cdf_scaled[train_mask]
        test_data = predictor.cdf_scaled[~train_mask]

        # Prepare data for polynomial models
        y_train_poly = np.asanyarray(train_data[['Price']])
        y_test_poly = np.asanyarray(test_data[['Price']])

        # Step 7: Train models
        print("\nSTEP 7: Training models...")

        # Multiple Linear Regression
        predictor.train_multiple_linear_regression(X_train, X_test, y_train, y_test)

        # Polynomial Regression (Area)
        predictor.train_polynomial_regression_area(train_data, test_data, y_train_poly, y_test_poly)

        # Advanced Polynomial Regression
        predictor.train_advanced_polynomial_regression(train_data, test_data, y_train_poly, y_test_poly)

        # Step 8: Compare models
        print("\nSTEP 8: Comparing models...")
        predictor.compare_models()

        print("\nProject completed successfully!")

    except Exception as e:
        print(f"Error occurred: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()