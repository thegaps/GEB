# Goldback conjecture: 
#	every even number can be represented as the sum of two primes
# Tortoise property:
#	An even number, 2N, has the Tortoise property if it is the 
#	difference of two odd primes.

# WHAT IS A TORTOISE PAIRS RELATION TO A TORTOISE #??!!
# two odd primes, where one minus the other is a Tortoise #.


# Check if given numbers are a Tortoise pair
#--------------------------------

# True if M and M+N prime
# Are AND operations allowed?
# seems like multiply, so should be

# All prime numbers, except 2, are odd.
# If both numbers are primes, and neither is equal to 2,
#	then they are both odd primes.

from prime import PRIME

def TORTOISE_PAIR(M,N):
    return (PRIME(M) and PRIME(M+N))

print TORTOISE_PAIR(4, 98)
print TORTOISE_PAIR(5, 98)    
print TORTOISE_PAIR(5, 100)
print TORTOISE_PAIR(5, 1742)


#~ for the Tortoise property
