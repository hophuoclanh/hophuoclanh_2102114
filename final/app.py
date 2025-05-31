import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from statsmodels.stats.proportion import proportions_ztest
import seaborn as sns
from scipy.stats import f_oneway
from scipy.stats import levene, shapiro
from scipy.stats import kruskal


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import Counter
import re

# Force nltk to use your local folder
nltk.data.path.append('./nltk_data')

# Download required NLTK data files
nltk.download('punkt', download_dir='./nltk_data')
nltk.download('stopwords', download_dir='./nltk_data')
nltk.download('vader_lexicon', download_dir='./nltk_data')

from nltk.sentiment import SentimentIntensityAnalyzer

# Load data
df = pd.read_csv('./final/cleaned_twitter_sentiment.csv')
df = df[df['text'].apply(lambda x: isinstance(x, str))]
df['length'] = df['text'].apply(len)

# Title + Intro
st.title("📊 Twitter Sentiment Analysis Dashboard")
st.markdown("""
This dashboard visualizes public sentiment toward various entities based on Twitter data.

We explore:
- Overall sentiment distribution
- Entity-level sentiment breakdown + Z-Test
- Word Cloud
- Bigrams & Trigrams
- Tweet Length + ANOVA Test
""")

# STEP 1: Overall Sentiment Distribution
st.header("🔍 Overall Sentiment Distribution")
sentiment_counts = df['sentiment'].value_counts()
fig, ax = plt.subplots()
sentiment_counts.plot(kind='bar', color='skyblue', ax=ax)
plt.title("Sentiment Counts")
st.pyplot(fig)

# STEP 2: Word Cloud by Entity & Sentiment
st.header("☁️ Word Cloud by Entity & Sentiment")
col1, col2 = st.columns(2)

top_entities = df['entity'].value_counts().head(10).index.tolist()

with col1:
    wc_entity = st.selectbox("Choose entity", top_entities, key="wc_entity")
with col2:
    wc_sentiment = st.selectbox("Choose sentiment", ["Positive", "Negative", "Neutral"], key="wc_sentiment")

wc_filtered = df[(df['entity'] == wc_entity) & (df['sentiment'] == wc_sentiment)]
text = ' '.join(wc_filtered['text'])

stopwords_set = set(STOPWORDS)
stopwords_set.update(['game', 'pic', 'twitter'])

wc = WordCloud(width=800, height=400, stopwords=stopwords_set, background_color="black").generate(text)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wc, interpolation='bilinear')
ax.axis('off')
plt.title(f"Word Cloud for {wc_entity} — {wc_sentiment}")
st.pyplot(fig)

# STEP 2.5: Top Bigrams & Trigrams
st.header("📚 Top Bigrams & Trigrams")
st.markdown("Displays the most common two- and three-word phrases for the selected entity and sentiment.")

ngram_entity = st.selectbox("Choose entity", top_entities, key="ngram_entity")
ngram_sentiment = st.selectbox("Choose sentiment", ["Positive", "Negative", "Neutral"], key="ngram_sentiment")

filtered_ngram_df = df[(df['entity'] == ngram_entity) & (df['sentiment'] == ngram_sentiment)]
texts = filtered_ngram_df['text'].dropna().tolist()

def clean_and_tokenize(text):
    text = re.sub(r"http\S+|@\S+|[^A-Za-z0-9\s]", '', text.lower())
    tokens = text.split()
    stop_words = set(stopwords.words('english'))
    return [w for w in tokens if w.isalpha() and w not in stop_words]

all_tokens = []
for t in texts:
    all_tokens.extend(clean_and_tokenize(t))

bigrams = list(ngrams(all_tokens, 2))
trigrams = list(ngrams(all_tokens, 3))

bigram_counts = Counter(bigrams).most_common(10)
trigram_counts = Counter(trigrams).most_common(10)

st.subheader("🔹 Top 10 Bigrams")
for phrase, count in bigram_counts:
    st.write(f"{' '.join(phrase)} — {count}")

st.subheader("🔹 Top 10 Trigrams")
for phrase, count in trigram_counts:
    st.write(f"{' '.join(phrase)} — {count}")

# STEP 3: Tweet Length Distribution
st.header("📉 Tweet Length Distribution by Sentiment")
col1, col2 = st.columns(2)
with col1:
    dist_entity = st.selectbox("Choose entity to visualize", top_entities, key="dist_entity")
