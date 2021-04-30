import random
class cpu:
    def __init__(self):
        self.hand = []
        self.ascii_hand = []
        self.name = random.choice(["Charlie", "Max", "Buddy", "Oscar", "Milo", "Archie", "Ollie", "Toby", "Jack"])
        self.say_turn = " "

    def add_card(self, deck):
        self.hand.append(deck.remove_top_card())

    def __str__(self):
        out = "NAME: " + self.name + "\n"
        for card in self.hand:
            out += card.__str__() + "\n"
        return out
