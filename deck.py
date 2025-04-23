import random
from card import Card

suits = ['HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES']
ranks = ['10', 'J', 'Q', 'K', 'A']
special_ranks = ['SD', 'SC', 'VD', 'BC']

class Deck:
    def __init__(self, special = False):
        self.cards = []
        if special:
            for rank in special_ranks:
                self.cards.extend([Card(rank, None)] * 2)
        else:
            self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def display(self):
        print([str(tmp_card) for tmp_card in self.cards])

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None

    def __len__(self):
        return len(self.cards)