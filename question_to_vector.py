import numpy as np
def question_to_vec(question, embeddings, dim=300):
    """
        question: a string
        embeddings: dict where the key is a word and a value is its' embedding
        dim: size of the representation

        result: vector representation for the question
        """
    question_vector = []
    
    length = len(question.split())
    for embedding in question.split(' '):
        if embedding in embeddings:
            question_vector.append(embeddings[embedding])

    if question == '' :
        return np.zeros(dim)
    if length == 1 and question not in wv_embeddings:
        return np.zeros(dim)
    question_vector_array = np.array(question_vector)
    return question_vector_array.mean(axis=0)


#def question_to_vec_tests():
#    if (np.zeros(300) != question_to_vec('', wv_embeddings)).any():
#        return "You need to return zero vector for empty question."
#    if (np.zeros(300) != question_to_vec('thereisnosuchword', wv_embeddings)).any():
#        return "You need to return zero vector for the question, which consists only unknown words."
#    if (wv_embeddings['word'] != question_to_vec('word', wv_embeddings)).any():
#        return "You need to check the corectness of your function."
#    if ((wv_embeddings['I'] + wv_embeddings['am']) / 2 != question_to_vec('I am', wv_embeddings)).any():
#        return "Your function should calculate a mean of word vectors."
#    if (wv_embeddings['word'] != question_to_vec('thereisnosuchword word', wv_embeddings)).any():
#        return "You should not consider words which embeddings are unknown."
#    return "Basic tests are passed."
#print(question_to_vec_tests())

