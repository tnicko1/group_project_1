
import random
from collections import Counter

# კლასი card აერთიანებს ფერებს და მნიშვნელობას კონფიგურაციიდან
class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def __str__(self):
        return f"{self.suit}{self.value}"

# კლასი deck არის ლისტის შვილობილი, დავამატე ექსტრა მეთოდები გლობალური კონფიგურაციებზე დაფუძნებით დასტის შესაქმნელად და მოთამაშეებისთვის დარიგებისთვის.
class Deck:
    def __init__(self,suits,values):
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

# მოთამაშის კლასი, აქვს სახელი და კარტის კლასის ობიექტებისგან შემდგარი სია
class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []
    
    def list(self): # აქ მეთოდი დავამატე, სხვაგვარად ვერ მივხვდი ხელი როგორ მომეკიდებინა მნიშვნელობაზე
        cards_list = [str(card) for card in self.hand]
        return cards_list
    
    def __str__(self):
        player_hand = " ".join(str(card) for card in self.hand)
        return f"{self.name}'s Cards: {player_hand}"
    
# სტატიკური მეთოდები
# 1 კარტის შეცვლა
def change_card(player, deck):
    while True:
        choice = input(f"{player.name}, do you want to change a card? (y/n): ").lower()
        if choice == "n":
            return False
        if choice == "y":
            break
        print("Please enter 'y' or 'n'.")
    
    while True:
        selected_card = input(f"{player.name}, which card do you want to change? ")
        for card in player.hand:
            if str(card) == selected_card:
                card_index = player.hand.index(card)
                player.hand[card_index] = deck.deal()
                print(f"{player.name}'s updated hand: {player}")
                return True
        print("Card not found in hand. Please try again.")
    

# კარტის ქულების დათვლა
def card_value(card):
    value = card[0]  # კარტის რიცხვი ან სიმბოლო
    if value.isdigit():
        return int(value)
    elif value == 'J':
        return 11
    elif value == 'Q':
        return 12
    elif value == 'K':
        return 13
    elif value == 'A':
        return 20

# მოთამაშის ქულების დათვლა
def calculate_score(cards):
    return sum(card_value(card) for card in cards)

# ერთნაირი ფერის კარტების რაოდენობა

def most_common_suit_count(players_card):
    result = {}
    
    for key, card_list in players_card.items():
        # ფერების რაოდენობის დათვლა
        suits = [card[-1] for card in card_list]  # კარტის ფერის ამოღება
        suit_counts = Counter(suits)
        # ყველაზე ხშირი ფერის რაოდენობა
        most_common_count = suit_counts.most_common(1)[0][1]
        # შედეგის შენახვა
        result[key] = most_common_count

    return result

# ერთნაირი მნიშვნელობების რაოდენობა
def value_count(cards):
    values = [card[:-1] for card in cards]
    return Counter(values)

# დამარცხებულის გამოვლენა
def determine_loser(players_dict):
    
    scores = {player: calculate_score(cards) for player, cards in players_dict.items()}
    min_score = min(scores.values())
    last_players = [player for player, score in scores.items() if score == min_score] # აქ ვიყვან ყველაზე პატარა ქულიან მოთამაშეს

    if len(last_players) == 1:
        players_dict.pop(last_players[0])
        return players_dict
    
    # თანაბარი ქულების შემთხვევაში, ფერების დათვლა
    suit_count_dict = most_common_suit_count(players_dict)
    min_suit_count = min(suit_count_dict.values())
    last_players = [player for player in last_players if suit_count_dict.get(player) == min_suit_count]
      
    if len(last_players) == 1:
        players_dict.pop(last_players[0])
        return players_dict

    # თანაბარი ფერების შემთხვევაში, მნიშვნელობების დათვლა
    value_counts = {player: min(value_count(players_dict[player]).values()) for player in last_players}
    min_value_count = min(value_counts.values())
    last_players = [player for player in last_players if value_counts[player] == min_value_count]

    if len(last_players) == 1:
        players_dict.pop(last_players[0])

    return players_dict # თუ დამარცხებული გამოვლინდა, ფუნქცია დამიბრუნებს მის გარეშე წევრებს

def main():
    
    # გლობალური კონფიგურაციები
    PLAYER_COUNT = 3
    CARDS_DEALT = 5
    ALL_SUITS = ["S", "H", "C", "D"]
    ALL_VALUES = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":20}

    # კოდის გაშვება
    players = [Player(input(f"Enter name for Player {i + 1}: ")) for i in range(PLAYER_COUNT)]

    def run():
        nonlocal players

        deck = Deck(ALL_VALUES, ALL_SUITS)

        for _ in range(CARDS_DEALT):
            for player in players:
                player.hand.append(deck.deal())

        for player in players:
            print(player)

        for player in players:
            change_card(player, deck)
        
        # აქ შემომაქვს ცარიელი დიქტი, რადგან შევინახო მოთამაშეების გენერირებული (ცვლილების გათვალისწინებით) კარტები
        player_cards = {}
        
        for player in players:
            player_cards[player.name] = player.list()  
                   
        print(player_cards)
        player_cards = determine_loser(player_cards)
            
        if len(player_cards.keys()) == 1 :
            for player, cards in player_cards.items():
                print (f"საბოლოო გამარჯვებული არის მოთამაშე: {player}!")
        else:  
            while len(player_cards.keys()) > 1:
                
                PLAYER_COUNT = len(player_cards.keys())
                players = [Player(input(f"Enter name for Player {i + 1}: ")) for i in range(PLAYER_COUNT)]
                return run()
   
    run()
        
if __name__ == "__main__":
    main()


