import numpy as np
import matplotlib.pyplot as plt
def function_1(x):
    return x**2+x

def numerical(f,x):
    h=1e-2
    return (f(x+h)-f(x-h))/(2*h)

x=np.arange(0.0,20.0,0.1)# 以0.1为单位 从0到20的数组x
y=function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
#plt.show()
print(function_1(5))
print(numerical(function_1,5))
