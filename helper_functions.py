from collections import Counter

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