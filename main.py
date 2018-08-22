import gensim
from gensim.models import KeyedVectors

# Data can be downloaded from this link https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit
# Put this file under data

wv_embeddings = KeyedVectors.load_word2vec_format('data/GoogleNews-vectors-negative300.bin',binary=True)

import check_embeddings
print(check_embeddings.check_embeddings(wv_embeddings))


###########################    Get mean of all word vectors in the question     ###########################
import question_to_vector
question2vec_result = []
for question in open('data/train.tsv'):
    question = question.strip()
    answer = question_to_vector.question_to_vec(question, wv_embeddings)
    question2vec_result = np.append(question2vec_result, answer)


