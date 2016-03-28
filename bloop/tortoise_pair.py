# checks for the tortoise property

# True if M and M+N prime
# Are AND operations allowed?
# seems like multiply, so should be

from prime import PRIME

def TORTOISE_PAIR(M,N):
    return (PRIME(M) and PRIME(M+N))

print TORTOISE_PAIR(4, 98)
print TORTOISE_PAIR(5, 98)    
print TORTOISE_PAIR(5, 100)
print TORTOISE_PAIR(5, 1742)
