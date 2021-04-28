class Player:

    def __init__(self, n):
        self.name = n
        self.hand = []

    def add_card(self, deck):
        self.hand.append(deck.remove_top_card())

    def __str__(self):
        out = "NAME: " + self.name + "\n"
        for card in self.hand:
            out += card.__str__() + "\n"
        return out