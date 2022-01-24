import numpy as np
x=np.array([0,1,2])
y=np.array([1,2,4])
x0=1.5
value=0.0

for i in range (3):
    L=1.0
    for j in range(3):
        if i!=j:
            L *= (x0-x[j])/(x[i]-x[j])
            
    value +=y[i]*L
print(value)    

