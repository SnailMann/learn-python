"""
Quick Sort
快速排序
时间复杂度为O(nlogn),空间复杂度为O(1)
"""


def quick_sort(num, left, right):
    if left >= right:
        return

    p1 = left
    p2 = right
    base_num = num[left]

    while p2 > p1:
        while p2 > p1 and num[p2] >= base_num:
            p2 -= 1
        num[p1] = num[p2]
        while p2 > p1 and num[p1] <= base_num:
            p1 += 1
        num[p2] = num[p1]
    num[p1] = base_num

    quick_sort(num, left, p1 - 1)
    quick_sort(num, p1 + 1, right)


if __name__ == '__main__':
    num = [6, 5, 1, 2, 5, 4, 0]
    print(num)
    quick_sort(num, 0, len(num) - 1)
    print(num)
