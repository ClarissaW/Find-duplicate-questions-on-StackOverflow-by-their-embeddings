import gensim
from gensim.models import KeyedVectors

# Data can be downloaded from this link https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit
# Put this file under data

wv_embeddings = KeyedVectors.load_word2vec_format('data/GoogleNews-vectors-negative300.bin',binary=True)

import check_embeddings
print(check_embeddings.check_embeddings(wv_embeddings))
