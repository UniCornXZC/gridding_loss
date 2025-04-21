# -*- coding: utf-8 -*-
# @Author: Haozhe Xie
# @Date:   2019-12-30 11:03:55
# @Last Modified by:   Haozhe Xie
# @Last Modified time: 2019-12-30 11:13:39
# @Email:  cshzxie@gmail.com

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
os.environ["TORCH_CUDA_ARCH_LIST"] = "5.0;6.0;6.1;6.2;7.0;7.5;8.0;8.7;9.0"
setup(name='gridding_distance',
      version='1.0.0',
      ext_modules=[
          CUDAExtension('gridding_distance', ['gridding_distance_cuda.cpp', 'gridding_distance.cu']),
      ],
      cmdclass={'build_ext': BuildExtension})
