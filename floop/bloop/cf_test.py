frac_sum = 0
print('Current term\t\t\tCombined term')
for i in range(1,100):
    frac = 1 / (2**i)
    frac_sum += frac
    print('{0:.10f}\t\t\t{1:.10f}'.format(frac,frac_sum))
    
