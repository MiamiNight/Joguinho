from random import randint

class Player:

    def __init__(self, name, cards):
        self.name = name
        self.dices = [4, 6, 8, 10, 12, 20]
        self.cards = cards
        self.main = None

    def roll(self, dice):
        return self.dices.pop(dice)
        
