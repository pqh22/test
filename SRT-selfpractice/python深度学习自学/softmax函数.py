import numpy as np
def softmax(a):
    c=np.max(a)
    a=a-c
    exp_a=np.exp(a)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a
    return(y)#ok没问题
a=np.array([0,0,0])
x=softmax(a)
print(x)