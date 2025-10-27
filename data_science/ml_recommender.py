"""
Movie Recommendation System
Content-Based and Collaborative Filtering Approaches

⚙️ This script was AI-assisted, generated and refined with the help of ChatGPT to accelerate learning and documentation.
"""

import numpy as np
import pandas as pd
from math import sqrt
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:
    def __init__(self, movies_file='movies.csv', ratings_file='ratings.csv'):
        self.movies_file = movies_file
        self.ratings_file = ratings_file
        self.movies_df = None
        self.ratings_df = None
        self.movies_with_genres_df = None

    def load_and_clean_data(self):
        """Load and clean the movie and ratings data"""
        # Load data
        self.movies_df = pd.read_csv(self.movies_file)
        self.ratings_df = pd.read_csv(self.ratings_file)

        print("Original movies data shape:", self.movies_df.shape)
        print("Original ratings data shape:", self.ratings_df.shape)

        # Extract year from title
        self.movies_df['year'] = self.movies_df.title.str.extract('(\(\\d\\d\\d\\d\))', expand=False)
        self.movies_df['year'] = self.movies_df.year.str.extract('(\\d\\d\\d\\d)', expand=False)
        self.movies_df['title'] = self.movies_df.title.str.replace('(\(\\d\\d\\d\\d\))', '', regex=True)
        self.movies_df['title'] = self.movies_df['title'].apply(lambda x: x.strip())

        # Split genres into lists
        self.movies_df['genres'] = self.movies_df.genres.str.split('|')

        # Create genre matrix
        self._create_genre_matrix()

        # Clean ratings data
        self.ratings_df = self.ratings_df.drop('timestamp', axis=1)

        # Ensure proper data types
        self.ratings_df['userId'] = self.ratings_df['userId'].astype(int)
        self.ratings_df['movieId'] = self.ratings_df['movieId'].astype(int)
        self.movies_df['movieId'] = self.movies_df['movieId'].astype(int)

        return self.movies_df, self.ratings_df

    def _create_genre_matrix(self):
        """Create one-hot encoded matrix for genres"""
        # Copy the movie dataframe
        self.movies_with_genres_df = self.movies_df.copy()

        # Create genre columns
        all_genres = set()
        for genres_list in self.movies_df['genres']:
            all_genres.update(genres_list)

        # Initialize all genre columns with 0
        for genre in all_genres:
            self.movies_with_genres_df[genre] = 0

        # Set genre values to 1
        for index, row in self.movies_df.iterrows():
            for genre in row['genres']:
                self.movies_with_genres_df.at[index, genre] = 1

        print(f"Created genre matrix with {len(all_genres)} genres")

    def get_user_input(self, user_ratings):
        """
        Process user input ratings

        Args:
            user_ratings (list): List of dictionaries with 'title' and 'rating'

        Returns:
            pd.DataFrame: Processed user input
        """
        input_movies = pd.DataFrame(user_ratings)

        # Filter movies by title and merge
        input_ids = self.movies_df[self.movies_df['title'].isin(input_movies['title'].tolist())]
        input_movies = pd.merge(input_ids, input_movies)

        # Drop unnecessary columns
        input_movies = input_movies.drop('genres', axis=1).drop('year', axis=1)

        # Ensure proper data types
        input_movies['movieId'] = input_movies['movieId'].astype(int)
        input_movies['rating'] = input_movies['rating'].astype(float)

        print(f"Processed {len(input_movies)} user ratings")
        return input_movies

    def content_based_recommendation(self, user_ratings, top_n=20):
        """
        Generate content-based recommendations

        Args:
            user_ratings (list): User's movie ratings
            top_n (int): Number of recommendations to return

        Returns:
            pd.DataFrame: Recommended movies
        """
        print("=== Content-Based Recommendation ===")

        # Process user input
        input_movies = self.get_user_input(user_ratings)

        # Get movies with genres that user has rated
        user_movies = self.movies_with_genres_df[
            self.movies_with_genres_df['movieId'].isin(input_movies['movieId'].tolist())
        ].reset_index(drop=True)

        # Create user genre profile
        user_genre_table = user_movies.drop(['movieId', 'title', 'genres', 'year'], axis=1)
        user_profile = user_genre_table.T.dot(input_movies['rating'])

        # Get genre table for all movies
        genre_table = self.movies_with_genres_df.set_index('movieId')
        genre_table = genre_table.drop(['title', 'genres', 'year'], axis=1)

        # Calculate recommendation scores
        recommendation_scores = (genre_table * user_profile).sum(axis=1) / user_profile.sum()
        recommendation_scores = recommendation_scores.sort_values(ascending=False)

        # Get top recommendations (exclude movies user already rated)
        user_rated_movies = input_movies['movieId'].tolist()
        top_recommendations = recommendation_scores[~recommendation_scores.index.isin(user_rated_movies)].head(top_n)

        recommended_movies = self.movies_df[
            self.movies_df['movieId'].isin(top_recommendations.index)
        ].copy()
        recommended_movies['recommendation_score'] = recommended_movies['movieId'].map(top_recommendations)

        return recommended_movies.sort_values('recommendation_score', ascending=False)

    def collaborative_filtering_recommendation(self, user_ratings, top_n=10, similar_users=100):
        """
        Generate collaborative filtering recommendations

        Args:
            user_ratings (list): User's movie ratings
            top_n (int): Number of recommendations to return
            similar_users (int): Number of similar users to consider

        Returns:
            pd.DataFrame: Recommended movies
        """
        print("=== Collaborative Filtering Recommendation ===")

        # Process user input
        input_movies = self.get_user_input(user_ratings)

        # Find users who rated the same movies
        user_subset = self.ratings_df[
            self.ratings_df['movieId'].isin(input_movies['movieId'].tolist())
        ]

        # Group by user and sort by number of common movies
        user_subset_group = list(user_subset.groupby(['userId']))
        user_subset_group = sorted(user_subset_group, key=lambda x: len(x[1]), reverse=True)
        user_subset_group = user_subset_group[:similar_users]

        # Calculate Pearson correlation
        pearson_correlation_dict = {}

        for user_id, group in user_subset_group:
            group = group.sort_values(by='movieId')
            input_movies_sorted = input_movies.sort_values(by='movieId')

            n_ratings = len(group)
            temp_df = input_movies_sorted[
                input_movies_sorted['movieId'].isin(group['movieId'].tolist())
            ]

            if len(temp_df) == 0:
                continue

            temp_rating_list = temp_df['rating'].tolist()
            temp_group_list = group['rating'].tolist()

            # Calculate Pearson correlation
            Sxx = sum([i**2 for i in temp_rating_list]) - pow(sum(temp_rating_list), 2) / float(n_ratings)
            Syy = sum([i**2 for i in temp_group_list]) - pow(sum(temp_group_list), 2) / float(n_ratings)
            Sxy = sum(i*j for i, j in zip(temp_rating_list, temp_group_list)) - sum(temp_rating_list) * sum(temp_group_list) / float(n_ratings)

            if Sxx != 0 and Syy != 0:
                pearson_correlation_dict[user_id] = Sxy / sqrt(Sxx * Syy)
            else:
                pearson_correlation_dict[user_id] = 0

        # Create correlation dataframe
        pearson_df = pd.DataFrame.from_dict(pearson_correlation_dict, orient='index', columns=['similarityIndex'])
        pearson_df['userId'] = pearson_df.index
        pearson_df.index = range(len(pearson_df))

        # Ensure proper data types for merging
        pearson_df['userId'] = pearson_df['userId'].astype(int)

        # Get top similar users
        top_users = pearson_df.sort_values(by='similarityIndex', ascending=False).head(50)

        if len(top_users) == 0:
            print("No similar users found. Returning empty recommendations.")
            return pd.DataFrame(columns=['movieId', 'title', 'year', 'weighted_average_score'])

        # Get ratings from top users
        top_users_rating = top_users.merge(
            self.ratings_df,
            on='userId',
            how='inner'
        )

        # Calculate weighted ratings
        top_users_rating['weightedRating'] = top_users_rating['similarityIndex'] * top_users_rating['rating']

        # Calculate recommendation scores
        temp_top_users_rating = top_users_rating.groupby('movieId').agg({
            'similarityIndex': 'sum',
            'weightedRating': 'sum'
        }).reset_index()
        temp_top_users_rating.columns = ['movieId', 'sum_similarityIndex', 'sum_weightedRating']

        # Filter out zero similarity to avoid division by zero
        temp_top_users_rating = temp_top_users_rating[temp_top_users_rating['sum_similarityIndex'] > 0]

        if len(temp_top_users_rating) == 0:
            print("No valid recommendations found. Returning empty results.")
            return pd.DataFrame(columns=['movieId', 'title', 'year', 'weighted_average_score'])

        # Calculate weighted average
        temp_top_users_rating['weighted_average_score'] = (
            temp_top_users_rating['sum_weightedRating'] / temp_top_users_rating['sum_similarityIndex']
        )

        # Filter out movies user has already rated
        user_rated_movies = input_movies['movieId'].tolist()
        recommendation_df = temp_top_users_rating[~temp_top_users_rating['movieId'].isin(user_rated_movies)]

        # Get top recommendations
        recommendation_df = recommendation_df.sort_values(by='weighted_average_score', ascending=False)
        top_recommendations = recommendation_df.head(top_n)

        if len(top_recommendations) == 0:
            print("No new recommendations found after filtering rated movies.")
            return pd.DataFrame(columns=['movieId', 'title', 'year', 'weighted_average_score'])

        # Get movie details
        recommended_movies = self.movies_df[
            self.movies_df['movieId'].isin(top_recommendations['movieId'])
        ].copy()
        recommended_movies = recommended_movies.merge(
            top_recommendations[['movieId', 'weighted_average_score']],
            on='movieId'
        )

        return recommended_movies.sort_values('weighted_average_score', ascending=False)

    def hybrid_recommendation(self, user_ratings, content_weight=0.6, collab_weight=0.4, top_n=15):
        """
        Generate hybrid recommendations combining both approaches

        Args:
            user_ratings (list): User's movie ratings
            content_weight (float): Weight for content-based recommendations
            collab_weight (float): Weight for collaborative filtering
            top_n (int): Number of recommendations to return

        Returns:
            pd.DataFrame: Recommended movies
        """
        print("=== Hybrid Recommendation ===")

        # Get recommendations from both methods
        content_rec = self.content_based_recommendation(user_ratings, top_n=50)
        collab_rec = self.collaborative_filtering_recommendation(user_ratings, top_n=50)

        # Create hybrid scores
        hybrid_scores = {}

        # Add content-based scores
        for _, row in content_rec.iterrows():
            movie_id = row['movieId']
            score = row['recommendation_score'] * content_weight
            hybrid_scores[movie_id] = score

        # Add collaborative filtering scores
        for _, row in collab_rec.iterrows():
            movie_id = row['movieId']
            score = row['weighted_average_score'] * collab_weight
            if movie_id in hybrid_scores:
                hybrid_scores[movie_id] += score
            else:
                hybrid_scores[movie_id] = score

        # Convert to dataframe and sort
        hybrid_df = pd.DataFrame.from_dict(hybrid_scores, orient='index', columns=['hybrid_score'])
        hybrid_df['movieId'] = hybrid_df.index
        hybrid_df = hybrid_df.sort_values('hybrid_score', ascending=False).head(top_n)

        if len(hybrid_df) == 0:
            print("No hybrid recommendations found.")
            return pd.DataFrame(columns=['movieId', 'title', 'year', 'hybrid_score'])

        # Get movie details
        recommended_movies = self.movies_df[
            self.movies_df['movieId'].isin(hybrid_df['movieId'])
        ].copy()
        recommended_movies = recommended_movies.merge(hybrid_df, on='movieId')

        return recommended_movies.sort_values('hybrid_score', ascending=False)

    def evaluate_recommendations(self, user_ratings, methods=['content', 'collaborative', 'hybrid']):
        """
        Evaluate and compare different recommendation methods
        """
        print("\n" + "="*60)
        print("RECOMMENDATION SYSTEM EVALUATION")
        print("="*60)

        results = {}

        if 'content' in methods:
            try:
                content_rec = self.content_based_recommendation(user_ratings)
                results['Content-Based'] = content_rec
                print(f"\nContent-Based Recommendations ({len(content_rec)} movies):")
                if len(content_rec) > 0:
                    print(content_rec[['title', 'year', 'recommendation_score']].head(10).to_string(index=False))
                else:
                    print("No content-based recommendations found.")
            except Exception as e:
                print(f"Error in content-based recommendation: {e}")
                results['Content-Based'] = pd.DataFrame()

        if 'collaborative' in methods:
            try:
                collab_rec = self.collaborative_filtering_recommendation(user_ratings)
                results['Collaborative Filtering'] = collab_rec
                print(f"\nCollaborative Filtering Recommendations ({len(collab_rec)} movies):")
                if len(collab_rec) > 0:
                    print(collab_rec[['title', 'year', 'weighted_average_score']].head(10).to_string(index=False))
                else:
                    print("No collaborative filtering recommendations found.")
            except Exception as e:
                print(f"Error in collaborative filtering recommendation: {e}")
                results['Collaborative Filtering'] = pd.DataFrame()

        if 'hybrid' in methods:
            try:
                hybrid_rec = self.hybrid_recommendation(user_ratings)
                results['Hybrid'] = hybrid_rec
                print(f"\nHybrid Recommendations ({len(hybrid_rec)} movies):")
                if len(hybrid_rec) > 0:
                    print(hybrid_rec[['title', 'year', 'hybrid_score']].head(10).to_string(index=False))
                else:
                    print("No hybrid recommendations found.")
            except Exception as e:
                print(f"Error in hybrid recommendation: {e}")
                results['Hybrid'] = pd.DataFrame()

        return results

    def get_movie_suggestions(self, query, top_k=5):
        """
        Get movie suggestions based on title search
        """
        matches = self.movies_df[
            self.movies_df['title'].str.contains(query, case=False, na=False)
        ].head(top_k)

        return matches[['movieId', 'title', 'year', 'genres']]

    def display_user_ratings(self, user_ratings):
        """Display the user's input ratings"""
        print("\nUser Ratings:")
        print("-" * 40)
        for rating in user_ratings:
            print(f"  - {rating['title']}: {rating['rating']}/5")


