---
title: 'Brick: A Python Card Game'

---

# Brick: A Python Card Game

## Introduction

Brick is a Python-based card game for one or two players, with a twist! It's played with a modified deck and includes special cards that introduce strategic elements beyond simply comparing card values. This README provides an overview of the game, how to play, and the underlying code structure.

## Game Rules

1.  **Deck:** The game uses a "small deck" consisting of cards from 10 upwards (10, Jack, Queen, King, Ace).
2.  **Special Cards:** The player has access to four unique special cards:
    * **View Deck (VD):** Allows the player to preview the opponent's hand.
    * **Burn Card (BC):** Discards one random card from both the player's and the opponent's hands.
    * **Switch Card (SC):** Allows the player to swap one of their chosen cards with a random card from the opponent's hand.
    * **Switch Deck (SD):** Allows the player to swap their entire hand with the opponent's hand. This card can only be played when both players have less than 5 cards in their hands.
3.  **Gameplay:**
    * The game ends when there are no more base cards in the deck.
    * In each turn, players draw a card, and the player with the higher-ranking card scores a point.
    * The player always starts the game.
    * The game supports both Player vs. Computer and Computer vs. Computer modes.
4. **Winning:** The player with the most points at the end of the game wins.

## How to Play

1.  **Game Modes:**
    * **Player vs. Computer (1):** Play against an computer.
    * **Computer vs. Computer (2):** Watch two computers play against each other.
2.  **Starting the Game:**
    * Run the `game.py` script.
    * The game will prompt you to choose a game mode.
    * If you choose Player vs. Computer mode, you will also receive special cards.
3.  **Playing Cards:**
    * In each turn, you can choose to play a regular card from your hand or use a special card (if available).
    * If you play a regular card, it will be compared to your opponent's card, and the player with the higher-ranking card wins the round.
    * If you play a special card, its effect will be applied.
4.  **Special Card Usage:**
    * Special cards can significantly alter the course of the game. Use them strategically!
    * Each special card has a unique effect, as described in the "Game Rules" section.
    * The game will prompt you for any necessary input when using a special card (e.g., which card to switch).

## Code Structure

The game is implemented in Python using a modular structure:

* `game.py`: This is the main file that contains the `Game` class. It orchestrates the gameplay, manages players, and handles user input.
* `player.py`: Defines the `Player` class, which represents a player in the game (either human or computer). Each player has a hand of cards and a set of special cards (for the human player).
* `deck.py`: Defines the `Deck` class, which represents a deck of cards. It handles card creation, shuffling, and dealing.
* `rules.txt`: Contains the rules of the game.

### Key Classes and Functions

* **`Game` Class:**
    * `__init__(self, game_mode)`: Initializes the game, including the deck, players, and game mode.
    * `deal_cards(self)`: Deals cards to the players at the beginning of the game.
    * `deal_special_cards(self)`: Deals special cards to the human player.
    * `use_special_card(self, player, opponent, card_index)`: Handles the logic for using special cards.
    * `player_action(self, player, opponent)`: Gets the player's card choice or special card selection.
    * `play(self)`: Contains the main game loop, managing turns, card comparisons, and scoring.
* **`Player` Class:**
    * `__init__(self, name, is_human)`: Initializes a player with a name and a flag indicating whether they are human or a computer.
    * `hand`: An instance of the `Deck` class, representing the player's hand.
    * `special_cards`: A list of `Card` objects, representing the player's special cards.
* **`Deck` Class:**
    * `__init__(self, special=False)`: Initializes a deck of cards, either a standard deck or a special card deck.
    * `shuffle_deck(self)`: Shuffles the deck.
    * `deal_card(self)`: Removes and returns the top card from the deck.

The game logic follows an object-oriented approach, with classes representing the core game elements. The `Game` class manages the overall flow, while the `Player` and `Deck` classes handle player-specific and deck-specific operations, respectively.

## Testing

The game includes unit tests to ensure the correctness of the core game logic. The tests cover the following:
* Deck creation and shuffling
* Card dealing
* Player actions
* Special card logic

Feel free to contribute to the game by submitting pull requests.


## Total worktime: 6 hours

