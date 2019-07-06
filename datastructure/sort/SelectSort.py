"""
Select Sort
选择排序
时间复杂度为O(n^2)
"""


def select_sort(num):
    for i in range(len(num) - 1):
        min = i
        for j in range(i + 1, len(num)):
            min = j if num[j] < num[min] else min
        if min != i:
            num[min], num[i] = num[i], num[min]


if __name__ == '__main__':
    num = [6, 5, 1, 2, 5, 4, 0]
    print(num)
    select_sort(num)
    print(num)
