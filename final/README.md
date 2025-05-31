
# Twitter Sentiment Analysis Dashboard

This Streamlit dashboard visualizes public sentiment toward popular tech and gaming entities using Twitter data. It provides insights using natural language processing (NLP) and statistical analysis.

## Features

- **Sentiment Distribution**: Visual breakdown of positive, negative, and neutral tweets.
- **Word Cloud**: Visualizes common words by sentiment and entity.
- **Bigrams & Trigrams**: Shows frequent two- and three-word combinations.
- **Tweet Length Analysis**: Compares average tweet length by sentiment.
- **Outlier Detection**: Highlights unusually long tweets.
- **Z-Test**: Compares proportions of negative vs. positive tweets statistically.
- **ANOVA & Kruskal–Wallis Tests**: Analyzes differences in tweet lengths across sentiment categories.

## Technologies Used

- **Streamlit** – for building the interactive dashboard
- **Pandas** – for data manipulation
- **Matplotlib / Seaborn** – for plotting
- **NLTK** – for text processing
- **WordCloud** – for generating word clouds
- **Scipy / Statsmodels** – for statistical testing

## Setup Instructions

1. **Clone this repo**:

```bash
git clone https://github.com/your-username/twitter-sentiment-dashboard.git
cd twitter-sentiment-dashboard
```

2. **Create a virtual environment (optional but recommended)**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Run the app**:

```bash
streamlit run app.py
```

## 🔎 Sample Output

- Sentiment bar charts  
- Word clouds per entity & sentiment  
- Top bigrams and trigrams  
- Tweet length histograms  
- Statistical test results with conclusions

## 📝 Notes

- You may need to download NLTK data manually if running offline:
  ```python
  import nltk
  nltk.download('punkt', download_dir='nltk_data')
  nltk.download('stopwords', download_dir='nltk_data')
  nltk.download('vader_lexicon', download_dir='nltk_data')
  ```

- Make sure the `nltk_data` folder is present in the root directory or adjust the download path accordingly.