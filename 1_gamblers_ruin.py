#!/usr/bin/env python

import random

def doRound(ps):

    heads = bool(random.getrandbits(1))

    if heads:
        ps[0] += 1
        ps[1] -= 1
    else:
        ps[1] += 1
        ps[0] -= 1

def runMatch(players):

    ps = players[:]

    rounds = 0
    while ps[0] > 0 and ps[1] > 0:
        rounds += 1
        doRound(ps)

    winner = 1 if ps[0] == 0 else 0

    return (rounds, winner)

def main():

    players = [5, 10]
    rounds, winner = runMatch(players)

    winner = "Anna" if winner == 1 else "Bob"
    print winner, "wins after", rounds, "rounds."

if __name__ == "__main__":
    main()
