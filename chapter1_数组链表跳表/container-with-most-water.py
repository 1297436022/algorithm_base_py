from typing import List  # 类型提示支持


def max_area(height: List[int]) -> int:
    i, j, res = 0, len(height) - 1, 0
    while i < j:
        if height[i] < height[j]:
            res = max(res, height[i] * (j - i))
            i += 1
        else:
            res = max(res, height[j] * (j - i))
            j -= 1
    return res


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))

# 优雅的三元运算
# res = height[i] < height[j] ? Math.max(res, (j - i) * height[i++]):Math.max(res, (j - i) * height[j--]);
