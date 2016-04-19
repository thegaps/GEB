def MINUS(M,N):
    ans = 0
    if M < N:
        return ans
    else:
        for x in range(M+1):
            if ans+N == M:
                return ans
            else:
                ans +=1
    print 'MINUS error!'
    return -1

# TESTS:
#~ print MINUS(10,5)
#~ print MINUS(53,6)
#~ print MINUS(2,20)
