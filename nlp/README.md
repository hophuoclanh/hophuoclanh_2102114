# 📚 Alice in Wonderland - NLP Semantic Analysis

This project explores the linguistic and semantic properties of *Alice in Wonderland* using Natural Language Processing (NLP) techniques. It covers:

- Tokenization and text cleaning with **spaCy**
- Word frequency analysis
- Word cloud generation
- Semantic word relationships using **GloVe** embeddings + **PCA**
- Cosine similarity heatmap between top frequent words

---

## 📦 Dependencies

Make sure you install the following libraries:

```bash
!pip install --upgrade numpy==1.24.3 gensim
!pip install spacy seaborn matplotlib wordcloud pandas scikit-learn
!python -m spacy download en_core_web_sm
```

---

## 📁 Dataset

We use the `alice.txt` text from **Project Gutenberg**.

---

## 🧠 NLP Processing Steps

### 1. **Preprocessing with spaCy**
- Convert text to lowercase
- Tokenize using `spaCy`
- Remove stopwords and non-alphabetic tokens

### 2. **Visualizations**

#### ✅ Word Cloud

![Word Cloud](wordcloud_preview.png)

- Shows the most frequent words.
- Larger words appear more often in the text.

#### ✅ Bar Plot of Word Frequency

![Bar Chart](barchart_preview.png)

- Displays the **Top 20 Most Frequent Words**.

### 3. **Semantic Analysis**

#### ✅ GloVe Embedding + PCA

![PCA Plot](pca_plot_preview.png)

- Uses GloVe 100D embeddings (`glove-wiki-gigaword-100`)
- Reduces dimensions to 2D using PCA
- Shows how top words relate semantically

#### ✅ Cosine Similarity Heatmap

![Heatmap](heatmap_preview.png)

- Measures pairwise semantic similarity between top 25 frequent words
- Darker red = higher similarity, blue = low or negative

---

## 📊 Summary of Insights

- Words like `alice`, `said`, and `little` are the most frequent.
- Words such as `queen`, `king`, and `princess` are semantically close.
- `rabbit`, `mouse`, and `cat` cluster together in PCA, showing their story relevance.
- Cosine similarity helps quantify how semantically related words are.