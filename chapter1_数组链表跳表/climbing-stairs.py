
def climb_stairs(n):
    a = b = 1
    for _ in range(n):  # _ 占位符 表示不在意变量的值 只是用于循环遍历n次，无法打印变量值
        a, b = b, a + b
    return a

# 从第 00 级开始爬的，所以从第 0 级爬到第 0 级我们可以看作只有一种方案，即 f(0) = 1
# 从第 0 级到第 1 级也只有一种方案，即爬一级，f(1) = 1
# 转移方程：f(x)=f(x−1)+f(x−2)


def climb_stairs1(n):  # 滑动数组
    p, q, r = 0, 0, 1
    for _ in range(n):
        p = q
        q = r
        r = p + q
    return r


print(climb_stairs1(3))
