# Is memory allowed?
#   what is memory?
from minus import MINUS

def FIBO(N):
    if N == 0:
        return 0
    new_result = 1
    prior_result = 1
    two_prior_result = 0
    for i in range(MINUS(N,1)):
        new_result = prior_result + two_prior_result
        two_prior_result = prior_result
        prior_result = new_result
    return new_result
#~ TESTS
print FIBO(0)
print FIBO(1)
print FIBO(2)
print FIBO(3)
print FIBO(4)
print FIBO(9)

