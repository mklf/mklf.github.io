<!-- 
.. title: 本周阅读 2017年06月23日
.. slug: ben-zhou-yue-du-2017nian-06yue-23ri
.. date: 2017-06-23 10:11:05 UTC+08:00
.. tags: 阅读清单
.. category: 
.. link: 
.. description: 
.. type: text
-->

##[1.Unified Memory for CUDA Beginners](https://devblogs.nvidia.com/parallelforall/unified-memory-cuda-beginners/)
一个简单的程序：用 Unified Memory 创建两个向量，在 CPU 上进行初始化，然后用 GPU kernel 计算向量加法。作者发现在 Kepler 架构的 K80 上，向量加法的 kernel 带宽能达到 134GB/s，而在 Pascal 架构的 Tesla P100 上却只有 6GB/s。这是什么原因造成的呢？

在 Pascal 架构以前， Unified Memory 在创建时会在 GPU 中分配显存，设置好页表等初始化操作。当 CPU 代码访问这片显存时，显卡驱动会把显存中的内容拷贝到内存中 (会有CPU页错误)。此后如果 GPU 又需要访问这片内存，驱动会先把**整块内存**拷贝到GPU，然后再启动kernel。也就是说内存拷贝的时间是不计入kernel 运行时间的。

Pascal 架构的 GPU 增加了硬件以提供对 Unified Memory 的支持。在调用`cudaMallocManaged() `时并不会真正在显存中分配内存。内存真正的分配被延迟到CPU 或者GPU 访问它的时候。由于支持页错误和页的移动(migration)，Pascal GPU 的kernel在访问一个内存中的 Unified Memory 时不需要提前把内存中的数据拷贝到显存中，而是在 kernel 中访问内存时才按页拷贝(当然会有数据预取减少页错误)。这种内存访问方式对于只利用部分内存的应用，比如对稀疏矩阵的某些操作，只需要在内存和显存间传输需要读写的部分数据。
<!-- TEASER_END -->

如何提高 Pascal GPU 上的带宽:

1. 直接在 GPU 上 初始化内存
2. 利用`cudaMemPrefetchAsync` 在CPU 初始化完成后将数据显式的传输 显存中。

-------







