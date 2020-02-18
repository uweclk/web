from flask import Flask, render_template, request
import word_2_vec_model
import json

# EB looks for an 'application' callable by default.
from settings import application

@application.route('/')
def index():
    return render_template("index.html")


######################################
########### API Endpoints ############
######################################

@application.route('/api/v1/similar_words')
def term_search():
    search_term = request.args.get('term')

    similar_words = word_2_vec_model.most_similar(search_term)

    return json.dumps(similar_words)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
