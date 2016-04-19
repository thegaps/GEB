#   pi/6 = 1/1^2 + 1/2^2 . . . 
# Haven't checked for legality
# doesn't actually find the digit

from numpy import sqrt, pi

# How do you put a bound on the sequence, so we
#   can get to a desired d.p.

# Riemann related:
def PI_RIE(N):
    if N == 0:
        return 0
    ans = 0
    for i in range(1,N):
        #~ print i**2
        frac = 1.0/(i**2)
        ans += frac
        #~ print frac
    return sqrt(ans*6)

# Nilakantha sequence
def PI_THA(N):
    d_fac = 3 # middle factor in denominator
    sign = 1
    ans = 3
    for i in range(N):
        frac = sign * 4.0/((d_fac-1)*d_fac*(d_fac+1))
        ans += frac
        d_fac += 2
        sign *= -1        
        print('%i\t%.20f\t%.20f' % (i, ans, ans - pi))
    return ans
    
#~ print PI_THA(0)
#~ print PI_THA(1)
#~ print PI_THA(2)
print PI_THA(1000000) # 14 digits until error hits (numerical error)

#~ print PI_DIGIT(0)
#~ print PI_DIGIT(1)
#~ print PI_DIGIT(2)
#~ print PI_DIGIT(300)

# Ideas:
#~ Use regular polygons
	#~ find relationship between accuracy and number of sides of polygon

