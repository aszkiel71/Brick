

UTIL_HANDS_RANK = {
    "10" : 10,
    "J" : 11,
    "Q" : 12,
    "K" : 13,
    "A" : 14,
    "SD" : 15,
    "SC" : 16,
    "VD" : 17,
    "BC" : 18
}

UTIL_HANDS_NAME = {
    "SD" : "Switch Deck",
    "SC" : "Switch Card",
    "VD" : "View Deck",
    "BC" : "Burn Card"
}


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.val = UTIL_HANDS_RANK[self.rank]

    def __str__(self):
        if self.suit:
            if self.suit == "SPADES":
                return f"{self.rank}♠"
            elif self.suit == "DIAMONDS":
                return f"{self.rank}◆"
            elif self.suit == "HEARTS":
                return f"{self.rank}♡"
            elif self.suit == "CLUBS":
                return f"{self.rank}♣"
        else:
            return UTIL_HANDS_NAME[self.rank]


    def __gt__(self, other):
        return self.val > other.val

    def __lt__(self, other):
        return self.val < other.val

    def __ge__(self, other):
        return self.val >= other.val

    def __le__(self, other):
        return self.val <= other.val

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.val == other.val
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
