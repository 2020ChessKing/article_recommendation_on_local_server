import pandas as pd, statistics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df = pd.read_csv("articles.csv")

#   Remove Simple Words
TFIDF = TfidfVectorizer(stop_words="english")

#   Replace NAN
df["text"] = df["text"].fillna(" ")

#   Creating TFIDF Matrix
TFIDF_matrix = TFIDF.fit_transform(df["text"])
TFIDF_matrix.shape

#   Calculating Dot Product
cosine_sim_score = linear_kernel(TFIDF_matrix, TFIDF_matrix)

#   Function to Find the Most Similar Movies
indexes = pd.Series(df.index, index=df["title"]).drop_duplicates()

def get_recommendation(title):
    idx = indexes[title]
    sim_scores = list(enumerate(cosine_sim_score[idx]))

    sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse=True)
    sim_scores = sim_scores[1: 11]

    article_indexing = [i[0] for i in sim_scores]
    
    return df['title'].iloc[article_indexing].tolist()
