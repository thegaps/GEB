# remainder of M divided by N
# if N is larger than M, return M

from division import DIVISION

def REMAINDER_MAGIC(M, N):
    # using magic operator found on-the-line:
    return M - (M // N * N)
    # // returns quotient without remainder.
    # not sure if that is fair play.
    # additionally the behaviour is different for different py versions 
    # '-' also not allowed
    
def REMAINDER(M, N):
    # my naive implementation
    # is checking if a number is an integer allowed?
    # what kind of process is that check?
    # => I will work 'backwards' and multiply instead.
    # DONE/FIXED! implemented divison first, so I can call that here.
        
    #Silly cases:
    if M < N:
        return M
    elif M==N:
        return 0
    # legit case:
    else:
        # M > N
        rem = 0
        return M-(N*DIVISION(M,N))
    print 'REMAINDER error'
    return -1

#~ print REMAINDER(5,1)
#~ print REMAINDER(5,2)
#~ print REMAINDER(0,1)
#~ print REMAINDER(25,11)
#~ print REMAINDER(1,2)
