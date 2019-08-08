class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BuildTreeByPreIn:
    def buildTree(self, pre, mid):
        if not pre or not mid or len(pre) != len(mid):
            return None

        root = TreeNode(pre[0])
        i = mid.index(root.val)
        if i >= 0:
            root.left = self.buildTree(pre[:i], mid[:i])
            root.right = self.buildTree(pre[i:], mid[i+1:])
        return root


if __name__ == '__main__':
    pre = [3, 9, 20, 15, 7]
    mid = [9, 3, 15, 20, 7]
    test = BuildTreeByPreIn()
    result = test.buildTree(pre, mid)
    print(result)
