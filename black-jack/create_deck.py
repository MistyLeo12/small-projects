from random import shuffle
from random import choice
from itertools import product

class Deck:
    def __init__(self): 
        self.cards = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
        self.suits = ("clubs", "spades", "diamonds", "hearts")
        self.deck = list(product(self.cards, self.suits))

    def shuffle(self): 
       shuffle(self.deck)

    def show(self):
        print(self.deck)