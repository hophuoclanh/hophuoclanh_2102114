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
- Sentiment distribution
- Word clouds
- Entity-specific insights
- Tweet behavior
- Statistical sentiment testing
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

# 5. Deep Dive: Borderlands + Z-Test

st.header("📌 Deep Dive: Borderlands")

borderlands = df[df['entity'] == 'Borderlands']
st.write(borderlands['sentiment'].value_counts())

# Z-Test
neg = (borderlands['sentiment'] == 'Negative').sum()
pos = (borderlands['sentiment'] == 'Positive').sum()
total = len(borderlands)
z_stat, p_val = proportions_ztest([neg, pos], [total, total], alternative='larger')

st.subheader("Z-Test Result")
st.write(f"Z-Score: {z_stat:.2f}")
st.write(f"P-Value: {p_val:.4f}")
if p_val < 0.05:
    st.success("Conclusion: Negative sentiment is significantly higher.")
else:
    st.info("Conclusion: No significant difference — positive dominates.")

# 6. Tweet Length vs Sentiment

st.header("✏️ Tweet Length by Sentiment")

avg_len = df.groupby('sentiment')['length'].mean().sort_values()
fig, ax = plt.subplots()
avg_len.plot(kind='bar', color='mediumseagreen', ax=ax)
plt.title("Average Tweet Length per Sentiment")
st.pyplot(fig)

