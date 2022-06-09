import torch


#构建第一个矩阵
a=torch.ones(2,2)

# 求均值
out=torch.mean(a)

# 均值是1

print(out)