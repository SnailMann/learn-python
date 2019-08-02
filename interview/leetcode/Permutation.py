class Permutation:
    """
    leetcode: Permutations
    题46 全排列
    给定一个没有重复数字的序列，返回其所有可能的全排列。

    输入: [1,2,3]
    输出:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
    """
    count = 0

    @staticmethod
    def permutation(nums, index=0):
        """
        1. index 代表从什么位置开始选元素，默认从数组的0索引开始
        2. 整个过程就是遍历从index到len - 1的元素
        3. 在0位置开始选元素时，如果总共有三个元素，所以就要遍历三次
        4. 每次遍历，都需要将index和i位置的元素交换，代表本次排列，第index位置放num数组的第i个元素
        5. 以交换后的顺序递归下去，递归完毕后，还要把位置交换回来，保证顺序的正确性
        6. 递归退出条件可以是index = len ，也可以是index = len - 1。如果减一，可以少递归几次，为什么呢？因为有5个元素，就相当于选择排序一样，一个位置选择一个元素，前4个位置选完，最后一个肯定也固定了
        """
        Permutation.count += 1
        if index == len(nums) - 1:
            print(nums)
            return

        for i in range(index, len(nums)):
            if i == index:
                Permutation.permutation(nums, index + 1)
            else:
                nums[i], nums[index] = nums[index], nums[i]
                Permutation.permutation(nums, index + 1)
                nums[i], nums[index] = nums[index], nums[i]


if __name__ == '__main__':
    Permutation.permutation(['a', 'b', 'c'])
    print(Permutation.count)
