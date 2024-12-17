import random

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
class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []
    def __str__(self):
        player_hand = f"{self.name}'s Cards: "
        for card in self.hand:
            player_hand += str(card)+ " "
        return player_hand
    
# სტატიკური მეთოდები
# 1 კარტის შეცვლა
def change_card(player,deck):
    while True:
        choice = input("Do you want to change 1 card? (y/n): ").lower()
        if choice == "n":
            return False
        if choice == "y":
            break
        print("Please choose Y or N")
    
    while True:
        choice = input("Which card do you want to change: ")
        for card in player.hand:
            if str(card) == choice:
                
                card_index = player.hand.index(card)
                player.hand[card_index] = deck.deal()
                return True
        print("Card not found in hand")
    
# გლობალური კონფიგურაციები
PLAYER_COUNT = 3
CARDS_DEALT = 5
ALL_COLORS = ["S","H","C","D"]
ALL_VALUES = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":20}

# კოდის გაშვება
players = []
for i in range(PLAYER_COUNT):
    players.append(Player(input(f"Player {i+1}: ")))

while True:
    deck = Deck(ALL_VALUES, ALL_COLORS)
    for player in players:
        for _ in range(CARDS_DEALT):
            card = deck.deal()
            player.hand.append(card)
    for player in players:
        print(player)
        if change_card(player,deck):
            print(f"Updated {player}")

     # აქ უბრალოდ საჩვენებლად გავაკეთე მე როგორ წარმომიდგენია, სანამ winners ლისტში 1ზე მეტი playeri-ს ობიექტია იქამდე ლუპი იმუშავებს.
     # winners ენიჭება ვალიდაციის შედეგად მოგებული მოთამაშეების სია, თუ ერთია გამარჯვებული, მაშინ თამაში რჩება
     # თუ 1-ზე მეტია, ეგეთ შემთხვევაში ფრეა და თამაში უნდა დაიწყოს თავიდან, ოღონდ, players კლასში უკვე მხოლოდ winner-ები უნდა იყვნენ
    winners = []
    if (len(winners) == 1):
        print("Winner")
        break

    # players = winners
    for player in players:
        player.hand.clear()
