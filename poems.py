# -*- coding:utf-8 -*-

from var import *
from singleton import Singleton


class Poems(Singleton):
    poems: list = []

    def __init__(self):
        with open(CORPUS_PATH, mode='r', encoding="utf8") as fin:
            for line in fin.readlines():
                poem = line.strip().split('|')
                temp_poem = []
                for sentence in poem:
                    temp_poem.append(sentence)
                self.poems.append(temp_poem)

    def __getitem__(self, index: int):
        if index < 0 or index >= len(self.poems):
            return None
        return self.poems[index]

    def __len__(self):
        return len(self.poems)

    def __iter__(self):
        return iter(self.poems)


# For test

if __name__ == "__main__":
    poems = Poems()
    for i in range(100):
        print(' '.join(poems[i]))
