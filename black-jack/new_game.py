from create_deck import Deck
from random import choice

def checkScore(score):
    if score <= 21:
        return True

class Game:
    def __init__(self):
        self.players = {} # creates an empty dictionary of the players hands
        self.deck = Deck()
    
    def addPlayers(self, player_number = 1):
        for i in range(player_number):
            self.players[(i+1)] = ([], 0)

    def dealCard(self, player):
        card = choice(self.deck.deck)
        self.deck.deck.remove(card)
        self.players[player][0].append(card[0])
        print(player, "was dealt", card[0], "of", card[1])


