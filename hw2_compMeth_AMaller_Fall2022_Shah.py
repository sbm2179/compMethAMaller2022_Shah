#HW-2: Integrating with Trapezoidal Method
#imports
import numpy as np
import matplotlib.pyplot as plt


#defining integrating function
def func(t):
    return np.exp(-t**2)

#Defining integration using trapezoidal method
def E(b):
    a=0
    N=100
    del_x=(b-a)/N
    s=(0.5*func(a))+(0.5*func(b))
    
    for i in range(1,int(N)):
        s+=func(a+i*del_x)
    
    return(del_x*s)

#calculating and printing E(x) for x from 0 to 3 with step 0.1
x=np.linspace(0,3,int(3-0/0.1))

for i in x:
    print(i, E(i))

#plotting E(x) vs x
plt.plot(x,E(x))
plt.suptitle("E(x) vs x using trapezoidal method")
plt.xlabel("x")
plt.ylabel("E(x)")
plt.show()

