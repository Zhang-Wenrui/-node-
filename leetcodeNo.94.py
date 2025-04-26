# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # 节点的值
        self.left = left      # 左孩子节点
        self.right = right    # 右孩子节点

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []              # 用来保存中序遍历结果

        def dfs(node):        # 定义一个递归函数 dfs
            if not node:      # 递归终止条件：当前节点是空的
                return
            dfs(node.left)    # 1. 递归遍历左子树
            res.append(node.val)  # 2. 访问当前节点（加入到结果列表）
            dfs(node.right)   # 3. 递归遍历右子树
        
        dfs(root)             # 从根节点开始递归
        return res            # 返回结果列表
