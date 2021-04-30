from ascii import *
import os
class Player:

    def __init__(self, n):
        self.name = n
        self.hand = []
        self.ascii_hand = []

    def add_card(self, deck):
        self.hand.append(deck.remove_top_card())

    def generate_ascii_hand(self):
        self.ascii_hand = []
        for card in self.hand:
            self.ascii_hand.append(ascii.card_to_ascii(card))


    def print_hand(self):
        print("YOU:")
        if len(self.ascii_hand) > 12:
            lines = [self.ascii_hand[i].splitlines() for i in range(int(len(self.ascii_hand) / 2))]
            for l in zip(*lines):
                print(*l, sep='' + "\t")

            lines = [self.ascii_hand[i].splitlines() for i in range(int(len(self.ascii_hand) / 2), len(self.ascii_hand))]
            for l in zip(*lines):
                print(*l, sep='' + "\t")
        else:
            lines = [self.ascii_hand[i].splitlines() for i in range(len(self.ascii_hand))]
            for l in zip(*lines):
                print(*l, sep='' + "\t")

    def __str__(self):
        out = "NAME: " + self.name + "\n"
        for card in self.hand:
            out += card.__str__() + "\n"
        return out
