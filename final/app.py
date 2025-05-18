import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from statsmodels.stats.proportion import proportions_ztest
import seaborn as sns

# Load data
df = pd.read_csv('./final/cleaned_twitter_sentiment.csv')
df = df[df['text'].apply(lambda x: isinstance(x, str))]
df['length'] = df['text'].apply(len)

# 1. Title + Intro
st.title("📊 Twitter Sentiment Analysis Dashboard")
st.markdown("""
This dashboard visualizes public sentiment toward various entities based on Twitter data.

We explore:
- Overall sentiment distribution
- Word cloud analysis
- Entity-level sentiment breakdown
- A deep dive into a specific entity
- Behavioral insight: tweet length per sentiment
""")

# 2. Overall Sentiment Distribution

st.header("🔍 Overall Sentiment Distribution")
sentiment_counts = df['sentiment'].value_counts()
fig, ax = plt.subplots()
sentiment_counts.plot(kind='bar', color='skyblue', ax=ax)
plt.title("Sentiment Counts")
st.pyplot(fig)

# 3. Explore by Entity

st.header("🏷️ Sentiment Breakdown by Entity")
top_entities = df['entity'].value_counts().head(10).index.tolist()
selected_entity = st.selectbox("Select an Entity", top_entities)

filtered = df[df['entity'] == selected_entity]
entity_counts = filtered['sentiment'].value_counts()

fig, ax = plt.subplots()
entity_counts.plot(kind='bar', color='lightcoral', ax=ax)
plt.title(f"Sentiment for {selected_entity}")
st.pyplot(fig)

# Z-Test Section
st.subheader("📏 Z-Test: Negative vs Positive Sentiment")

# Filter selected entity's data
entity_data = df[df['entity'] == selected_entity]
neg_count = (entity_data['sentiment'] == 'Negative').sum()
pos_count = (entity_data['sentiment'] == 'Positive').sum()
total_count = len(entity_data)

# Prepare for Z-Test
count = [neg_count, pos_count]
nobs = [total_count, total_count]

# Run Z-Test (comparing if Negative > Positive)
z_stat, p_val = proportions_ztest(count, nobs, alternative='larger')

# Display results
st.markdown(f"**Z-Score:** `{z_stat:.2f}`")
st.markdown(f"**P-Value:** `{p_val:.4f}`")

# Interpret result
if p_val < 0.05:
    st.success("**Conclusion:** Negative sentiment is significantly higher than Positive.")
else:
    st.info("**Conclusion:** No significant difference — Positive sentiment may dominate or they are similar.")

# 4. Word Cloud
st.header("☁️ Word Cloud by Sentiment")
sentiment_choice = st.selectbox("Choose sentiment", ["Positive", "Negative"])
text = ' '.join(df[df['sentiment'] == sentiment_choice]['text'])

stopwords = set(STOPWORDS)
stopwords.update(['game', 'pic', 'twitter'])

wc = WordCloud(width=800, height=400, stopwords=stopwords).generate(text)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wc, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

# 5. Tweet Length vs Sentiment

st.header("✏️ Tweet Length by Sentiment")

avg_len = df.groupby('sentiment')['length'].mean().sort_values()
fig, ax = plt.subplots()
avg_len.plot(kind='bar', color='mediumseagreen', ax=ax)
plt.title("Average Tweet Length per Sentiment")
st.pyplot(fig)

