# 下面学习的是pytorch的自动求导的办法
# 自动求导是pytorch中非常重要的机制
import torch
from torch.autograd import Variable


# 百度requires_grad
x = Variable(torch.Tensor([2]), requires_grad=True)
# x可以理解为原始变量,假设x是输入层上的某个神经元xx的值
# y的值是x直接得到的,假设一个神经网络只有一个隐藏层,y是隐藏层里面的一个神经元yy,假设神经元yy只获得输入层xx的值,y由x演化而来,
y=x+2
# z由y演化而来,z是y的函数,y是x函数,这就是复合函数,复合函数求导是逐层进行的....y的2次方加3
z = y ** 2 + 3
print(z)

# 使用自动求导 自动求导函数,z到底是不是函数呢?????
# z求导,z对什么求导呢??????
# 这句程序导致进程无法终止,难道这是一个死循环么?????死循环么???????? backward函数是反向求导数????
# z.backward()
#
#
# print("z求导的值是:",z.backward())
# #
# #输出tensor([8.])
# # 为什么x的grad是8呢,为什么呢?????????其实z是y的函数,y是x的函数,y是x的函数理解为:y是以x为自变量的函数,z=(x+2)**2+3,如果z对x求导,就是2(x+2),而x的值是2,所以求导结果是8,最后x.grad就是z对x求导的值,
print(x.grad)
# 构建三个二维张量，张量的两大要素，形状和数值，
x = Variable(torch.randn(10, 20), requires_grad=True)
y = Variable(torch.randn(10, 5), requires_grad=True)
w = Variable(torch.randn(20, 5), requires_grad=True)

# 三个二维张量，或者说二维数组，或者说二维矩阵，

# 实现一样功能的函数,在不同的模块里面,名字可能不一样,这个句子的作用是::::::::matmul是矩阵相乘的函数,先让x和w这两个矩阵相乘,然后让y矩阵减去相乘后的矩阵,矩阵相减形状必须一样,显然这里相减的矩阵形状是一样的.....out是一个复合函数
out=torch.mean(y-torch.matmul(x,w))

out.backward()

# 得到 x 的梯度
print("x的梯度是",x.grad)
# 得到 y 的的梯度
print("y的梯度是",y.grad)

# 得到 w 的梯度
print("w的梯度是",w.grad)

# 上面数学公式就更加复杂，矩阵乘法之后对两个矩阵对应元素相乘，然后所有元素求平均，有兴趣的同学可以手动去计算一下梯度，使用 PyTorch 的自动求导，我们能够非常容易得到 x, y 和 w 的导数，因为深度学习中充满大量的矩阵运算，所以我们没有办法手动去求这些导数，有了自动求导能够非常方便地解决网络更新的问题。