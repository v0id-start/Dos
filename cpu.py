import random
import time
from ascii import *
class cpu:
    def __init__(self):
        self.hand = []
        self.name = random.choice(["Charlie", "Max", "Buddy", "Oscar", "Milo", "Archie", "Ollie", "Toby", "Jack"])
        self.say_turn = " "

    def add_card(self, deck):
        self.hand.append(deck.remove_top_card())

    def check_win(self,players,deck):
        if len(self.hand) == 0:
            ascii.redraw(players,deck)
            return True
        return False

    def get_most_color(self):
        num_red = 0
        num_blue = 0
        num_green = 0
        num_yellow = 0
        for card in self.hand:
            if card.color is not None:
                if card.color == "red":
                    num_red += 1
                elif card.color == "blue":
                    num_blue += 1
                elif card.color == "green":
                    num_green += 1
                elif card.color == "yellow":
                    num_yellow += 1
        num_colors = [num_red,num_blue,num_green,num_yellow]
        most = max(num_colors)
        if most == num_red:
            return "red"
        elif most == num_blue:
            return "blue"
        elif most == num_yellow:
            return "yellow"
        elif most == num_green:
            return "green"

    def take_turn(self, players, deck, next_turn, reverse):
        won = False
        most_color = self.get_most_color()
        print(self.name + " TURN TAKEN")
        self.say_turn = " MY TURN"
        ascii.redraw(players, deck)

        time.sleep(1)

        skip = False
        is_turn = True
        while is_turn:
            card_found = False

            # If next person's hand size is 1, try to find draw/skip card
            if len(players[next_turn].hand) == 1:
                for card in self.hand:
                    if card.type is not None:
                        if card.type == "draw_four" or card.type == "skip":

                            if card.type == "draw_four":
                                for i in range(4):
                                    players[next_turn].add_card(deck)

                                ind = self.hand.index(card)
                                deck.add_card_to_pile(self.hand.pop(ind))

                                new_color = self.get_most_color()
                                deck.get_top_pile().color = new_color
                                won = self.check_win(players,deck)
                                return [reverse, skip, won]

                            if card == "skip":
                                skip = True
                                ind = self.hand.index(card)
                                deck.add_card_to_pile(self.hand.pop(ind))
                                won = self.check_win(players,deck)
                                return [reverse, skip, won]

            for card in self.hand:
                if (card.color == deck.get_top_pile().color or card.number == deck.get_top_pile().number or (card.type is not None and card.type == deck.get_top_pile().type) and (card.type is not None and card.type != "draw_four") and (card.type is not None and card.type != "wild")):
                    card_found = True

                    if card.type is not None:
                        # If draw 2 played, next person draws 2. Simple.
                        if card.type == "draw_two":
                            players[next_turn].add_card(deck)
                            players[next_turn].add_card(deck)

                        # If draw 2 played, next person draws 2. Simple.
                        if card.type == "reverse":
                            reverse = not reverse

                        # If skip, skip. Simple.
                        if card.type == "skip":
                            skip = True

                    ind = self.hand.index(card)
                    deck.add_card_to_pile(self.hand.pop(ind))
                    won = self.check_win(players,deck)
                    is_turn = False
                    break

                elif card.type is not None:
                    if card.type == "draw_four":
                        for i in range(4):
                            players[next_turn].add_card(deck)
                        ind = self.hand.index(card)
                        deck.add_card_to_pile(self.hand.pop(ind))

                        new_color = self.get_most_color()
                        deck.get_top_pile().color = new_color
                        ascii.redraw(players, deck)
                        is_turn = False
                        break

                    elif card.type == "wild":
                        ind = self.hand.index(card)
                        deck.add_card_to_pile(self.hand.pop(ind))

                        new_color = self.get_most_color()
                        deck.get_top_pile().color = new_color
                        ascii.redraw(players, deck)
                        is_turn = False
                        break

            if not card_found:
                self.add_card(deck)
                ascii.redraw(players,deck)
                time.sleep(0.5)
            else:
                is_turn = False
        time.sleep(1)
        self.say_turn = " "
        return [reverse, skip, won]
    def __str__(self):
        out = "NAME: " + self.name + "\n"
        for card in self.hand:
            out += card.__str__() + "\n"
        return out
