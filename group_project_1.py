import random
from collections import Counter

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.suit}{self.value}"


class Deck:
    def __init__(self, suits, values):
        self.cards = [Card(suit, value) for suit in suits for value in values]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            raise ValueError("No more cards in the deck")
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)


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


# Helper Functions
def calculate_score(hand, value_points):
    return sum(value_points[card.value] for card in hand)


def most_common_suit_count(hand):
    suits = [card.suit for card in hand]
    return Counter(suits).most_common(1)[0][1]


def determine_loser(players, value_points):
    scores = {player.name: calculate_score(player.hand, value_points) for player in players}
    min_score = min(scores.values())
    losers = [player for player in players if scores[player.name] == min_score]

    if len(losers) == 1:
        eliminated_player = losers[0]
        players.remove(eliminated_player)
        print(f"{eliminated_player.name} has been eliminated!")

    return players


PLAYER_COUNT = 3
CARDS_DEALT = 5
ALL_SUITS = ["S", "H", "C", "D"]
ALL_VALUES = {"2": 2, "3": 3, "4": 3, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 20}

def main():
    players = [Player(input(f"Enter name for Player {i + 1}: ")) for i in range(PLAYER_COUNT)]

    while len(players) > 1:
        deck = Deck(ALL_SUITS, ALL_VALUES.keys())

        for player in players:
            player.hand = []

        for _ in range(CARDS_DEALT):
            for player in players:
                player.hand.append(deck.deal())

        for player in players:
            print(player)

        for player in players:
            while not player.has_changed_card:
                choice = input(f"{player.name}, do you want to change a card? (y/n): ").lower()
                if choice == "n":
                    break
                elif choice == "y":
                    selected_card = input(f"{player.name}, which card do you want to change? ").upper()
                    for card in player.hand:
                        if str(card) == selected_card:
                            player.update_hand(card, deck.deal())
                            player.has_changed_card = True
                            print(f"{player.name}'s updated hand: {player}")
                            break
                    else:
                        print("Card not found in hand. Please try again.")
                else:
                    print("Please enter 'y' or 'n'.")

        for player in players:
            player.has_changed_card = False

        previous_player_count = len(players)
        players = determine_loser(players, ALL_VALUES)

        if len(players) == previous_player_count:
            print("It's a tie! No one is eliminated.")

    if len(players) == 1:
        print(f"The final winner: {players[0].name}!")


if __name__ == "__main__":
    main()