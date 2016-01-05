#!/usr/bin/env python

"""
Numerical Recipes Project - Penney Ante
NAME: Tijn Kersjes
STUDENT ID: 11048018
"""

import random

def flipCoin(seq):

    heads = bool(random.getrandbits(1))
    return seq[1:] + ("H" if heads else "T")

def runMatch(players):

    ps = players[:]
    seq = "." * len(players[0])

    rounds = 0
    while seq != ps[0] and seq != ps[1]:
        rounds += 1
        seq = flipCoin(seq)

    winner = 0 if seq == ps[0] else 1

    return (rounds, winner)

def main():

    players = ["HTT", "HHT"]
    rounds, winner = runMatch(players)

    winner = "Anna" if winner == 1 else "Bob"
    print winner, "wins after", rounds, "rounds."

if __name__ == "__main__":
    main()
