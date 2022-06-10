# coding=utf-8
import torch
from torch.autograd import Variable
x = Variable(torch.FloatTensor([3]), requires_grad=True)
y = x * 2 + x ** 2 + 3
print(y)
print(y.shape)
print(y.size())
# y求导???y对x求导???y是x的函数,求导得到的是x的一个表达式,但是在开始就给x赋予了一个值3,

# y.backward就是对y中所有的自变量进行了求导,但是在这里,y只有x这一个变量,所以,这里就是对x求导,如果是多元函数,比如y=x+z,这样y.backward就是同时对x和z求导这里就是偏导,求导以后计算图就被破坏了,如果y=2z+x,z=3x,这样由于z和x有关联,所以最终化成了x的函数,所以y最终还是x的函数,如果z和x是独立没有关联的,这样y就是z和x的函数,二元函数....
y.backward(retain_graph=True) # 设置 retain_graph 为 True 来保留计算图
# 输出值是8,
print(x.grad)
# 由于上面增加了retain_graph=True这个参数,就是保留计算图,

y.backward() # 再做一次自动求导，这次不保留计算图
print(x.grad)
# 可以发现 x 的梯度变成了 16，因为这里做了两次自动求导，所以讲第一次的梯度 8 和第二次的梯度 8 加起来得到了 16 的结果。,,,,但是这又是什么原理呢????