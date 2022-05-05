# -*- coding:utf-8 -*-

from var import *
import singleton


def _gen_word_dic():


class Word_Dict(singleton):
    _word_to_int: dict = {}
    _int_to_word: list = []

    def __init__(self):
        self._int_to_word.append(START_OF_SENTENCE)
        self._word_to_int[START_OF_SENTENCE] = 0
        with open()
