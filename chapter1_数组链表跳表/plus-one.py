


def plus_one1(digits):
    for i in range(len(digits) - 1, -1, -1): # 倒序要加 -1
        digits[i] = digits[i] + 1
        digits[i] = digits[i] % 10 #
        if digits[i] != 0:
            return digits
    digits[1:] = digits[:] #
    digits[0] = 1
    return digits


def plus_one(digits):
    num = 0
    for i in range(len(digits)):
        num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]


print(plus_one1([1,2,3]))