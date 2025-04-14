<div align="center">
  <h1>🎧 Decoding and Predicting Spotify Song Popularity with Machine Learning 🎵</h1>
  <p>Unveiling the sonic secrets behind a hit song</p>
</div>

---

## 🚀 Project Overview

This project delves into the Spotify Tracks Dataset from Kaggle to explore the relationship between musical features and song popularity. By employing Python, Pandas, Seaborn, Matplotlib, scikit-learn, and SQL, we aim to:

* Understand how different audio characteristics (e.g., danceability, energy) influence a song's popularity.
* Develop a machine learning model to predict song popularity based on these features.
* Analyze genre-specific popularity trends.

This repository contains the code and resources for data cleaning, exploratory data analysis (EDA), feature engineering and machine learning model building

## 🛠️ Technologies Used

* **Python:** The core programming language for data manipulation, analysis, and machine learning.
* **Pandas:** For efficient data loading, cleaning, and manipulation.
* **NumPy:** For numerical operations, especially during log transformation.
* **Seaborn:** For creating informative and visually appealing statistical visualizations.
* **Matplotlib:** For foundational plotting and customization.
* **scikit-learn:** For machine learning model development and evaluation.
* **(Optional) boto3:** For interacting with AWS S3 (if implemented).


## ⚙️ Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/agajankush/spotify-music-eda.git](https://github.com/agajankush/spotify-music-eda.git)
    cd spotify-music-eda
    ```

2.  **Install the required Python libraries:**

    ```bash
    pip install -r requirements.in
    ```

3.  **Download the dataset:**

    * Download the `SpotifyFeatures.csv` file from the Kaggle link: [https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)
    * Place the `SpotifyFeatures.csv` file in the `data/` directory (you might need to create this directory).

## ▶️ Running the Code

The analysis can be run using the provided Python scripts. You can execute each script sequentially:

There is only one file to understand this project,
* * Open data_analysis.ipynb in Jupyter Notebook and run each cell manually to see the output.

## 📊 Key Findings

*(This section will be populated with the most significant findings from your analysis. Examples:*

* * `Danceability`, `energy`, and `loudness` are significant predictors of a song's popularity.
* * A Random Forest Regressor model achieved an R-squared score of 0.XX in predicting song popularity.
* * Certain genres (e.g., 'pop', 'hip-hop') tend to have higher average popularity.
* * Log transformation improved the model's ability to handle the skewness in the popularity distribution.
* * Violin plots showed the distribution of 'danceability' varies significantly across genres.*)

## 📈 Model Performance

* * R-squared: 0.9999999997000221
* * Mean Squared Error (MSE): 2.0196082673124275e-10
* * Mean Absolute Error (MAE): 1.6490552390970118e-07

## 🔮 Future Enhancements

* Explore other machine learning models (e.g., Gradient Boosting).
* Perform hyperparameter tuning to optimize model performance.
* Analyze time-based trends in popularity.
* Investigate the impact of artist popularity on song popularity.
* Develop a web application to visualize and interact with the results.
* Implement a song recommendation system based on audio features.

## 🙌 Contributing

Contributions to this project are welcome! If you have suggestions for improvements, new analyses, or bug fixes, please feel free to submit a pull request.

## 📄 License

[Your License] (e.g., MIT License)

## 📧 Contact

Ashutosh Gajankush - agajankush.github@gmail.com - https://www.linkedin.com/in/ashutoshgajankush

---

<div align="center">
  <p>Thank you for exploring this project! Feel free to connect and share your thoughts.</p>
</div>
