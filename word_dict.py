# -*- coding:utf-8 -*-

from var import *
from singleton import Singleton


class Word_Dict(Singleton):
    _word_to_int: dict = {}
    _int_to_word: list = []

    def __init__(self):
        self._int_to_word.append(START_OF_SENTENCE)
        self._word_to_int[START_OF_SENTENCE] = 0
        with open(WORD_DICT_PATH, mode='r', encoding="utf8") as fin:
            index: int = 1
            for word in fin.readline().strip().split('|'):
                self._int_to_word.append(word)
                self._word_to_int[word] = index
                index += 1

        self._int_to_word.append(END_OF_SENTENCE)
        self._word_to_int[END_OF_SENTENCE] = len(self._int_to_word) - 1

    def word_to_int(self, word: str) -> int:
        if word in self._word_to_int:
            return self._word_to_int[word]
        return -1

    def int_to_word(self, index: int) -> str:
        return self._int_to_word[index]

    def __len__(self):
        return len(self._int_to_word)

    def __iter__(self):
        return iter(self._word_to_int)

    def __contains__(self, ch: str):
        return ch in self._word_to_int


# For test
if __name__ == "__main__":
    word_dict = Word_Dict()
    for i in range(100):
        ch: str = word_dict.int_to_word(i)
        print(ch)
        print(i)
        assert i == word_dict.word_to_int(ch)
