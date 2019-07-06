"""
Merge Sort
归并排序
时间复杂度为O(n^2), 空间复杂度为O(n)
"""


def merge_sort(num, left, right):
    # 递归出口
    if left >= right:
        return

    # 递归
    mid = (left + right) // 2
    merge_sort(num, left, mid)
    merge_sort(num, mid + 1, right)

    p1 = left
    p2 = mid + 1
    temp_array = []

    # 合并算法
    while p1 <= mid and p2 <= right:
        if num[p1] <= num[p2]:
            temp_array.append(num[p1])
            p1 += 1
        else:
            temp_array.append(num[p2])
            p2 += 1

    while p1 <= mid:
        temp_array.append(num[p1])
        p1 += 1
    while p2 <= right:
        temp_array.append(num[p2])
        p2 += 1

    # 将temp_array覆盖到num的[left,right + 1)区间的值中
    num[left:right + 1] = temp_array


if __name__ == '__main__':
    num = [6, 5, 1, 2, 5, 4, 0]
    print(num)
    merge_sort(num, 0, len(num) - 1)
    print(num)
