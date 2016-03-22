# integer division of M by N

#~ keep adding to number of times to multiply N by x until we 
 #~ find situation where N*x = M or (N*x < M and N*(x+1) > M)
#~ The problem with this approach is how do we put a bound on it?
#   well, if N is greater than 0, then we should only let x get
#       as big as M

def DIVISION(M, N):
    # Easy cases:
    if N == 0:
        return 0    # 0? 1? undefined? Meatballs for dinner?
    elif M < N:
        return 0
    elif M==N:
        return 1
    else:
        # M > N
        x = 1
        for i in range(M):
            product = x * N
            if product == M:
                return x
            elif (product < M) and ((product+N) > M):
                return x
            x += 1
    return -1
#~ 
#~ print DIVISION(0,0)
#~ print DIVISION(0,1)
#~ print DIVISION(1,0)
#~ print DIVISION(6,4)
#~ print DIVISION(12,6)
#~ print DIVISION(5,2)
