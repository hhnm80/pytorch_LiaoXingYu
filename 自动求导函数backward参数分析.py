# coding=utf-8
import torch
from torch.autograd import Variable


x = torch.tensor([0.0, 2.0, 8.0], requires_grad=True)
y = torch.tensor([5.0, 1.0, 7.0], requires_grad=True)
z = x * y+5*x+5*y

z.backward(torch.FloatTensor([0, 0, 2]))
# 因为在上面定义x和y的时候,已经设置了true,而x和y是相互独立的,z是x和y的函数,是二元函数,z对x求导,是与y相关的一个值,y是三维向量,所以求导结果就是3维向量,z对x的导数(偏导)是y+5,因为y的值是[5.0, 1.0, 7.0],所以y+5是[10,6,12],在backward里面提供的参数[0,0,2],就是三维向量三个值的倍率化,就是倍数化,所以最后的值x.grad是[10*0,6*0,12*2],就是[0,0,24].......

print(x.grad)

# 这只是一个最简单的例子,因为z是x和y的函数,但是x*y是什么意思呢???这里的*号显然是对应位置的元素相乘,并不是矩阵相乘,因为

print("x乘以y的值是:",x*y)