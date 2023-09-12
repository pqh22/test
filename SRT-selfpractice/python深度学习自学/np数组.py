import numpy as np
a=np.array([[1,1],[1,1]])
b=np.array([[1,1],[1,1]])
#c=np.dot(a,b) 矩阵乘法
#c=a@b # @符号代表矩阵乘法
# np.multiply是将相同的数组或者矩阵的对应元素相乘 类似于k积
#c=np.multiply(a,b)
c=np.cross(a,b)
#np.cross代表外积，虽然还不是很明白矩阵之间的外积是什么玩意
print(c.shape)
print(c)
#一维数组课题理解为向量
#二维数组代表二阶张量，就是相当于矩阵
#三维数组代表三阶张量，三阶及以上就比较抽象