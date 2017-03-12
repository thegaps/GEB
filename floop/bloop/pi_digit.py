#   pi/6 = 1/1^2 + 1/2^2 . . . 
# Haven't checked for legality
# doesn't actually find the digit

# no methods presented in the book until this
# point except for the cont frac pi/4 method

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

# Pi/4 sequence
# should be able to reason at what point continued fraction
# expansion will not change the last digit.
def PI_FE(N):

    # if we want the Nth digit (after the d.p.), we only need
    # to work out the fractions that can change the
#    10 ^ - N
#    e.g. want 3rd digit:
#    3.141
#    10 ^ - 3 = 0.001.
#    How do we know when we can't affect it?
#    if we were doing 1/2's:
#    1/2 + 1/4 + 1/8 + 1/16 + 1/32
#    0.5 + 0.25 + 0.125 + 0.0625
#    in this case all the remaining terms will not be greater than
#    the current term.
#    what's the threshold? (early guess: something to do with e)
#    Oh but it can! what if there is an asymptote near a relatively
#    large digit? then:
#    0.3232429999999 could change to
#    0.3232430000000 with a weanie little bit.
#
#    how to reason about that?
    
#    I almost have to compute what would be required for a digit change,
#    and compare it to what is changing, to check on the fly if a
#    change is possible.

    
    # just calc N fractions so I have something to look at:
    frac_sum = 0
    sign = 1
    print("""Current term\t\t\tCombined term
------------\t\t\t-------------""")
    for fraction_number in range(1,N+1):
        denom = fraction_number*2 - 1
        frac = sign * 1 / denom
        frac_sum += frac
        sign *= -1
        print('{0:.9f}\t\t\t{1:.10f}'.format(frac,frac_sum))

    return frac_sum * 4
    
#~ print PI_THA(0)
#~ print PI_THA(1)
#~ print PI_THA(2)
#print PI_THA(1000000) # 14 digits until error hits (numerical error)

#~ print PI_DIGIT(0)
#~ print PI_DIGIT(1)
#~ print PI_DIGIT(2)
#~ print PI_DIGIT(300)

# Ideas:
#~ Use regular polygons
	#~ find relationship between accuracy and number of sides of polygon
