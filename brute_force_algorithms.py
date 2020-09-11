'''
A brute force algorithm solves a problem by exhaustively searching all possible
solutions without using an understanding of the mathematical structure in the problem to eliminate steps
'''
import time
from math import sqrt, floor


def brute_force(number):
    n = number
    x = 2
    for i in range(x, n - 1):
        if n % i == 0:
            return("Composite")
    else:
        return ("Prime")

def improved_brute_force(number):
    n = number
    x = 2
    for i in range(x, int(sqrt(n))):
        if n % i == 0:
            return("Composite")
    else:
        return ("Prime")

millis = int(round(time.time() * 1000))
print(brute_force(11) + " completed in " + str(millis) + " milliseconds")

print(improved_brute_force(11) + " completed in " + str(millis) + " milliseconds")