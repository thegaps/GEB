# True if M and M+N prime

from prime import PRIME

def TORTOISE_PAIR(M,N):
    return (PRIME(M) and PRIME(M+N))
    
print TORTOISE_PAIR(5, 100)
print TORTOISE_PAIR(5, 1742)
