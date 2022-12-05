from flask import Flask, jsonify, request
from storage import all_articles, liked_articles, disliked_articles
from demographic_filtering import output
from content_filtering import get_recommendation

app = Flask(__name__)

i=0

#   Get Articles


@app.route('/get-articles')
def get_articles():
    return jsonify({
        "data": all_articles,
        "status": "success"
    })

#   Like Article


@app.route('/like-article', methods=['POST'])
def like_article():
    global all_articles, liked_articles

    article = all_articles[i]
    all_articles = all_articles[1:]

    print(article[11])

    liked_articles.append(article)

    return jsonify({
        "status": "success",
    })

#   Dislike Article


@app.route('/dislike-article', methods=['POST'])
def dislike_article():
    global all_articles, liked_articles
    
    article = all_articles[i]
    all_articles = all_articles[1:]

    print(article[11])

    disliked_articles.append(article)

    return jsonify({
        "status": "success",
    })

#   Get Popular Articles


@app.route('/popular-articles')
def get_popular_articles(output=output):
    return jsonify({
        "data": output,
        "status": "success",
    })

#   Get Recommended Articles


@app.route('/recommended-articles')
def get_recommended_articles(output=output, liked_articles=liked_articles):

    if(len(liked_articles) != 0):
        articles = get_recommendation(liked_articles[len(liked_articles) - 1][11])
    else:
        articles = output

    return jsonify({
        "data": articles,
        "status": "success",
    })


if __name__ == '__main__':
    app.debug = True
    app.run()
