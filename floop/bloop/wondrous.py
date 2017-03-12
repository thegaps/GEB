# Can I put a bound on this loop?
# No. => Not Bloop.


# odd     -> triple + 1
# even    -> half
# reach 1 -> WONDROUS
# don't   -> UNWONDROUS

from even import IS_EVEN
from division import DIVISION

def IS_WONDROUS(N):

    # note the number of steps taken
    step_count = 0
    
    while N != 1:  # ! NOT BLOOP

        # Update the user
        print step_count, '\t\t', N
        
        if IS_EVEN(N):
            N = DIVISION(N,2)
        else:
            N = (3 * N) + 1
        step_count+=1
        
    return True
