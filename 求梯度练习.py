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
# zeros()函数返回的是什么呢???它是pytorch的函数,返回的一般是张量,张量必然有其形和质,这里的形是2维,第一维是2个元素,第二维也是二个元素,2行2列,二维数组可以不定义行数,但是一定不能不定义列数,这就是说最后一个维度是必须定义的,既然这里定义了j.......返回值赋值,基本操作.....
j = torch.zeros(2, 2)
# k求导,k是x所构成的,k是x的函数
k.backward(torch.FloatTensor([1, 0]), retain_graph=True)

# x的梯度 tensor([4., 3.]),这说明什么问题呢???k是x的函数,k中有两个函数,,要确定这两个函数的值,k.backward是k对变量求导,但是实际上k由x决定,而x里面有两个元素,k的x求导,

# k对x求导,在这里面,我们需要明白,x是一个张量里面有两个值,不是单个元素,所以k对x求导这里就有文章了,k对x[0]求导是一个值,k对x[1]求导是另外一个值,共有两个值,这么来看最后值个数由变量来决定,k对x[0]求导是k[0]对x[0]求导与k[1]对x[0]求导的和,,,,得到值为(2x[0]+2,3+2x[1]),但是在k求导的时候,我们额外传入了一个张量,所以值是(2*1+2,3+2*0),就是(4,3)
print("x的梯度",x.grad)
print("x的梯度的数据",x.grad.data)





#k是x的函数,由x演化而来,这里用x的值(相关值)给j里面的元素赋值,那么这里,j是不是x的函数呢????是用x的grad的data去给j里面的元素赋值,但是在这里,如果把x看做是变量,那么为什么是x.grad,不是其他的呢???显然,根据函数层级划分,k是x的函数,k求导,并且保留计算图,是对x的求导,得到的导数表达式可能是一个与x有关的式子,但是x这里已经定义了值,那么x.grad就是一个有具体数值的张量,
j[0] = x.grad.data
# zero_()函数
x.grad.data.zero_() # 归零之前求得的梯度
k.backward(torch.FloatTensor([0, 1]))
j[1] = x.grad.data