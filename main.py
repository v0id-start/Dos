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
print(get_turn(True, 3, 2))
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






def play(players, deck):
    playing = True
    reverse = False
    turn = 0
    human = players[0]
    while playing:
        ascii.redraw(players,deck)

        if turn == 0:
            human.take_turn(players, deck)
            #Increment turn
        else:
            players[turn].take_turn()
        #turn = get_turn(reverse, len(players), turn)


menu()

input=("")
