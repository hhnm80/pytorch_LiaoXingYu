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
# mean函数是用来求数组(矩阵)里面元素的平均的,在这里就是(15+18)/2=16.5,但是输出是
out = c.mean()

# 虽然out的确是一个数值,但是在potorch里面,,,,,就算是数值也是和tensor相关的...
# tensor(16.5000, grad_fn=<MeanBackward0>)
print(out)
# torch.Size([])
print(out.shape)

# 通过输出发现,out是没有形状的,这说明out的确是一个值,,,,,

# 这是单个数值的向量,或者说是矩阵,
num=torch.Tensor([2])
print("num的值是:",num)
print(num.shape)



# 这里为什么没有参数呢?????out求导,,out是对什么求导呢?????out是c里面的元素求平均值所得,如果用数学表达式表示,就是(a+b+c)/n这种,如果元素个数为3,这里n=3,所以out最终是由c[0],c[1]....就是c里面所有的值共同决定的,,,,out.backward()里面没有参数,
out.backward()

print("input:")
# a的data是: tensor([2., 3.])
print("a的data是:",a.data)

print("output:")

# tensor(16.5000)
print(out.data)

# 16.5
print(out.data.item())

print("input gradients are" )
#tensor([1.5000, 1.5000])
# 准确来说,c是b的函数,b是a的函数,c是a的函数,但是out是out = c.mean(),也就是说out是由c中的元素来决定的,但是仔细想想,a是一个向量,c也是一个向量,c也是由a中单个元素来决定,那么out是不是a的元素呢???我们可以用手写公式推导,c[0,0]=3a[0,0]+9,c[0,1]=3a[0,1]+9,,,,,,,,于是c对a求导,得到的肯定是一个二维,首先是c[0,0]对a求导,是c[0,0]对a[0,0]和a[0,1]求导的和,,,,然后是c[0,1]
print(a.grad)