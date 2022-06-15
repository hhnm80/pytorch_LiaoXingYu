# coding=utf-8
import torch
from torch.autograd import Variable


# 将张量转换为Variable
a=Variable(torch.FloatTensor([2,3]),requires_grad=True)

# a是一个Variable变量,或者说一个套了壳子的张量,
b =a+3
# tensor([5., 6.], grad_fn=<AddBackward0>)
print(b)

c=b*3
# tensor([15., 18.], grad_fn=<MulBackward0>)
print(c)



#tensor(16.5000, grad_fn=<MeanBackward0>)
# mean函数是用来求数组(矩阵)里面元素的平均的,在这里就是(15+18)/2=16.5
out = c.mean()
print(out)


# 这里为什么没有参数呢?????out求导,,out是对什么求导呢?????out是c里面的元素求平均值所得,如果用数学表达式表示,就是(a+b+c)/n这种,如果元素个数为3,这里n=3,所以out最终是由c[0],c[1]....就是c里面所有的值共同决定的,,,,
out.backward()