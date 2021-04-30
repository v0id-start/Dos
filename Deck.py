from Card import *
import random
class Deck:

    def populate(self, color):
        self.card_deck.append(Card(c=color, n=0))
        self.card_deck.append(Card("skip", c=color))
        self.card_deck.append(Card("skip", c=color))
        self.card_deck.append(Card("draw_two", c=color))
        self.card_deck.append(Card("draw_two", c=color))
        self.card_deck.append(Card("reverse", c=color))
        self.card_deck.append(Card("reverse", c=color))

        for i in range(2):
            for i in range(1,10):
                self.card_deck.append(Card(c=color, n=i))

    def __init__(self):
        self.card_deck = []
        self.pile = []
        for i in range(4):
            self.card_deck.append(Card("wild"))

        for i in range(4):
            self.card_deck.append(Card("draw_four"))

        self.populate("red")
        self.populate("yellow")
        self.populate("green")
        self.populate("blue")


    def shuffle(self):
        random.shuffle(self.card_deck)

    def remove_top_card(self):
        if len(self.card_deck) > 0:
            return self.card_deck.pop(0)
        else:
            self.re_pile_cards()
            print("RE-PILING CARDS")
            return self.card_deck.pop(0)

    def add_top_card_to_pile(self):
        self.pile.append(self.remove_top_card())

    def add_card_to_pile(self, card):
        self.pile.append(card)

    def re_pile_cards(self):
        self.deck = self.pile
        self.pile = []
        self.shuffle()
        self.add_top_card_to_pile()

    def get_top_pile(self):
        return self.pile[-1]

    def get_cards(self):
        return self.card_deck

    def get_count(self):
        return len(self.card_deck)

    def __str__(self):
        out = ""
        for card in self.card_deck:
            out += card.__str__() + "\n"
        return out
