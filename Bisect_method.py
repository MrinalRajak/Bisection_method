

#Root finding by bisection method

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import sys

def f(x):
    return x**3-3*x+1.06

#Plotting the given function
x=np.linspace(-5,5,100)
plt.plot(x,f(x))
plt.grid(True)
plt.show()
a=float(input("Enter the lower limit: "))
b=float(input("Enter the upper limit: "))
tol=float(input("Enter the tolerance: "))
if f(a)*f(b)>0:
    print("No roots exist in this interval")
    sys.exit()

while(abs(b-a)>=tol):
    xm=0.5*(a+b)
    if f(xm)==0:
        print("The root is: ",xm)
        sys.exit()
    if f(a)*f(xm)<0:
        b=xm
    else:
        a=xm

print("The root is: ",xm)
print("The root finding using scipy")
print(opt.bisect(f,a,b))
