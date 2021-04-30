import sys, os

from Player import *
from Deck import *
from ascii import *
from cpu import *


def get_turn(reverse, num_players, turn):

    if not reverse:
        if turn == num_players-1:
            turn = 0
        else:
            turn += 1
    else:
        if turn == 0:
            turn = num_players-1
        else:
            turn -= 1

    return turn
print(get_turn(False, 2, 2))
def menu():
    ascii.draw_menu()
    setup()

def setup():
    num_bots = int(input("How many bots to play against?\n"))

    players = []

    name = input("What is your name?\n")
    player = Player(name)
    players.append(player)

    for i in range(1, num_bots+1):
        players.append(cpu())

    deck = Deck()
    deck.shuffle()
    deck.add_top_card_to_pile()

    for player in players:
        for i in range(7):
            player.add_card(deck)

    play(players, deck)

def redraw(players, deck):
    os.system('cls')
    # Draw pile card at center
    ascii_centered_card = ascii.center_ascii_card(ascii.card_to_ascii(deck.get_top_pile()))
    print(ascii.get_board(players, ascii_centered_card))

    # Draw player's hand
    players[0].generate_ascii_hand()
    players[0].print_hand()

# Return index of card from action -- ex: "r1" to get index of red 1 card
# Returns -1 if card not found
def index_of_card(human, human_action):
    card_ind = 0
    found_ind = -1
    for card in human.hand:
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


def play(players, deck):
    playing = True
    reverse = False
    turn = 0
    human = players[0]
    while playing:
        redraw(players,deck)


        is_turn = True
        while is_turn:
            # Player makes action
            human_action = input("Your Move: ")

            if human_action == "c":
                human.hand.append(deck.remove_top_card())
                redraw(players,deck)

            else:
                # Check if player actually has that card
                found_ind = index_of_card(human, human_action)

                if found_ind != -1:
                    if human.hand[found_ind].type == "wild" or human.hand[found_ind].type == "draw_four":
                        deck.add_card_to_pile(human.hand.pop(found_ind))
                        is_turn = False
                    elif human.hand[found_ind].color == deck.get_top_pile().color or human.hand[found_ind].number == deck.get_top_pile().number or (human.hand[found_ind].type is not None and human.hand[found_ind].type == deck.get_top_pile().type):
                        deck.add_card_to_pile(human.hand.pop(found_ind))
                        is_turn = False
                    else:
                        redraw(players,deck)
                        print("You can't play " + human.hand[found_ind].__str__() + " right now!")
                else:
                    redraw(players,deck)
                    print("You don't have that card!")
        #Increment turn
        #turn = get_turn(reverse, len(players), turn)


menu()

input=("")