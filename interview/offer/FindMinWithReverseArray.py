class FindMinWithReverseArray:
    """
    剑指Offer: 面试题9 | 旋转数组的最小数字
    把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转。输出该旋转数组的最小元素
    例如，数组{3,4,5,1,2}是数组{1,2,3,4,5}的一个旋转，该数组的最小值是1
    """

    @staticmethod
    def findMin(array):
        if array is None or 0 == len(array):
            return
        begin, first, end = 0, 0, len(array) - 1
        while begin + 1 < end:
            mid = (begin + end) // 2
            if array[mid] >= array[begin]:
                begin = mid
            else:
                end = mid

        return array[first] if array[end] > array[first] else array[end]


if __name__ == '__main__':
    array = [3, 4, 5, 1, 2]
    array1 = [3, 4, 5, 6, 7, 8, 9, -3, -2, -1]
    array2 = [1, 2, 3, 4, 5]
    result = FindMinWithReverseArray.findMin(array2)
    print(result)
