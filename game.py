import random
from player import Player
from deck import Deck
import time

class Game:
    def __init__(self, game_mode):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.special_deck = Deck(special=True)
        self.special_deck.shuffle_deck()
        self.game_mode = game_mode
        self.player1 = Player("Bot1" if game_mode == 2 else "Player", is_human=(game_mode == 1))
        self.player2 = Player("Bot2" if game_mode == 2 else "Bot", is_human=False)
        self.deal_cards()
        if game_mode == 1:
            self.deal_special_cards()
        self.opponent = self.player2 if self.player1.is_human else self.player1

    def deal_cards(self):
        for _ in range(len(self.deck) // 2):
            card1 = self.deck.deal_card()
            if card1:
                self.player1.hand.add_card(card1)
            card2 = self.deck.deal_card()
            if card2:
                self.player2.hand.add_card(card2)

    def deal_special_cards(self):
        for _ in range(2):
            card1 = self.special_deck.deal_card()
            if card1 and self.player1.is_human:
                self.player1.special_cards.append(card1)

    def use_special_card(self, player, opponent, card_index):
        if player.is_human and 0 <= card_index < len(player.special_cards):
            card = player.special_cards.pop(card_index)
            print(f"{player.name} uses special card: {card}")
            if card.rank == "SD": # Switch Deck
                if len(player.hand) < 5 and len(opponent.hand) < 5:
                    player.hand.cards, opponent.hand.cards = opponent.hand.cards, player.hand.cards
                    print("Decks have been switched!")
                else:
                    print("Cannot use Switch Deck - each player must have less than 5 cards.")
                    player.special_cards.insert(card_index, card)
                    return False
            elif card.rank == "SC": # Switch Card
                if len(player.hand) > 0 and len(opponent.hand) > 0:
                    while True:
                        choice = input(f"Choose a card number to switch (1-{len(player.hand)}): ")
                        try:
                            player_card_index_to_remove = int(choice) - 1
                            if 0 <= player_card_index_to_remove < len(player.hand):
                                opponent_card_index = random.randrange(len(opponent.hand))
                                if len(player.hand) > player_card_index_to_remove and len(opponent.hand) > opponent_card_index:
                                    switched_player_card = player.hand.cards.pop(player_card_index_to_remove)
                                    switched_opponent_card = opponent.hand.cards.pop(opponent_card_index)
                                    player.hand.cards.insert(player_card_index_to_remove, switched_opponent_card)
                                    opponent.hand.add_card(switched_player_card)
                                    print(f"Your card: {switched_player_card} (position {int(choice)}) has been switched with opponent's card: {switched_opponent_card}")
                                    return True
                                else:
                                    print("Error retrieving card for switch.")
                                    player.special_cards.insert(card_index, card)
                                    return False
                            else:
                                print("Invalid card number.")
                        except ValueError:
                            print("That's not a number.")
                        break
                    return False
                else:
                    print("Cannot use Switch Card - both players must have cards.")
                    player.special_cards.insert(card_index, card)
                    return False
            elif card.rank == "VD": # View Deck
                print(f"{opponent.name}'s deck: {opponent.hand.display()}")
                return True
            elif card.rank == "BC": # Burn Card
                if len(player.hand) > 0 and len(opponent.hand) > 0:
                    player_burn_index = random.randrange(len(player.hand))
                    opponent_burn_index = random.randrange(len(opponent.hand))
                    burned_player_card = player.hand.cards.pop(player_burn_index)
                    burned_opponent_card = opponent.hand.cards.pop(opponent_burn_index)
                    print(f"Card {burned_player_card} has been burned from {player.name}'s hand.")
                    print(f"Card {burned_opponent_card} has been burned from {opponent.name}'s hand.")
                    return True
                else:
                    print("Cannot use Burn Card - both players must have cards.")
                    player.special_cards.insert(card_index, card)
                    return False
            return True
        return False

    def player_action(self, player, opponent):
        if player.is_human:
            print(f"\n--- Your Turn ---")
            while True:
                all_cards_to_display = []
                print("Your cards:")
                for i, card in enumerate(player.hand.cards):
                    display_text = f"{i+1}. {card}"
                    all_cards_to_display.append((str(i + 1), card, "hand"))
                    print(display_text)

                if player.special_cards:
                    print("Special cards:")
                    for i, card in enumerate(player.special_cards):
                        letter = chr(ord('a') + i)
                        display_text = f"{letter}. {card}"
                        all_cards_to_display.append((letter, card, "special"))
                        print(display_text)

                choice = input("Choose a card to play or use a special card: ")
                for key, card_obj, card_type in all_cards_to_display:
                    if choice == key:
                        if card_type == "hand":
                            return player.hand.cards.pop(int(key) - 1)
                        elif card_type == "special":
                            if self.use_special_card(player, opponent, player.special_cards.index(card_obj)):
                                print("Special card used.")
                                break
                            else:
                                print("Cannot use this special card in this situation.")
                                break
                else:
                    print("Invalid choice. Try again.")
            return None
        else:
            time.sleep(1)
            if len(player.hand) > 0:
                return player.hand.cards.pop(random.randrange(len(player.hand)))
            return None

    def play(self):
        player1_score = 0
        player2_score = 0

        while len(self.player1.hand) > 0 and len(self.player2.hand) > 0:
            opponent_player1 = self.player2
            opponent_player2 = self.player1
            card1_played = self.player_action(self.player1, opponent_player1)
            card2_played = self.player_action(self.player2, opponent_player2)

            if card1_played == "special_card_used" or card2_played == "special_card_used":
                continue

            if card1_played and card2_played:
                print(f"\n{self.player1.name} played: {card1_played}")
                print(f"{self.player2.name} played: {card2_played}")
                if card1_played > card2_played:
                    print(f"{self.player1.name} wins the round!")
                    player1_score += 1
                elif card2_played > card1_played:
                    print(f"{self.player2.name} wins the round!")
                    player2_score += 1
                else:
                    print("It's a draw!")
                print(f"Current score - {self.player1.name}: {player1_score}, {self.player2.name}: {player2_score}\n")

            if len(self.player1.hand) == 0 or len(self.player2.hand) == 0:
                break

        print("\n--- Game Over ---")
        print(f"Final score - {self.player1.name}: {player1_score}")
        print(f"Final score - {self.player2.name}: {player2_score}")
        if player1_score > player2_score:
            print(f"{self.player1.name} wins!")
        elif player2_score > player1_score:
            print(f"{self.player2.name} wins!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    print("Welcome to Brick!\n")
    rules_txt = open("rules.txt", "r")
    opt = input("If you want to display rules, type yes. Else, type whatever : ").lower()
    if opt == "yes":
        for line in rules_txt:
            print(line)
    while True:
        try:
            mode = int(input("Choose game mode (1 - Player vs Computer / 2 - Computer vs Computer): "))
            if mode in [1, 2]:
                game = Game(mode)
                game.play()
                break
            else:
                print("Invalid choice. Enter 1 or 2.")
        except ValueError:
            print("That's not a number. Enter 1 or 2.")