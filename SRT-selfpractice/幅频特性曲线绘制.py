import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.ndimage import gaussian_filter1d
x=np.array([3,4,5,6,7,8,9,10,11,12,13,14,15,20,25,30])
y11=np.array([0.080,0.114,0.158,0.219,0.312,0.473,0.828,1.815,1.471,0.803,0.551,0.421,0.345,0.188,0.132,0.102])
y22=np.array([0.079,0.114,0.158,0.217,0.307,0.458,0.766,1.392,1.248,0.766,0.539,0.416,0.342,0.188,0.132,0.102])
y33=np.array([0.079,0.114,0.156,0.214,0.300,0.439,0.690,1.072,1.027,0.713,0.522,0.410,0.339,0.188,0.133,0.102])
y1 = gaussian_filter1d(y11, sigma=1.5)
y2 = gaussian_filter1d(y22, sigma=1.5)
y3 = gaussian_filter1d(y33, sigma=1.5)
plt.scatter(x, y1)
plt.scatter(x, y2)
plt.scatter(x, y3)
plt.plot(x,y1,label="I=0.6A")
plt.plot(x,y2,label="I=0.8A")
plt.plot(x,y3,label="I=1.0A")
plt.title("幅频特性曲线", fontproperties="SimHei")
plt.xlabel("简谐激励振动频率(Hz)", fontproperties="SimHei")
plt.ylabel("振幅比(mm/N)", fontproperties="SimHei")
plt.legend()
plt.show()