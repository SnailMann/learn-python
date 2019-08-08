import math


class MinCostClimbingStairs:
    """
    leetcode 746 : Min Cost Climbing Stairs | 使用最小花费爬楼梯

    爬n阶的楼梯，可以一次爬1阶，也可以爬2阶
    每一阶都有自己需要消耗的体力值，当你爬到楼顶时，你使用花费最少体力的爬法，最后需要花费多少体力？
    """

    @staticmethod
    def minCostClimbingStairs(cost):
        """
        其实如果我们看透了，其实会发现它跟斐波那契的求法一模一样
        思路分析：
        到达低i阶楼梯有两种情况，第一种是由第i - 2阶楼梯跨两步直接到达第i阶，第二种是有第i - 1阶楼梯跨一步
        到达第i阶楼梯。所以最后走完所有楼梯，可以由第costSize - 2阶跨两步到达顶端，也可以由第costSize - 1阶跨一步到达顶端。取两者的较小代价即可。
        所以要想到第n阶，那么它的最小代价爬法就是f(n) = min(f(n -1),f(n-2)) + curCost。而斐波那契的通式是f(n) = f(n-1) + f(n-2)。所以只要理解出这一点，就ok了
        :param cost:
        :return:
        """
        if cost is None or len(cost) == 0:
            return 0
        if len(cost) == 1:
            return 0
        if len(cost) == 2:
            return cost[0] if cost[0] < cost[1] else cost[1]

        a = cost[0]
        b = cost[1]
        # f(n) = min(f(n -1),f(n-2)) + curCost
        for i in range(2, len(cost)):
            # 求出跳到当前n阶，所需要的最小代价，a其实就是f(n-2), b就是f(n-1)
            c = min(a, b) + cost[i]
            # 推断更新，为了求下一阶的最小代价，做准备
            a = b
            b = c

        # 最后的比较，是n-2阶时跨两阶到楼顶，和n-1阶跨一阶到楼顶，楼顶没有cost，所以这里不需要加上cost
        return min(a, b)

    @staticmethod
    def methoh1(cost):
        p1, p2 = 0, 0
        for i in range(2, len(cost) + 1):
            p1 = p2
            p2 = min(p2 + cost[i - 1], p1 + cost[i - 2])
        return p2


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    result = MinCostClimbingStairs.minCostClimbingStairs(cost)
    print(result)
