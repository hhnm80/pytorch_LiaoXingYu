# coding=utf-8
import torch
from torch.autograd import Variable
x = Variable(torch.FloatTensor([2, 3]), requires_grad=True)

# 先是定义了,k的形状和值,k的形状,zeros这个函数在很多地方都有,numpy里面有,matlab里面有,在numpy里面,zeros函数就是创建一个数组,这个数组的"质"已经规定了,就是里面的元素全为0 ,但是还没有"形",因此我们传入参数,一个或者两个或者三个参数,几个参数就是几维,这里传入一个2,就是1个维度,而且这个维度的元素个数是2,注意这个2不是数值,因为数值已经给你规定了,有几个维度还不够,还要知道每个维度有多少个数值,在这里,一个参数就是说明只有一个维度,这个维度的元素个数是2,值全为0,简单表示就是[0,0],在pytorch里面,函数的调用返回值一般都是tensor张量,没有数组的概念,torch.zeros(2)不好理解???zeros(2)好理解吧,一个函数,参数为2....
k = Variable(torch.zeros(2))

# 显然定义了k为全0矩阵,或者说全0张量还不够,我们要重新对k里面的每个元素赋值,k里面的值由x里面的值决定,x手机一个矩阵,把x当做一个自变量....
k[0] = x[0] ** 2 + 3 * x[1]
k[1] = x[1] ** 2 + 2 * x[0]

print(k)
# zeros()函数返回的是什么呢???它是pytorch的函数,返回的一般是张量,张量必然有其形和质,这里的形是2维,第一维是2个元素,第二维也是二个元素,2行2列,二维数组可以不定义行数,但是一定不能不定义列数,
j = torch.zeros(2, 2)
k.backward(torch.FloatTensor([1, 0]), retain_graph=True)
j[0] = x.grad.data
x.grad.data.zero_() # 归零之前求得的梯度
k.backward(torch.FloatTensor([0, 1]))
j[1] = x.grad.data