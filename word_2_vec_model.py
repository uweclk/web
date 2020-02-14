import gensim 
from gensim.models import Word2Vec 
from stop_words import get_stop_words
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "machine_learning/cbow.model"
abs_file_path = os.path.join(script_dir, rel_path)

model = Word2Vec.load(abs_file_path)

stop_words = get_stop_words('en')

def most_similar(word):
    if word in model.wv:
        unfiltered = model.wv.most_similar(word, topn = 10000)
        filtered = []
        for x in unfiltered:
            if((x[0] not in stop_words) and len(x[0]) > 1):
                filtered.append(x)
        return filtered[:10]
    else:
        return [word + " is not in our vocabulary"]
