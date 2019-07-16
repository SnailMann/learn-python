
"""
方法一：
1. 只用用于统计处理无符号的二进制，既只能处理正数，无法处理负数
"""
def method_1(num):
    count = 0
    while (num):
        if (num & 1):
            count += 1
        num = num >> 1
    print(count)


if __name__ == '__main__':
    method_1(-10)
