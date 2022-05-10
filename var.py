# -*- coding:utf-8 -*-

import os

ROOT_DIR: str = os.path.dirname(__file__)
RAW_DIR: str = os.path.join(ROOT_DIR, "raw")
DATA_DIR: str = os.path.join(ROOT_DIR, "data")

CORPUS_PATH: str = os.path.join(RAW_DIR, "corpus.txt")
CORPUS_SPLITTED_PATH: str = os.path.join(RAW_DIR, "corpus_splitted.txt")
WORD_DICT_PATH: str = os.path.join(RAW_DIR, "word_dict.txt")
CHAR_DICT_PATH: str = os.path.join(RAW_DIR, "char_dict.txt")
WORD_VEC_PATH: str = os.path.join(DATA_DIR, "word_vec.npy")

START_OF_SENTENCE: str = '^'
END_OF_SENTENCE: str = '$'

NUM_OF_SENTENCES: int = 8
WORD_VEC_DIMS: int = 256
