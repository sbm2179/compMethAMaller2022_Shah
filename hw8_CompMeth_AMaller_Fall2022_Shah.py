#Imports
import numpy as np
import matplotlib.pyplot as plt

#Part-2: Write a program that solves the equations and plot 

#Define the constants given in the problem
theta=30*np.pi/180 #initial angle (radian)
v_initial=100 #m/s
vx_initial=v_initial*np.cos(theta) #x-component of velocity
vy_initial=v_initial*np.sin(theta) #y-component of velocity
x_initial=0
y_initial=0
t_initial=0.0
t_final=10.0
h=0.01 #best h value after experimenting different h-values
g=9.81 #m/s^2
C=0.47 #coefficient of drag
R=0.08 #m
rho=1.22 #kg/m^3 

#Define function for calculating the differential equations
def f(r, constants_product):
  x=r[0]
  y=r[1]
  fx=r[2]
  fy=r[3]
  fxv=(-1)*constants_product*fx*np.sqrt(fx**2+fy**2)
  fyv=(-1*g)-constants_product*fy*np.sqrt(fx**2+fy**2)
  return np.array([fx,fy,fxv,fyv])

#Create method to calculate the trajectory of an object
def cannonball_trajectory(mass):
  t_points=np.arange(t_initial,t_final+h,h)
  r_points=np.zeros((len(t_points),4))
  r_points[0,:]=[x_initial,y_initial,vx_initial,vy_initial]
  constants_product=(np.pi*R**2*rho*C)/(2.0*mass)

#Implement Runge-Kutta method for each value of t
  for i in range(1,len(t_points)):
    k1=f(r_points[i-1,:],constants_product)
    k2=f(r_points[i-1,:]+(h/2)*k1,constants_product)
    k3=f(r_points[i-1,:]+(h/2)*k2,constants_product)
    k4=f(r_points[i-1,:]+h*k3,constants_product)
#Do not add negative values to array 
    if (r_points[i-1,:][0]>=0) and (r_points[i-1,:][1]>=0):
      r_points[i,:]=r_points[i-1,:]+(h/6)*(k1+2*k2+2*k3+k4)
    else:
      break

#Do not return the part of the array that is still filled with 0
  return r_points[:i]

result=cannonball_trajectory(1) # initial mass in kg

# Plot the y values as a function of x
plt.plot(result[:,0],result[:,1],'black')
plt.title('Cannonball trajectory with air resistance')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()

#Part-3: plot a series of trajectories for cannonballs of different masses
    
mass_one_trajectory=cannonball_trajectory(1.0)
mass_two_trajectory=cannonball_trajectory(2.0)
mass_three_trajectory=cannonball_trajectory(3.0)
mass_four_trajectory=cannonball_trajectory(4.0)

plt.plot(mass_one_trajectory[:,0],mass_one_trajectory[:,1])
plt.plot(mass_two_trajectory[:,0],mass_two_trajectory[:,1])
plt.plot(mass_three_trajectory[:,0],mass_three_trajectory[:,1])
plt.plot(mass_four_trajectory[:,0],mass_four_trajectory[:,1])
plt.plot()
plt.title('Cannonball trajectory with air resistance (Different mass)')
plt.xlabel('Distance (m)')
plt.ylabel('Altitude (m)')
plt.legend(('1kg','2kg','3kg','4kg'))
plt.show()
