def factorial1(x):
    result = x
    for i in range(1, x):
        result *= i
    return result


def factorial2(x):
    if x == 1:
        result = 1
    else:
        result = x * factorial2(x-1)
        # print(result)
    return result


print('循环实现阶乘的结果：' + str(factorial1(5)))
print('递归实现阶乘的结果：' + str(factorial2(5)))
