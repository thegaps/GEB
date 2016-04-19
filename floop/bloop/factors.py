# returns a list of all the factors of a number, N.
# in ascending order.
# each factor is returned only once.
# N is not included in the list of factors.

from minus import MINUS
from remainder import REMAINDER


def FACTORS(N):
	factors = []
	for i in range(1,N):
		if REMAINDER(N,i) == 0:
			factors.append(i)
	return factors

#TESTS:
#~ print FACTORS(1)
#~ print FACTORS(2)
#~ print FACTORS(3)
#~ print FACTORS(4)
#~ print FACTORS(5)
#~ print FACTORS(6)
#~ print FACTORS(24)
#~ print FACTORS(28)
