# Card Game

## Overview
This is a card game implemented in Python where multiple players compete to avoid elimination until only one remains as the winner. Each round, players receive a hand of cards, and they can decide whether to swap one card to improve their score. The player with the lowest score at the end of the round is eliminated.

## Features
- **Deck Management**: A shuffled deck is created and managed automatically.
- **Player Interaction**: Players can view their hands and choose whether to swap cards.
- **Elimination Rules**: The player with the lowest score is eliminated after each round.
- **Tie Handling**: If multiple players have the same lowest score, no one is eliminated in that round.
- **Winner Declaration**: The game ends when only one player remains.

## Classes

### `Card`
Represents a single card with a suit and a value.
- **Attributes**:
  - `suit`: The suit of the card (e.g., `"S"` for Spades).
  - `value`: The value of the card (e.g., `"A"` for Ace).
- **Methods**:
  - `__str__`: Returns a string representation of the card.

### `Deck`
Represents a deck of cards.
- **Attributes**:
  - `cards`: A list of `Card` objects.
- **Methods**:
  - `shuffle`: Shuffles the deck.
  - `deal`: Deals the top card from the deck.
  - `__len__`: Returns the number of cards remaining in the deck.

### `Player`
Represents a player in the game.
- **Attributes**:
  - `name`: The name of the player.
  - `hand`: A list of `Card` objects representing the player's current hand.
  - `has_changed_card`: A flag to track if the player has swapped a card in the current round.
- **Methods**:
  - `update_hand`: Replaces a specified card in the hand with a new card.
  - `__str__`: Returns a string representation of the player's hand.

## Game Flow
1. **Setup**:
   - Players enter their names.
   - A shuffled deck is created for each round.

2. **Dealing Cards**:
   - Each player is dealt a hand of 5 cards.

3. **Card Swapping**:
   - Players decide whether to swap a card from their hand with a new one from the deck.

4. **Scoring and Elimination**:
   - Each player's hand is scored based on card values.
   - The player with the lowest score is eliminated.

5. **Repeat**:
   - Steps 2–4 are repeated until only one player remains.

6. **Winner Announcement**:
   - The last remaining player is declared the winner.

## Scoring
- Card values are assigned points as follows:
  - Numbered cards (`2`–`10`): Points equal to their number.
  - Face cards (`J`, `Q`, `K`): 11, 12, and 13 points, respectively.
  - Ace (`A`): 20 points.

## How to Run
1. Ensure you have Python installed (version 3.6 or later).
2. Save the code to a file, e.g., `card_game.py`.
3. Open a terminal or command prompt and navigate to the file's directory.
4. Run the script using the command:
   ```
   python card_game.py
   ```
5. Follow the prompts to play the game.

## Example Gameplay
```
Enter name for Player 1: Alice
Enter name for Player 2: Bob
Enter name for Player 3: Charlie

Alice's Cards: S2 H5 D9 C3 D7
Bob's Cards: H10 C4 S6 DQ CA
Charlie’s Cards: D8 C2 H3 S7 H9

Alice, do you want to change a card? (y/n): y
Alice, which card do you want to change? S2
Alice's updated hand: H5 D9 C3 D7 S4
...
Bob has been eliminated!
...
The final winner: Alice!
```


## Acknowledgments
Thank you for playing! Feel free to customize the rules or add new features.
