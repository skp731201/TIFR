import numpy as np
def f(x):
    return 10-3*(x**2)
a=float(input("Enter the lower value:"))
b=float(input("Enter the upper bound:"))
n=int(input("Enter the number of intervals you want:"))
h=float((b-a)/n)
valueodd=0.0
valueeven=0.0
x=np.linspace(a,b,n)
for i in range(1,n):
    if i%2==0:
        valueeven +=2*f(x[i])
    else:
        valueodd +=4*f(x[i])
value=(h/3)*(f(a)+f(b)+valueodd+valueeven)
print("The integrationvalue:",value)

