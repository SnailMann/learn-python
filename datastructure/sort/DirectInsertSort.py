# coding=utf-8
"""
Direct Insert Sort
直接插入排序
时间复杂度为O(n^2)
"""


def direct_insert_sort(num):
    for i in range(1, len(num)):
        pre_insert_num = num[i]  # 待插入数
        for j in range(i - 1, -1, -1):  # 等同于for(int j = i - 1; i >= 0; i++)
            if pre_insert_num < num[j]:
                num[j], num[j + 1] = num[j + 1], num[j]
            else:
                break


if __name__ == '__main__':
    num = [6, 5, 1, 2, 5, 4, 0]
    print(num)
    direct_insert_sort(num)
    print(num)
