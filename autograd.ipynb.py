# 下面学习的是pytorch的自动求导的办法
# 自动求导是pytorch中非常重要的机制
import torch
from torch.autograd import Variable


# 百度requires_grad
x = Variable(torch.Tensor([2]), requires_grad=True)
# x可以理解为原始变量,假设x是输入层上的某个神经元xx的值
# y的值是x直接得到的,假设一个神经网络只有一个隐藏层,y是隐藏层里面的一个神经元yy,假设神经元yy只获得输入层xx的值,y由x演化而来,
y=x+2
# z由y演化而来,z是y的函数,y是x函数,这就是复合函数,符合函数求导是逐层进行的....
z = y ** 2 + 3
