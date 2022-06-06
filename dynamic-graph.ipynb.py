# pytorch
import torch
# first_counter = torch.Tensor([0,1,2,3])

first_counter = torch.Tensor([0])

second_counter = torch.Tensor([10])

# 这是什么意思呢???为什么张量之间可以比较大小呢,然后后面又出现了一个方括号括起来的东西,这到底是下标还是列表呢???来调试一下程序,

# 输出的是一个张量,值是tensor([True]),这说明结果还是一个张量,这个张量中只有一个元素,元素的个数
print("经过比较",first_counter < second_counter)
# a=10

variable1=(first_counter < second_counter)[0]
print(variable1.shape)


#
print("第一个元素???",variable1)

while (first_counter < second_counter)[0]:
    first_counter += 2
    second_counter += 1

#tensor([20.])
print(first_counter)
print(first_counter.shape)

#tensor([20.])

print(second_counter)
print(second_counter.shape)
