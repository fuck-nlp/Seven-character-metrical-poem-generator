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
    # poems = [poem[0] + poem[1] + poem[2] + poem[3] + poem[4] + poem[5] + poem[6] + poem[7] for poem in poems]
    poems = [','.join(poem) for poem in poems]
    print(poems[1])
    model = gensim.models.Word2Vec(poems, vector_size=WORD_VEC_DIMS, min_count=1)
    embedding = numpy.random.uniform(-1.0, 1.0, [len(word_dict), WORD_VEC_DIMS])
    for i, ch in enumerate(word_dict):
        if ch in model.wv:
            embedding[i, :] = model.wv[ch]
    numpy.save(WORD_VEC_PATH, embedding)


class Word_Vec(Singleton):
    def __init__(self):
        self._embedding = numpy.load(WORD_VEC_PATH)
        self._word_dict = Word_Dict()

    def similar_word(self, keyword: str, num=1):
        if keyword not in self._word_dict:
            return []
        keyword_vec = self._embedding[self._word_dict.word_to_int(keyword)]
        ans: list = []
        # TODO: Use numpy to find similar words ----lzj
        for index in range(0, len(self._word_dict)):
            sim = numpy.sum(numpy.square(keyword_vec - self._embedding[index]))
            if len(ans) < num:
                ans.append([index, sim])
            else:
                max_dif = max([pair[1] for pair in ans])
                if max_dif > sim:
                    for j in range(0, num):
                        if ans[j][1] == max_dif:
                            ans[j] = [index, sim]
        ans = sorted(ans, key=lambda x: x[1])
        return [self._word_dict.int_to_word(pair[0]) for pair in ans]


# For test
if __name__ == "__main__":
    # _gen_word_vec()
    word_vec = Word_Vec()
    keyword = input()
    print("find similar words of {}".format(keyword))
    print(word_vec.similar_word(keyword, 40))
