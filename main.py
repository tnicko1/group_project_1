from deck import Deck
from player import Player
from helper_functions import *


PLAYER_COUNT = 3
CARDS_DEALT = 5
ALL_SUITS = ["S", "H", "C", "D"]
ALL_VALUES = {"2": 2, "3": 3, "4": 3, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 20}

def main():
    players = [Player(input(f"Enter name for Player {i + 1}: ").strip() or f"Player {i + 1}") for i in range(PLAYER_COUNT)]

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
                            print(f"{player.name}'s hand updated. {player}")
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
