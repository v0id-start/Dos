import sys
import os

from Player import *
from Deck import *
from ascii import *
from cpu import *

# System call
os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


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
print(get_turn(True, 3, 2))
def menu():
    print(style.CYAN)
    ascii.draw_menu()
    setup()

def setup():

    num_bots = int(input("How many bots to play against? (1-3)\n"))

    while num_bots < 1 or num_bots > 3:
        num_bots = int(input("How many bots to play against? (1-3)\n"))

    players = []

    name = input("What is your name?\n")
    player = Player(name)
    players.append(player)

    for i in range(1, num_bots+1):
        players.append(cpu())

    deck = Deck()
    deck.shuffle()
    deck.add_top_card_to_pile()

    num_start_cards = 7
    for player in players:
        for i in range(num_start_cards):
            player.add_card(deck)

    play(players, deck)




print(style.RESET)

def play(players, deck):
    print(style.RESET)
    playing = True
    reverse = False
    skip = False
    turn = 0
    next_turn = 1
    human = players[0]
    game_info = [reverse, skip]
    while playing:
        ascii.redraw(players,deck)

        next_turn = get_turn(reverse, len(players), turn)

        if turn == 0:
            game_info = human.take_turn(players, deck, next_turn, reverse)
            reverse = game_info[0]
            skip = game_info[1]
            won = game_info[2]
            if won:
                print(style.GREEN)
                ascii.human_win()
                playing = False
        else:
            game_info = players[turn].take_turn(players, deck, next_turn, reverse)
            reverse = game_info[0]
            skip = game_info[1]
            won = game_info[2]
            if won:
                print(style.MAGENTA)
                ascii.cpu_win()
                playing = False
        if skip:
            turn = get_turn(reverse, len(players), turn)
            skip = False

        turn = get_turn(reverse, len(players), turn)


menu()

input=("")
