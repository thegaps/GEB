#~ Determines if N is a perfect number.
#~ A perfect number has factors (divisor == factor?) that
	#~ sum up to itself

from factors import FACTORS


def IS_PERFECT(N):
	factors = FACTORS(N)
	factor_sum = 0
	for i in len(factors):
		factor_sum += factors(i)
	if (factor_sum == N):
		return True
	else:b h
		return False
	
#TESTS:
print IS_PERFECT(1)
print IS_PERFECT(2)
print IS_PERFECT(28)
print IS_PERFECT(29)
