#!/usr/bin/env python

import random

def doRound(players):

    heads = bool(random.getrandbits(1))

    if heads:
        players[0] += 1
        players[1] -= 1
    else:
        players[1] += 1
        players[0] -= 1

def runMatch(players):

    rounds = 0
    while players[0] > 0 and players[1] > 0:
        rounds += 1
        doRound(players)

    return rounds

def main():

    players = [5, 10]
    rounds = runMatch(players)

    winner = "Anna" if players[0] == 0 else "Bob"
    print winner, "wins after", rounds, "rounds."

if __name__ == "__main__":
    main()
