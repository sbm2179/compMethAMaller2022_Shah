#Solving NLSE for ligh pulses in a medium using finite difference method
#imports
import numpy as np
import matplotlib.pyplot as plt
import numba

#Properties of the light pulses
P=1e-6 #Pulse peak power in Watt
D=1e-6 #Pulse cross-section diametter in meter
tau=10e-12 #Pulse width in second 


#Properties of the propagating medium (Silica)
b2=0.06e-24   #beta 2 GVD parameter in s2/m
gamma=0.015   #SPM Nonlinearity coefficent in W-1.m-1

#Setting up the data points for distance and time
Nt = 301
Nx = 11
dt = 1/(Nt-1)
dx=1e-5
t = np.linspace(0, 10*tau, Nt)

#Setting up initial Amplitude time profile
I=P/(D)**2
A0=np.sqrt(I)*np.exp(-(t/(tau/np.sqrt(2*np.log(2))))**2)

#Setting up the matrix with initial condition
A=np.zeros([Nx,Nt],dtype = "complex_")
A[0]=A0

#Finite difference method to solve NLSE
@numba.jit("c16[:,:](c16[:,:])", nopython=True, nogil=True)
def comp_A(A):
    for i in range(0,Nx-1):
        for j in range(0,Nt-1):
            A[i+1][j]=A[i][j]-((1j*b2/2)*(dx/dt**2)*(A[i][j+1]-2*A[i][j]+A[i][j-1]))+((1j*gamma*dx*I)*A[i][j])
    return A

#Solving the equation
A_dfm=comp_A(A)

#Graphing the solutions
for i in range(0,Nx):
    plt.plot(t,np.absolute(A_dfm[i]),label=str((1e-7)*i)+" meter")
    plt.legend()
    plt.xlim(0,0.2e-10)
    plt.xlabel("Time in seconds")
    plt.ylabel("Amplitude (Arb. Unit)")
    plt.pause(0.001)
    
for i in range(0,Nx):
    plt.plot(t,np.absolute(A_dfm[i]),label=str((1e-7)*i)+" meter")
    plt.xlim(0,0.2e-10)
    plt.legend()
plt.xlabel("Time in seconds")
plt.ylabel("Amplitude (Arb. Unit)")
plt.show() 


