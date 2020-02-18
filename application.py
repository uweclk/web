from flask import Flask, render_template, request
import word_2_vec_model

# EB looks for an 'application' callable by default.
from settings import application

@application.route('/')
def index():
    # search_term = request.args.get('term') or 'water'

    # similar_words = word_2_vec_model.most_similar(search_term)

    # return render_template(
    #     "index.html",
    #     search_term=search_term,
    #     similar_words=similar_words)
    return render_template("index.html")

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
