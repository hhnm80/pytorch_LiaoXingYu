# coding=utf-8
import torch
from torch.autograd import Variable
x = Variable(torch.FloatTensor([2, 3]), requires_grad=True)

# 先是定义了,k的形状和值,k的形状,zeros这个函数在很多地方都有,numpy里面有,matlab里面有,在numpy里面,zeros函数就是创建一个数组,这个数组的"质"已经规定了,就是里面的元素全为0 ,但是还没有"形",因此我们传入参数,一个或者两个或者三个参数,几个参数就是几维,这里传入一个2,就是1个维度,而且这个维度的元素个数是2,注意这个2不是数值,因为数值已经给你规定了,有几个维度还不够,还要知道每个维度有多少个数值,在这里,一个参数就是说明只有一个维度,这个维度的元素个数是2,值全为0,简单表示就是[0,0],在pytorch里面,函数的调用返回值一般都是tensor张量,没有数组的概念,torch.zeros(2)不好理解???zeros(2)好理解吧,一个函数,参数为2....
k = Variable(torch.zeros(2))
k[0] = x[0] ** 2 + 3 * x[1]
k[1] = x[1] ** 2 + 2 * x[0]
