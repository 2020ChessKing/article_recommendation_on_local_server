import csv
import pandas as pd

# Get Data
csv_array_data = []

with open("articles.csv", encoding="utf-8") as file:
    csv_data = csv.reader(file)

    for rows in file:
        csv_array_data.append(rows)

df = pd.read_csv("articles.csv")

all_articles = df.values.tolist()

headers = "id" + csv_array_data[0]

liked_articles = []
disliked_articles = []