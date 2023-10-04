# hack2023-umass
# Movie Recommendation System using Collaborative Filtering

This system block implements a basic movie recommendation system using Collaborative Filtering. It leverages the MovieLens dataset (ml-100k) to suggest movies similar to a user's input.

## Link to Dataset
- https://grouplens.org/datasets/movielens/100k/

## Dependencies

Make sure you have the following Python libraries installed:

- `numpy` - for numerical operations.
- `pandas` - for data manipulation and analysis.
- `streamlit` - for building interactive web apps.
- `warnings` - for suppressing warnings.

You can install these libraries using `pip`:

```bash
pip install numpy pandas streamlit
```

## Data Preparation

1. Two datasets are imported:
   - `u.data`: Contains user-item ratings.
   - `u.item`: Contains movie information.
2. The datasets are merged on the 'item_id' column to combine movie information with user ratings.
3. Timestamps are dropped as they are not needed for this recommendation system.

## Recommendation System

1. User is prompted to input a movie name and year (e.g., 'Star Wars (1977)').
2. The code calculates movie ratings correlation using collaborative filtering.
3. It then suggests movies that are most similar to the input movie based on user ratings.
4. The top recommended movies are displayed to the user.

## Movie Ratings and Votes

1. The code also calculates the average rating and the number of votes for each movie.
2. It displays the most voted on films based on user ratings.

## Output

The final output includes a list of recommended movies that are similar to the user's input. These recommendations are based on the correlation of user ratings.

## Usage

1. Run the code, and it will start a Streamlit web app.
2. Enter a movie name and year in the text input field.
3. The system will provide a list of recommended movies based on user ratings correlation.

## Contributing

Feel free to contribute to this code block by improving the recommendation algorithm or adding more features to the web app.

## License

This code block is open-source and available under the [MIT License](LICENSE).

---
