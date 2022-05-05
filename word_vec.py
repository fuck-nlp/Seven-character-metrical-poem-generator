# -*- coding:utf8 -*-

from word_dict import Word_Dict
from poems import Poems
from singleton import Singleton
import numpy
from var import *
import gensim


def _gen_word_vec():
    word_dict = Word_Dict()
    poems = Poems()
    poems = [poem[0] + poem[1] + poem[2] + poem[3] + poem[4] + poem[5] + poem[6] + poem[7] for poem in poems]
    model = gensim.models.Word2Vec(poems, vector_size=WORD_VEC_DIMS, min_count=1)
    embedding = numpy.random.uniform(-1.0, 1.0, [len(word_dict), WORD_VEC_DIMS])
    for i, ch in enumerate(word_dict):
        if ch in model.wv:
            embedding[i, :] = model.wv[ch]
    numpy.save(WORD_VEC_PATH, embedding)

# class Word_Vec(Singleton):
#     def __init__(self):
# For test
if __name__ == "__main__":
    _gen_word_vec()
