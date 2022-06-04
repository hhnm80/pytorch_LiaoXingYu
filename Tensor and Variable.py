# 把pytorch当做numpy来使用,pytorch的官方介绍是一个拥有强力GPU加速的张量和动态构建网络的库，其主要构件是张量，所以我们可以把 PyTorch 当做 NumPy 来用，PyTorch 的很多操作好 NumPy 都是类似的，但是因为其能够在 GPU 上运行，所以有着比 NumPy 快很多倍的速度。

import torch
import numpy as np

# 创建一个numpy数组, 一个10行20列的数组,里面的每个数都是符合标准正太分布数字,或者说10个一维向量,每个一维向量里面有20个元素

numpy_tensor=np.random.randn(10,20)
print(numpy_tensor)

# 我们可以使用下面两种方式将numpy的ndarray转换到tensor上,下面用两种方法将多维数组转化为张量
# Tensor函数就是根据传入的数据创建张量,
pytorch_tensor1 = torch.Tensor(numpy_tensor)
pytorch_tensor2 = torch.from_numpy(numpy_tensor)


# 当然,也可以把张量转换为numpy数组,相当于上面的逆运算
# 如果 pytorch tensor 在 cpu 上
numpy_array = pytorch_tensor1.numpy()

# 如果 pytorch tensor 在 gpu 上
numpy_array = pytorch_tensor1.cpu().numpy()

# 需要注意 GPU 上的 Tensor 不能直接转换为 NumPy ndarray，需要使用`.cpu()`先将 GPU 上的 Tensor 转到 CPU 上

# PyTorch Tensor 使用 GPU 加速
#
# 我们可以使用以下两种方式将 Tensor 放到 GPU 上
# 第一种方式是定义 cuda 数据类型
dtype = torch.cuda.FloatTensor # 定义默认 GPU 的 数据类型
gpu_tensor = torch.randn(10, 20).type(dtype)

# 第二种方式更简单，推荐使用
gpu_tensor = torch.randn(10, 20).cuda(0) # 将 tensor 放到第一个 GPU 上

# 其实就是放到第二块显卡上面,但是在我电脑上只有一块显卡,所以,这一句不能使用
# gpu_tensor = torch.randn(10, 20).cuda(1) # 将 tensor 放到第二个 GPU 上
# 而将 tensor 放回 CPU 的操作非常简单
cpu_tensor = gpu_tensor.cpu()

# 我们也能够访问到 Tensor 的一些属性
# 可以通过下面两种方式得到 tensor 的大小
print(pytorch_tensor1.shape)
print(pytorch_tensor1.size())
