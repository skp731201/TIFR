def f(x):
    return 10-x**2
a=-2.0
b=2.0
n=int(input("Enter the number of steps:"))
h= float((b-a)/n)
s=0.0
s+=f(a)/2.0

for i in range(1,n):
    s+=f(a+i*h)
s+=f(b)/2.0
print("The value of the integration is:", s*h)
