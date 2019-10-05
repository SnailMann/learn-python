# coding=utf-8
"""
Bubbule Sort 冒泡算法
时间复杂度平均为O(n^2)
"""


def bubble_sort(num):
    for i in range(len(num) - 1):
        for j in range(len(num) - 1 - i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]


if __name__ == '__main__':
    num = [6, 5, 1, 2, 5, 4, 0]
    print(num)
    bubble_sort(num)
    print(num)
