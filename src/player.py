from random import randint

class Player:

    def __init__(self, name, cards):
        self.name = name
        self.dices = [4, 6, 8, 10, 12, 20]
        self.cards = cards
        self.main = None

    def roll(self, dice_id):
        if len(self.dices) > 0:
            # Remove dice from player's pool:
            max_value = self.dices.pop(dice_id)
            return randint(1, max_value)
