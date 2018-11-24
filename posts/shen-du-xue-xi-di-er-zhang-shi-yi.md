
最近在阅读《深度学习》这本书。可能限于篇幅，有很多结论作者没有详细说明。所以在博客记录一下我对这些结论的推导。
<!-- TEASER_END -->


**原文2.7节** 实对称矩阵的特征分解也可以用于优化二次方程 $f(x) = x^TAx$，其中 限制 $\|x \|^2 = 1$。当 x 等于 A 的某个特征向量时，f 将返回对应的特征值。在限制条 件下，函数 f 的最大值是最大特征值，最小值是最小特征值。

**证明**

首先把问题表示成标准形式:
$$\min(\max)\quad f(x)=x^TAx$$
$$s.t.\quad\|x\|^2-1=0$$

用拉格朗日乘子法:

注意到$\|x\|^2=1$ 等价于 $x^Tx=1$ 拉格朗日函数为:
$$l(x,\lambda) = f(x)-\lambda (x^Tx-1)$$

上式对$x$求导，注意$A$是一个对称矩阵,得到:

\begin{equation}
\begin{split} 
\frac{\delta l}{\delta x}&=Ax+A^Tx-2\lambda x\\\\
\quad&=2(A-\lambda\cdot I)x\\\\
\end{split}
\end{equation}

令导数为0，得到:
$$(A-\lambda\cdot I)x=0$$

观察这个等式的结构可以发现这就是矩阵的特征值和特征向量的求解公式，因此$\lambda$就等于特征值，$x$是特征向量单位化的值。回顾特征值和特征向量满足$Ax=\lambda x$，注意到$x^Tx=1$,因此:
$$f(x)=x^TAx=x\cdot\lambda x=\lambda x^Tx = \lambda$$

因此，和2.7节的结论一致，$f(x)$的最大值是最大的特征值，最小值是最小的特征值，此时$x$是对应特征值的特征向量。

----

**原文2.8节** 我们可以用与 A 相关的特征分解去解释$A$的奇异值分解。$A$的左奇异向量（left singular vector）是 $AA^T$ 的特征向量。$A$的右奇异向量（right singular vector）是$A^TA$的特征向量。$A$的非零奇异值是$A^TA$特征值的平方根，同时也是$AA^T$特征值的平方根。

**证明**

我们知道如果A为方阵，它的特征值$\lambda$和特征向量$x$满足
$$Ax = \lambda x$$
如果A是一个$m\times n$维的矩阵，$v$ 是一个n维向量，$u$是一个m维向量,它的奇异值分解满足:
$$Av=\lambda u$$
$$A^Tu = \lambda v$$
奇异值分解的求解方法是:

$$Av=\lambda u$$
则:
$$A^TAv=\lambda A^Tu = \lambda ^2 v$$
上式表明，$v$ 是$A^TA$的特征向量，同理$u$ 是$AA^T$的特征向量,和上文的描述一致。

这个结论的一个用处是帮助理解PCA和SVD之间的关系

给定一个中心化(即均值为0)的数据矩阵$X_{n\times m}$，其中$n$是数据的数目，$m$是数据的维度，PCA 首先求数据的协方差矩阵，然后对协方差矩阵进行特征分解，然后按特征值由大到小进行选择。形式化来说，由于$X$已经进行过中心化，因此$X$的协方差矩阵可以表示为$\frac{1}{n-1}X^TX$,然后PCA对矩阵$\frac{1}{n}X^TX$进行特征分解。

上文已经证明过$X^TX$的特征值就是$X$的右奇异向量,因此PCA得到的特征向量就是$X$的右奇异向量。而对于特征向量，注意到协方差矩阵前面有一个$\frac{1}{n-1}$,因此PCA特征值的$n-1$倍等于SVD特征值的平方。

我们可以用下面的代码来验证上述关系。


```python
import numpy as np
# 得到一个4*4 的矩阵
X = np.random.randn(4,4)
# 中心化
X -= X.mean(axis=1)[:,np.newaxis]
# PCA
np.random.seed(41)
def pca(X):
    n = X.shape[0]
    Y = 1/(n-1)*np.dot(X.T,X)
    # 特征值和特征向量
    eigen_val,eigen_vec = np.linalg.eig(Y)
    # 按从大到小排序
    order = np.argsort(eigen_val)[::-1]
    
    return eigen_val[order],eigen_vec[order]
def svd(X):
    # SVD 返回的是U\sigmaV^T,我们不需要U
    return np.linalg.svd(X)[1:]
pca_val,pca_vec = pca(X)
svd_val,svd_vec = svd(X)
print("PCA 特征值的n-1倍是:",3*pca_val)
print("SVD 特征值的二次方是:",svd_val**2)
```

    PCA 特征值的n-1倍是: [  8.30037519e+00   1.92882619e+00   3.63183940e-02  -2.22306907e-16]
    SVD 特征值的二次方是: [  8.30037519e+00   1.92882619e+00   3.63183940e-02   1.88715574e-33]


----
**原文2.9节** Moore-Penrose 伪逆的补充

给定一个矩阵$A_{n\times m}$，A的 Moore-Penrose 伪逆定义为$A^*=(A^TA)^{-1}A^T$

伪逆有以下特性:
1. $A^*A = (A^TA)^{-1}A^TA=I$，这也是$A*$被称作伪逆的原因
2. $A^*A$ 是一个投影矩阵,OLS $Ax=b$的一种解释是找到距离A的值域中距离b最近的投影，这里采用的投影矩阵就是$A^*A$


----
**原文2.12节** $argmax_d{Tr(d^TX^TXd)}$ subject to $d^Td=1$ 这个优化问题可以通过特征分解来求解。最优的$d$就是$X^TX$最大的特征值对应的特征向量

**证明**

注意到$d^TX^TXd$ 是一个标量,因此$Tr(d^TX^TXd)$ 的迹运算可以去掉，设$A=X^TX$，注意到A是一个对称矩阵，那么原问题变为:
$$\mathop{\arg\max}_d\ d^TAd$$
$$s.t.\quad d^Td=1$$
这个问题就变为上文2.7节中讨论的问题，目标函数的最大值就是矩阵$A=X^TX$的最大特征值，而$d$是最大特征值对应的特征向量的单位化。

