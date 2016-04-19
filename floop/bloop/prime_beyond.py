# Not bloop

# The lowest prime number beyond N

from prime import PRIME

def PRIME_BEYOND(N):
	number_beyond = N+1
	# loops indefinitely
	while(1):
		if (PRIME(number_beyond)):
			return (number_beyond)
		else:
			number_beyond++
