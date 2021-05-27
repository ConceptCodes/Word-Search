import numpy as np
from random import random 

class Word():
    def __init__(self, word):
        self.word = word
        self.indexes = []
        self.completed = False

    def add_index(self, x,y): self.indexes.append((x,y))

    def completed(self): self.completed = True

class Board():
    def __init__(self, word_list):
        self.__size = 10
        self._word_list = []
        self.body = [[0] * self.__size] * self.__size
        for i in word_list:
            if type(i) is str & len(i) <= self.__size:
                self._word_list.append(Word(i))
    
    '__repr__' == '__str__'
    
    def __str__(self):
        print(np.matrix(self.body))

    @property
    def _word_list(self):
        return self.word_list

    @property
    def _completed(self,word, points):
        return self.completed

    def _horizontal_(self,word):
        # choose a random row
        row = random.randint(0,row)
        # place word inside 

    def _vertical_(self, world):
        # choose a random col
        col = random.randint(0,col)
        # place word 
        pass


