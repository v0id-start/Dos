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

    # Return index of card from action -- ex: "r1" to get index of red 1 card
    # Returns -1 if card not found
    def index_of_card(self, human_action):
        card_ind = 0
        found_ind = -1
        for card in self.hand:
            if len(human_action) == 2:

                if human_action[1].isnumeric():
                    if card.color is not None and card.number is not None:
                        if card.color[0] == human_action[0] and str(card.number) == human_action[1]:
                            found_ind = card_ind
                elif human_action[1] in ["s", "r", "d"] and card.type is not None and card.color is not None:
                    if card.color[0] == human_action[0] and card.type[0] == human_action[1]:
                        found_ind = card_ind

            elif len(human_action) == 1 and card.type is not None:
                if card.type[0] == human_action[0]:
                    found_ind = card_ind
            card_ind += 1
        return found_ind


    def take_turn(self, players, deck):
        is_turn = True
        while is_turn:
            # Player makes action
            human_action = input("Your Move: ")

            if human_action == "c":
                self.hand.append(deck.remove_top_card())
                ascii.redraw(players,deck)

            else:
                # Check if player actually has that card
                found_ind = self.index_of_card(human_action)

                if found_ind != -1:
                    if self.hand[found_ind].type == "wild" or self.hand[found_ind].type == "draw_four":
                        deck.add_card_to_pile(self.hand.pop(found_ind))
                        new_color = input("What is the new color?")
                        c = ""
                        if new_color[0].lower() == "r":
                            c = "red"
                        elif new_color[0].lower() == "y":
                            c = "yellow"
                        elif new_color[0].lower() == "g":
                            c = "green"
                        elif new_color[0].lower() == "b":
                            c = "blue"
                        deck.get_top_pile().color = c
                        is_turn = False
                    elif self.hand[found_ind].color == deck.get_top_pile().color or self.hand[found_ind].number == deck.get_top_pile().number or (self.hand[found_ind].type is not None and self.hand[found_ind].type == deck.get_top_pile().type):
                        deck.add_card_to_pile(self.hand.pop(found_ind))
                        is_turn = False
                    else:
                        ascii.redraw(players,deck)
                        print("You can't play " + self.hand[found_ind].__str__() + " right now!")
                else:
                    ascii.redraw(players,deck)
                    print("You don't have that card!")


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
