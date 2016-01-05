#!/usr/bin/env python

"""
Numerical Recipes Project - Penney Ante
NAME: Tijn Kersjes
STUDENT ID: 11048018
"""

import sys
import random

def flipCoin(seq):

    heads = bool(random.getrandbits(1))
    return seq[1:] + ("H" if heads else "T")

def runMatch(players):

    ps = players[:]
    n = len(players[0])
    seq = "." * n

    rounds = 0
    while seq != ps[0] and seq != ps[1]:
        rounds += 1
        seq = flipCoin(seq)

    winner = 0 if seq == ps[0] else 1

    return (rounds, winner)

def main(players):

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

    avg_rounds = float(total_rounds) / iterations
    frac_anna_wins = 100 * total_anna_wins / iterations
    frac_bob_wins = 100 * total_bob_wins / iterations
    avg_rounds_if_anna_wins = float(rounds_if_anna_wins) / total_anna_wins
    avg_rounds_if_bob_wins = float(rounds_if_bob_wins) / total_bob_wins

    print "\n"
    print "Average number of rounds:", avg_rounds
    print "Wins by Anna:", str(frac_anna_wins) + "%", "(taking", avg_rounds_if_anna_wins, "rounds on average)"
    print "Wins by Bob:", str(frac_bob_wins) + "%", "(taking", avg_rounds_if_bob_wins, "rounds on average)"

if __name__ == "__main__":
    players_1 = ["HTT", "HHT"]
    players_2 = ["THH", "HHT"]

    print "Anna => Head - Head - Tails"
    print "Bob => Head - Tails - Tails"
    main(players_1)

    print "\n---------------------------\n"
    
    print "Anna => Tails - Head - Head"
    print "Bob  => Head - Head - Tails"
    main(players_2)
