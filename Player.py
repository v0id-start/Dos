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
                if card.type == "draw_four" and human_action[0] == "d":
                    found_ind = card_ind
                elif card.type == "wild" and human_action[0] == "w":
                    found_ind = card_ind

            if found_ind != -1:
                return found_ind

            card_ind += 1
        return found_ind

    def check_win(self):
        if len(self.hand) == 0:
            return True
        return False
    def take_turn(self, players, deck, next_turn, reverse):
        won = False
        skip = False
        is_turn = True
        while is_turn:
            # Player makes action
            human_action = input("Your Move: ")
            if len(self.hand) == 2:
                if human_action.lower() != "dos":
                    self.add_card(deck)
                    self.add_card(deck)

                    ascii.redraw(players,deck)
                    print("!DIDN'T SAY DOS!")
                    human_action = input("Your Move: ")
                else:
                    print("Good Job!")
                    human_action = input("Your Move: ")
            if human_action == "c":
                self.hand.append(deck.remove_top_card())
                ascii.redraw(players,deck)

            else:
                # Check if player actually has that card
                found_ind = self.index_of_card(human_action)

                if found_ind != -1:
                    if self.hand[found_ind].type == "wild" or self.hand[found_ind].type == "draw_four":

                        # Next player draws 4 if d4 played
                        if self.hand[found_ind].type == "draw_four":
                            for i in range(4):
                                players[next_turn].add_card(deck)

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

                        if len(self.hand) == 0:
                            won = self.check_win()
                        is_turn = False
                    # If found card is legal to play on top of pile (same # or color or wild or draw4)
                    elif self.hand[found_ind].color == deck.get_top_pile().color or self.hand[found_ind].number == deck.get_top_pile().number or (self.hand[found_ind].type is not None and self.hand[found_ind].type == deck.get_top_pile().type):

                        if self.hand[found_ind].type is not None:
                            # If draw 2 played, next person draws 2. Simple.
                            if self.hand[found_ind].type == "draw_two":
                                players[next_turn].add_card(deck)
                                players[next_turn].add_card(deck)

                            # If reverse, reverse.
                            if self.hand[found_ind].type == "reverse":
                                reverse = not reverse

                            # If skip, skip. Simple.
                            if self.hand[found_ind].type == "skip":
                                skip = True

                        # Place found & legal card on pile
                        deck.add_card_to_pile(self.hand.pop(found_ind))

                        if len(self.hand) == 0:
                            won = self.check_win()
                        is_turn = False
                    else:
                        ascii.redraw(players,deck)
                        print("You can't play " + self.hand[found_ind].__str__() + " right now!")
                else:
                    ascii.redraw(players,deck)
                    print("You don't have that card!")

        return [reverse, skip, won]

    def f(self):
        for i in range(3):
            print(i * 12, (i + 1) * 12)

    def print_section(self, start, stop):
        lines = [self.ascii_hand[i].splitlines() for i in range(start, stop)]
        for l in zip(*lines):
            print(*l, sep='' + "\t")

    def print_hand(self):
        print("YOU:")

        if len(self.ascii_hand) > 36:
            self.print_section(0, len(self.ascii_hand)-36)
            self.print_section(len(self.ascii_hand)-36, len(self.ascii_hand)-24)
            self.print_section(len(self.ascii_hand)-24, len(self.ascii_hand)-12)
            self.print_section(len(self.ascii_hand) - 12, len(self.ascii_hand))
        elif len(self.ascii_hand) > 24:
            self.print_section(0, len(self.ascii_hand)-24)
            self.print_section(len(self.ascii_hand)-24, len(self.ascii_hand)-12)
            self.print_section(len(self.ascii_hand)-12, len(self.ascii_hand))
        elif len(self.ascii_hand) > 12:
            self.print_section(0, int(len(self.ascii_hand)/2))
            self.print_section(int(len(self.ascii_hand)/2), len(self.ascii_hand))
        else:
            self.print_section(0, len(self.ascii_hand))
        print("# CARDS:", len(self.ascii_hand))

    def __str__(self):
        out = "NAME: " + self.name + "\n"
        for card in self.hand:
            out += card.__str__() + "\n"
        return out