def main():
    """Main function to demonstrate the movie recommendation system"""

    # Initialize recommender
    recommender = MovieRecommender()

    try:
        # Load and clean data
        print("Loading and cleaning data...")
        movies_df, ratings_df = recommender.load_and_clean_data()

        # Sample user ratings
        user_ratings = [
            {'title': 'Breakfast Club, The', 'rating': 5},
            {'title': 'Toy Story', 'rating': 3.5},
            {'title': 'Jumanji', 'rating': 2},
            {'title': 'Pulp Fiction', 'rating': 5},
            {'title': 'Akira', 'rating': 4.5}
        ]

        # Display user ratings
        recommender.display_user_ratings(user_ratings)

        # Evaluate different recommendation methods
        results = recommender.evaluate_recommendations(
            user_ratings,
            methods=['content', 'collaborative', 'hybrid']
        )

        # Display summary
        print("\n" + "="*60)
        print("RECOMMENDATION SUMMARY")
        print("="*60)

        for method, recommendations in results.items():
            print(f"\n{method}:")
            print(f"  Number of recommendations: {len(recommendations)}")
            if len(recommendations) > 0:
                top_movie = recommendations.iloc[0]
                score_column = 'recommendation_score' if method == 'Content-Based' else 'weighted_average_score' if method == 'Collaborative Filtering' else 'hybrid_score'
                score = top_movie[score_column]
                print(f"  Top recommendation: {top_movie['title']} ({top_movie['year']}) - Score: {score:.3f}")
            else:
                print(f"  No recommendations available")

        # Get movie suggestions for a query
        print("\n" + "="*60)
        print("MOVIE SUGGESTIONS FOR 'Star'")
        print("="*60)

        suggestions = recommender.get_movie_suggestions('Star')
        if len(suggestions) > 0:
            print(suggestions[['title', 'year', 'genres']].to_string(index=False))
        else:
            print("No movie suggestions found for 'Star'")

    except Exception as e:
        print(f"Error in main execution: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()