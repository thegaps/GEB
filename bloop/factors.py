psuedo:
def FACTORS(N):
	for i in range(N-1):
		if REMAINDER(N,i) == 0:
			factors.pop(i)
	return factors
