# 把pytorch当做numpy来使用,pytorch的官方介绍是一个拥有强力GPU加速的张量和动态构建网络的库，其主要构件是张量，所以我们可以把 PyTorch 当做 NumPy 来用，PyTorch 的很多操作好 NumPy 都是类似的，但是因为其能够在 GPU 上运行，所以有着比 NumPy 快很多倍的速度。

import torch
import numpy as np

# 创建一个numpy数组, 一个10行20列的数组,里面的每个数都是符合标准正太分布数字,或者说10个一维向量,每个一维向量里面有20个元素

numpy_tensor=np.random.randn(10,20)
print(numpy_tensor)

# 我们可以使用下面两种方式将numpy的ndarray转换到tensor上,下面用两种方法将多维数组转化为张量
# Tensor函数就是根据
pytorch_tensor1 = torch.Tensor(numpy_tensor)
pytorch_tensor2 = torch.from_numpy(numpy_tensor)