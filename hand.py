

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)

    def get_card(self, index):
        if index in range(len(self.cards)):
            return self.cards[index]
        return None

    def display(self):
        return [str(card) for card in self.cards]

    def __len__(self):
        return len(self.cards)