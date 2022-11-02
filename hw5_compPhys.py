#imports
import numpy as np
import matplotlib.pyplot as plt

#7.4(a) Read in the data from dow.txt
dow=np.loadtxt("dow.txt")

#7.4(a) plot them on a graph
plt.plot(dow)
plt.show()

#7.4(b) Calculate the coefficients of the discrete Fourier transform of the data using the function rfft from numpy.fft
dft=np.fft.fft(dow)

#7.4(c) Set all but the first 10% of the elements of this array to zero
dft[102:]=0 #taking first 10%, everything else is zero

#7.4(d) Calculate the inverse Fourier transform of the resulting array, zeros and all, using the function irfft
idft=np.fft.irfft(dft)

#7.4(e) Plot it on the same graph as the original data
plt.plot(dow,"k",label="dow")
plt.plot(idft,"b",label="10%")
plt.legend()
plt.tight_layout()
plt.show()
#Comment: Data got smoother than the original 

#7.4(e) Modify your program so that it sets all but the first 2% of the coefficients to zero and run it again.
dft2=np.fft.fft(dow)
dft2[21:]=0 #taking first 2%, everything else is zero
idft2=np.fft.irfft(dft2)
plt.plot(dow,"k",label="dow")
plt.plot(idft2,"b",label="2%")
plt.legend()
plt.show()
#Comment: Data got even more smoother than 10%


#7.6(a) Write a program similar to the one for Exercise 7.4, part (e), in which you read the data in the file dow2.txt and plot it on a graph. Then smooth the data by calculating its Fourier transform, setting all but the first 2% of the coefficients to zero, and inverting the transform again, plotting the result on the same graph as the original data.
dow2=np.loadtxt("dow2.txt")
dft3=np.fft.fft(dow2)
dft3[21:]=0 #taking first 2%, everything else is zero
idft3=np.fft.irfft(dft3)
plt.plot(dow2,"k",label="dow")
plt.plot(idft3,"b",label="2%")
plt.legend()
plt.show()

#7.6(b)  Modify your program to repeat the same analysis using discrete cosine transforms
#defininf discrete cosine transforms
def dft_cos(y):
    N=len(y)
    c=np.zeros([N],complex)
    for k in range(N):
        for n in range(N):
            c[k]+=y[n]*np.exp(-2j*np.pi*k*n/N)
    return c

#Doing the 2% smoothening
dft4=dft_cos(dow2)

dft4[21:]=0 #taking first 2%, everything else is zero
idft4=np.fft.irfft(dft4)
plt.plot(dow2,"k",label="dow")
plt.plot(idft4,"b",label="2% with DFT Cosine")
plt.legend()
plt.show()


