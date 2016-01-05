#!/usr/bin/env python

"""
Numerical Recipes Project - Gambler's Ruin
NAME: Tijn Kersjes
STUDENT ID: 11048018
"""

import sys
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
    iterations = 100000

    total_rounds = 0
    total_anna_wins = 0
    rounds_if_anna_wins = 0
    total_bob_wins = 0
    rounds_if_bob_wins = 0

    for i in range(iterations):
        rounds, winner = runMatch(players)

        total_rounds += rounds
        if winner == 0:
            total_bob_wins += 1
            rounds_if_bob_wins += rounds
        else:
            total_anna_wins += 1
            rounds_if_anna_wins += rounds

        sys.stdout.write("\rFlipping coins... " + str(100 * (i+1) / iterations) + "% ")
        sys.stdout.flush()

        # winner = "Anna" if winner == 1 else "Bob"
        # print winner, "wins after", rounds, "rounds."

    avg_rounds = total_rounds / iterations
    frac_anna_wins = 100 * total_anna_wins / iterations
    frac_bob_wins = 100 * total_bob_wins / iterations
    avg_rounds_if_anna_wins = rounds_if_anna_wins / total_anna_wins
    avg_rounds_if_bob_wins = rounds_if_bob_wins / total_bob_wins

    print "\n"
    print "Average number of rounds:", avg_rounds
    print "Wins by Anna:", str(frac_anna_wins) + "%", "(taking", avg_rounds_if_anna_wins, "rounds on average)"
    print "Wins by Bob:", str(frac_bob_wins) + "%", "(taking", avg_rounds_if_bob_wins, "rounds on average)"


if __name__ == "__main__":
    main()
