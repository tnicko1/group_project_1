from card import Card
from random import shuffle


class Deck(list):
    def __init__(self, suits, values):
        super().__init__(Card(suit, value) for suit in suits for value in values)
        self.shuffle()

    def shuffle(self):
        shuffle(self)

    def deal(self):
        if not self:
            raise ValueError("No more cards in the deck")
        return self.pop()