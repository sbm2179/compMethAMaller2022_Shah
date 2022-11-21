from pylab import *

N = 10000000

z = random(N)
x = z**2

def g(x):
    return 1/(1+exp(x))

I = sum(g(x))/N*2


print('I = {}'.format(I))
