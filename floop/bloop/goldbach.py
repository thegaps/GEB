# every even number can be represented as the sum of two primes

from prime import PRIME
from minus import MINUS

# Incrementally search each number less than the target number. If the
#	current number is a prime, then check if the target number less the
#	current number is also a prime. If so, we have found the two primes
# 	which make N a Goldbach number.
 
def GOLDBACH(N):
    cell = 2
    for i in range(N):
        if PRIME(cell) and PRIME(MINUS(N, cell)):
            return True
        cell += 1
    return False
																			   reeeee
#TESTS:
#~ print GOLDBACH(4)
#~ print GOLDBACH(22)
#~ print GOLDBACH(62)
#~ print GOLDBACH(93)
#~ print GOLDBACH(94)
