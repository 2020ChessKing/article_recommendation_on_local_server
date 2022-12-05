import pandas as pd, statistics as stats

df = pd.read_csv("articles.csv")

df = df.sort_values('totalActivity', ascending=False)
output = df["title"].tolist()[0:20]