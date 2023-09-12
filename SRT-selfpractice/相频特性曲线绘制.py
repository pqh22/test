import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.ndimage import gaussian_filter1d
x=np.array([3,4,5,6,7,8,9,10,11,12,13,14,15,20,25,30])
y11=np.array([-5.1,-6.3,-7.7,-9.6,-12.2,-17.0,-27.4,-64.1,-136.6,-158.4,-166.1,-169.9,-172.2,-178.3,-181.4,-183.4])
y22=np.array([-5.7,-7.3,-9.1,-11.5,-15.1,-21.1,-33.9,-68.9,-126.9,-151.4,-161.1,-166.1,-169.2,-176.6,-180.2,-182.5])
y33=np.array([-6.7,-8.7,-10.9,-14.0,-18.5,-26.0,-40.5,-72.6,-118.0,-143.4,-155.0,-161.3,-165.2,-174.4,-178.7,-181.4])
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
plt.ylabel("相位差(°)", fontproperties="SimHei")
plt.legend()
plt.show()