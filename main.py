import sys

from Player import *
from Deck import *
"""
 --
|  |
|  |
|  |
 --
 """

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
    print("WELCOME TO DOS")
    print("--------------")
    setup()

def setup():
    num_players = int(input("How many bots to play against?\n"))

    players = []
    for i in range(1, num_players+1):
        name = input("What is the name of player %s?\n" % str(i))
        player = Player(name)
        players.append(player)

    deck = Deck()
    deck.shuffle()
    deck.add_card_to_pile()

    for player in players:
        for i in range(7):
            player.add_card(deck)
        print(player)

    play(players, deck)
    print(deck.get_top_pile())

def play(players, deck):
    playing = True
    reverse = False
    turn = 0
    while playing:
        #Player makes action

        #Increment turn
        turn = get_turn(reverse, len(players), turn)


#menu()


input=("")

cards = ["""
 ----------------
| @@@@ RED  @@@@ |
|       _        |
|      / |       |
|      - |       |
|      | |       |
|      | |       |
|      |_|       |
|                |
| @@@@ RED  @@@@ |
 ----------------
""","""
 ----------------
| @@@@ RED  @@@@ |
|       _        |
|      / |       |
|      - |       |
|      | |       |
|      | |       |
|      |_|       |
|                |
| @@@@ RED  @@@@ |
 ----------------""","""
 ----------------
| @@@@ RED  @@@@ |
|       _        |
|      / |       |
|      - |       |
|      | |       |
|      | |       |
|      |_|       |
|                |
| @@@@ RED  @@@@ |
 ----------------"""]
def print_hand(hand):
    lines = [cards[i].splitlines() for i in range(len(cards))]
    for l in zip(*lines):
        print(*l, sep='' + "\t")

print_hand(cards)