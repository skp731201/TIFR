def f(x):
    return(x**2-10)
def fprime(x):
    return 2*x
x_0=float(input("Enter the initial value of x:"))
for i in range(0,100):
    x_0=x_0-f(x_0)/fprime(x_0)
print("The root is:",x_0)    
    
