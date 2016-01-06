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

def generateSequences(n):
    seqs = []
    for i in range(2**n):
        seq = ""
        for j in range(n):
            seq = ("T" if (i & 2**j) else "H") + seq
        seqs += [seq];
    return seqs

def displayStats(players):

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
            total_anna_wins += 1
            rounds_if_anna_wins += rounds
        else:
            total_bob_wins += 1
            rounds_if_bob_wins += rounds

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

def assignmentA():
    players_a = ["HHT", "HTT"]
    print "Anna =>", players_a[0]
    print "Bob  =>", players_a[1]
    displayStats(players_a)

def assignmentB():
    players_b = ["HHT", "THH"]
    print "Anna =>", players_b[0]
    print "Bob  =>", players_b[1]
    displayStats(players_b)

def assignmentC():
    iterations = 25000
    n = 3
    possibleSeqs = generateSequences(n)

    # for all possible sequences that Anna can pick
    for a in possibleSeqs:
        best_seq = ""
        best_score = -1

        # check all possible counter sequences for Bob
        for i in range(2**n):

            b = possibleSeqs[i]

            # calculate winning odds
            anna_win = 0
            bob_win = 0

            for j in range(iterations):

                _, winner = runMatch([a, b])

                if winner == 0:
                    anna_win += 1
                else:
                    bob_win += 1

                sys.stdout.write("\rAnna picks " + a + " => Flipping coins... " + str(100 * (i * iterations + j) / (2**n * iterations)) + "% ")
                sys.stdout.flush()

            score = int(round(float(bob_win) / float(anna_win)))

            # find the best counter strategy
            if score > best_score:
                best_score = score
                best_seq = b

        sys.stdout.write("\rAnna picks " + a + " => Bob should pick " + best_seq + " (" + str(best_score) + " to 1)\n")

def main():
    assignmentA()
    print "\n---------------------------\n"
    assignmentB();
    print "\n---------------------------\n"
    assignmentC();

if __name__ == "__main__":
    main()
