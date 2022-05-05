# -*- coding:utf-8 -*-

from var import *
from singleton import Singleton


class Poems(Singleton):
    _poems: list = []

    def __init__(self):
        with open(CORPUS_PATH, mode='r', encoding="utf8") as fin:
            for line in fin.readlines():
                poem = line.strip().split('|')
                self._poems.append(poem)

    def __getitem__(self, index: int):
        if index < 0 or index >= len(self._poems):
            return None
        return self._poems[index]

    def __len__(self):
        return len(self._poems)

    def __iter__(self):
        return iter(self._poems)


# For test
if __name__ == "__main__":
    poems = Poems()
    for i in range(100):
        print(' '.join(poems[i]))