with col2:
    dist_sentiment = st.selectbox("Choose sentiment", ["Positive", "Negative", "Neutral"], key="dist_sentiment")

dist_df = df[(df['sentiment'] == dist_sentiment) & (df['entity'] == dist_entity)]

fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(dist_df['length'], bins=50, kde=True, ax=ax, color="mediumpurple")
plt.title(f'{dist_sentiment} Tweet Length Distribution — {dist_entity}')
plt.xlabel('Tweet Length')
plt.ylabel('Frequency')
st.pyplot(fig)

# STEP 4: Outlier Detection
st.header("🕵️‍♀️ Detect Potential Mixed or Outlier Tweets")
outlier_threshold = df['length'].quantile(0.99)
outliers = df[df['length'] > outlier_threshold]

st.markdown(f"Outliers: Tweets longer than 99th percentile (> {outlier_threshold:.0f} characters)")
st.dataframe(outliers[['entity', 'sentiment', 'length', 'text']].head(5))

# STEP 5: Z-Test
st.header("🏷️ Sentiment Breakdown by Entity")
selected_entity = st.selectbox("Select an Entity", top_entities, key="z_entity")
filtered = df[df['entity'] == selected_entity]
entity_counts = filtered['sentiment'].value_counts()

fig, ax = plt.subplots()
entity_counts.plot(kind='bar', color='lightcoral', ax=ax)
plt.title(f"Sentiment for {selected_entity}")
st.pyplot(fig)

st.subheader("📏 Z-Test: Negative vs Positive Sentiment")
neg_count = (filtered['sentiment'] == 'Negative').sum()
pos_count = (filtered['sentiment'] == 'Positive').sum()
total_count = len(filtered)

count = [neg_count, pos_count]
nobs = [total_count, total_count]

z_stat, p_val = proportions_ztest(count, nobs, alternative='larger')
st.markdown(f"**Z-Score:** `{z_stat:.2f}`")
st.markdown(f"**P-Value:** `{p_val:.4f}`")
if p_val < 0.05:
    st.success("**Conclusion:** Negative sentiment is significantly higher than Positive.")
else:
    st.info("**Conclusion:** No significant difference.")

# STEP 6: ANOVA - Tweet Length by Sentiment
st.header("✏️ Tweet Length by Sentiment")
selected_entity_length = st.selectbox("Choose an Entity for Length Analysis", top_entities, key="length_entity")
filtered_length_df = df[df['entity'] == selected_entity_length]
avg_len = filtered_length_df.groupby('sentiment')['length'].mean().sort_values()

fig, ax = plt.subplots()
avg_len.plot(kind='bar', color='mediumseagreen', ax=ax)
plt.title(f"Average Tweet Length per Sentiment — {selected_entity_length}")
plt.ylabel("Avg Length (Characters)")
st.pyplot(fig)

st.subheader("📊 ANOVA Test: Does Tweet Length Differ by Sentiment?")
groups = [group['length'].values for name, group in filtered_length_df.groupby('sentiment')]

# ✅ INSERT THIS BLOCK TO CHECK ASSUMPTIONS
st.markdown("#### ⚠️ Assumption Checks for ANOVA")

# Levene’s test for homogeneity of variance
levene_stat, levene_p = levene(*groups)
st.markdown(f"**Levene’s test for equal variances**: stat = `{levene_stat:.2f}`, p = `{levene_p:.4f}`")

# Shapiro-Wilk test for normality
for sentiment, group in filtered_length_df.groupby('sentiment'):
    stat, p = shapiro(group['length'])
    st.markdown(f"**Shapiro-Wilk for {sentiment}**: p = `{p:.4f}`")

st.subheader("🧪 Kruskal–Wallis H-Test: Non-Parametric Alternative")

# Apply the Kruskal-Wallis test to the same sentiment groups
kw_stat, kw_p_val = kruskal(*groups)

st.markdown(f"**H-Statistic:** `{kw_stat:.2f}`")
st.markdown(f"**P-Value:** `{kw_p_val:.4f}`")

if kw_p_val < 0.05:
    st.success("**Conclusion:** There is a statistically significant difference in tweet length across sentiment groups (non-parametric test).")
else:
    st.info("**Conclusion:** No significant difference found with Kruskal–Wallis test.")

