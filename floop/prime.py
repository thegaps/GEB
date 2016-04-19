from bloop import minus, remainder

# from book
# does not identify 1 correctly

def PRIME(N):
    if N == 0:
        return False
    cell = 2
    for i in range(MINUS(N,2)):
        if REMAINDER(N,cell) == 0:
            return False
        cell += 1
    return True

# TESTS:
#~ print PRIME(0)	#false
#~ print PRIME(1)	#false
#~ print PRIME(2)	#true
#~ print PRIME(3)
#~ print PRIME(100)
#~ print PRIME(101)
#~ print PRIME(11)
