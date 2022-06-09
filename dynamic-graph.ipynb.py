# pytorch
import torch
# first_counter = torch.Tensor([0,1,2,3])

first_counter = torch.Tensor([0])

second_counter = torch.Tensor([10])

# 这是什么意思呢???为什么张量之间可以比较大小呢,然后后面又出现了一个方括号括起来的东西,这到底是下标还是列表呢???来调试一下程序,

# 输出的是一个张量,值是tensor([True]),这说明结果还是一个张量,这个张量中只有一个元素,元素的个数取决于被比较的两个张量里面的元素的个数,如果参与比较的两个张量元素个数不一样,比如一个是2个元素的一维张量,一个是4个元素的一维张量,比较出来的结果可能有点奇怪,因此,一般参与比较的两个张量的元素个数都一样,在这里,两个相比较的张量都是只有一个元素,因此(first_counter < second_counter)是只有一个元素的张量,在这里是[True],variable1=(first_counter < second_counter)[0]代表张量的第一个元素,在这里本来是一个值,一个bool值,就是这里的true,但是,在编译器里面variable1=(first_counter < second_counter)[0]被当做一个张量,但是这个张量没有维度,想想都明白,本来是一个数,被当做张量,就算是张量,也没有维度,名不副实而已>>>>
print("经过比较",first_counter < second_counter)
# a=10

variable1=(first_counter < second_counter)[0]
print(variable1.shape)


#
print("第一个元素???",variable1)

# 循环执行了10次????为什么循环执行了10次呢???因为每次循环,first_counter和second_counter的值都在更新,(first_counter < second_counter)获得的是一个张量,这个张量里面的元素全是bool型,元素的个数取决于参与比较的两个张量每个张量里面的元素个数,假设

# 改成while (first_counter < second_counter)效果一样,因为这里(first_counter < second_counter)只有一个元素,所以可以这么改
# 第一次循环的时候,first_counter值是[0],second_counter值是[10],显然第一次是true,循环中会改变first_counter和second_counter这两个张量的值,第一次循环结束后,first_counter值是[2],而second_counter值是[11],虽然最开始first_counter里面的值比second_counter小,但是架不住first_counter的增量大,这样,循环几次后first_counter和second_counter值相等的时候,循环结束
while (first_counter < second_counter)[0]:
    first_counter += 2
    second_counter += 1

#tensor([20.])
print(first_counter)
print(first_counter.shape)

#tensor([20.])

print(second_counter)
print(second_counter.shape)
