from scipy.interpolate import CubicSpline
import numpy as np
x=np.array([0,1,2])
y=np.array([1,2,4])
s=CubicSpline(x,y)
V_1=s(1.5)
V_2=pow(2,1.5)
print("Interpolated value using library function:",V_1)
print("Original Value:",V_2)
