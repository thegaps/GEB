def FACTORIAL(N):
    if N == 0:
        return 0
    ans = 1
    factor = 1
    for i in range(N):
        ans *= factor
        factor += 1
    print ans
    return ans

#TESTS
#~ FACTORIAL(0)
#~ FACTORIAL(1)
#~ FACTORIAL(2)
#~ FACTORIAL(3)
#~ FACTORIAL(4)
