#Constants
G = 6.674e-11 #Grav. Constant
M = 5.974e24 #Mass of Earth
m = 7.348e22 #Mass of Moon
R = 3.884e8 #Earth-Moon distance
w = 2.662e-6 #Omega

#Equation of circular orbit motion
def func(r):
    return (G*M/r**2)-(G*m/(R-r)**2)-(w**2)*r

#Derivative equation of circular orbit motion
def derivative_func(r):
    return (-2*G*M/r**3)-(2*G*m/(R-r)**3)-(w**2)

#Initial root estimate 
r=R/2
#Maximum iterations
max_iter=100
#Accuracy 
acc=1e-5

#Newton's method
for iter in range(max_iter+1):
    delta_r=-func(r)/derivative_func(r) #calculate delta_r
    r=r+delta_r #updare r
    if abs(delta_r)<=acc:
        break
    
#Print output
if iter >= max_iter:
    print("Maximum number of iterations reached")
else:
    print(f"The Lagrange point from the earth center to the L1 point is r={r} m")