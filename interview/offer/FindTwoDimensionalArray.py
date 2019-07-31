class FindTwoDimensionalArray():
    """
    剑指Offer:面试题4 | 二维数组中的查找
    在一个二维数组中，每一行都按照从左到右递增的顺序，每一列都按照从上到下递增的顺序。请完成一个函数
    输入一个符合条件的二维数组，和一个目标值，判断数组中是否含有该整数
    """

    @staticmethod
    def find(matrix, target):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # 真实行列数据
        row = len(matrix)  # 矩阵有多少行
        colum = len(matrix[0])  # 矩阵有多少列

        # 行列的索引，默认从矩阵最右上角开始比较
        curRow = 0
        curCol = colum - 1

        while curRow <= row - 1 and curCol >= 0:
            if target == matrix[curRow][curCol]:
                print(curRow, curCol)
                return True
            # 如果跟矩阵最右上角的数据相比要小，那么你就要往矩阵的左边找，大既要往矩阵的下边找
            elif target < matrix[curRow][curCol]:
                curCol -= 1
            else:
                curRow += 1

        return False



if __name__ == '__main__':
    matrix = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15]
    ]
    result = FindTwoDimensionalArray.find(matrix, 4)
    print(result)
