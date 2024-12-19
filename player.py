class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.has_changed_card = False

    def update_hand(self, old_card, new_card):
        if old_card in self.hand:
            self.hand[self.hand.index(old_card)] = new_card
        else:
            raise ValueError(f"{old_card} not in hand")

    def __str__(self):
        player_hand = " ".join(str(card) for card in self.hand)
        return f"{self.name}'s Cards: {player_hand}"