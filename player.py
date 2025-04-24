from hand import Hand

class Player:
    def __init__(self, name, is_human=False):
        self.name = name
        self.hand = Hand()
        self.special_cards = []
        self.is_human = is_human

    def display_special_cards(self):
        if self.is_human and self.special_cards:
            print("Special cards : :")
            for i, card in enumerate(self.special_cards):
                print(f"{chr(ord('a') + i)}. {card}")
        elif self.is_human:
            print("You have got no special card.")