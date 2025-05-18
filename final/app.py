import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from statsmodels.stats.proportion import proportions_ztest
import seaborn as sns
from scipy.stats import f_oneway

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
- Entity-level sentiment breakdown + Z-Test
- Word Cloud
- Tweet Length + ANOVA Test
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
st.header("☁️ Word Cloud by Entity & Sentiment")

col1, col2 = st.columns(2)

with col1:
    wc_entity = st.selectbox("Choose entity", top_entities, key="wc_entity")

with col2:
    wc_sentiment = st.selectbox("Choose sentiment", ["Positive", "Negative"], key="wc_sentiment")

# Filter text
wc_filtered = df[(df['entity'] == wc_entity) & (df['sentiment'] == wc_sentiment)]
text = ' '.join(wc_filtered['text'])

stopwords = set(STOPWORDS)
stopwords.update(['game', 'pic', 'twitter'])

wc = WordCloud(width=800, height=400, stopwords=stopwords, background_color="black").generate(text)

fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wc, interpolation='bilinear')
ax.axis('off')
plt.title(f"Word Cloud for {wc_entity} — {wc_sentiment}")
st.pyplot(fig)

# 5. Tweet Length vs Sentiment + ANOVA
st.header("✏️ Tweet Length by Sentiment")

selected_entity_length = st.selectbox("Choose an Entity for Length Analysis", top_entities, key="length_entity")

filtered_length_df = df[df['entity'] == selected_entity_length]

avg_len = filtered_length_df.groupby('sentiment')['length'].mean().sort_values()

fig, ax = plt.subplots()
avg_len.plot(kind='bar', color='mediumseagreen', ax=ax)
plt.title(f"Average Tweet Length per Sentiment — {selected_entity_length}")
plt.ylabel("Avg Length (Characters)")
st.pyplot(fig)

# --- ANOVA Test ---
st.subheader("📊 ANOVA Test: Does Tweet Length Differ by Sentiment?")

groups = [group['length'].values for name, group in filtered_length_df.groupby('sentiment')]

f_stat, p_val = f_oneway(*groups)

st.markdown(f"**F-Statistic:** `{f_stat:.2f}`")
st.markdown(f"**P-Value:** `{p_val:.4f}`")

if p_val < 0.05:
    st.success("**Conclusion:** There is a significant difference in tweet length across sentiment groups.")
else:
    st.info("**Conclusion:** No significant difference in tweet length across sentiment groups.")
