# every even number can be represented as the sum of two primes

from prime import PRIME
from minus import MINUS

def GOLDBACH(N):
    cell = 2
    for i in range(N):
        if PRIME(cell) and PRIME(MINUS(N, cell)):
            return True
        cell += 1
    return False

#TESTS:
#~ print GOLDBACH(4)
#~ print GOLDBACH(22)
#~ print GOLDBACH(62)
#~ print GOLDBACH(93)
#~ print GOLDBACH(94)
