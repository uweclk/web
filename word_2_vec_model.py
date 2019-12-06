import gensim 
from gensim.models import Word2Vec 
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "machine_learning/cbow.model"
abs_file_path = os.path.join(script_dir, rel_path)

model = Word2Vec.load(abs_file_path)

def most_similar(word):
    return model.wv.most_similar(word)