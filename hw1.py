# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
#HW1a
theta_a=np.linspace(0,2*np.pi,1000)
x_a=2*np.cos(theta_a)+np.cos(2*theta_a)
y_a=2*np.sin(theta_a)-np.sin(2*theta_a)
#HW1b
theta_b=np.linspace(0,10*np.pi,1000)
r_b=theta_b**2
x_b=r_b*np.cos(theta_b)
y_b=r_b*np.sin(theta_b)
#HW1c
theta_c=np.linspace(0,24*np.pi,1000)
r_c=np.exp(np.cos(theta_c))-(2*np.cos(4*theta_c))+(np.sin(theta_c/12))**5
x_c=r_c*np.cos(theta_c)
y_c=r_c*np.sin(theta_c)
#Graphing all into one figure
fig,(ax1,ax2,ax3)=plt.subplots(1,3)
fig.suptitle("HW1: Comp Meth by Shah")
ax1.plot(x_a,y_a)
ax1.set_title("HW1a\nDeltoid Curve")
ax1.set(xlabel="x",ylabel="y")
ax2.plot(x_b,y_b)
ax2.set_title("HW1b\nGalilean Spiral")
ax2.set(xlabel="x",ylabel="y")
ax3.plot(x_c,y_c)
ax3.set_title("HW1c\nFey's Function")
ax3.set(xlabel="x",ylabel="y")
fig.tight_layout()
plt.show()


