r, c = map(int, input().split())

if max(abs(r - 8), abs(c - 8)) % 2:
    print("black")
else:
    print("white")


# 求的是该点到中心点（8，8）的切比雪夫距离，距离为奇数则为黑色，为偶数则为白色。

# 切比雪夫距离（Chebyshev Distance），也称为无限范数距离或 L∞ 距离
# 是向量空间中两个点之间的距离度量方式之一。它定义为两个点在各个维度上坐标数值差的最大值。
# 切比雪夫距离在图像处理、模式识别、机器学习等领域都有广泛的应用，
# 尤其是在处理棋盘距离问题（如在一个格子棋盘中两个点的最短距离）时常被使用。
