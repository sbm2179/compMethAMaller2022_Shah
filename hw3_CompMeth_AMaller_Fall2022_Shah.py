#imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


#defining potential due to charge q at r_0
def potential(q,r_0,x,y,k=1):
    r_main=np.hypot(x-r_0[0],y-r_0[1])
    return k*q/(r_main+0.001)


#making the grid points and meshes
n_x, n_y=100, 100
x=np.linspace(-50,50,n_x)
y=np.linspace(-50,50,n_y)
X, Y = np.meshgrid(x,y)


#calculating potentials due to charges
charges = [(-1,(5,0)),(1,(-5,0))]
V = np.zeros((n_x,n_y))
for q_char in charges:
    e_v=potential(*q_char,x=X,y=Y)
    V += e_v
    

#Plotting the potential contour plot
fig_1 = plt.figure(figsize=(7,7))
plt.contourf(X, Y, V, 20, cmap='RdGy')
plt.colorbar()
plt.suptitle("E-Potentials due to two charges",fontsize=25)


#Gradient of potential
E_y,E_x = np.gradient(V, x, y)


#Plotting electric field 
#where color brightness tells the magnitdue of the field
fig_2 = plt.figure(figsize=(8,8))
ax = fig_2.add_subplot(111)
color=np.log(np.hypot(E_x,E_y))
ax.streamplot(X,Y,E_x,E_y,color=color,linewidth=1,cmap=plt.cm.inferno,density=1,arrowstyle="->",arrowsize=1.5)
charge_colors={True:"#aa0000",False:"#0000aa"}
for q, pos in charges:
    ax.add_artist(Circle(pos,1,color=charge_colors[q>0]))
plt.suptitle("E-fields due to two charges",fontsize=25)