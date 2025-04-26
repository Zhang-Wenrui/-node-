# -node-
see in readme
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

我的疑惑是，为什么dfs(node)乃至if not node中的node会被默认当做树中节点这样一个数据结构，毕竟treenode也没有定义node这么一个结构。如果我们把node改为list,student,tree或其他任意名称，计算机是不是就不认为他是树的节点了呢，答案是：No,也就是说无论你怎么改名，这都是树的节点这个数据结构，即计算机并不依靠node这个单词判定其数据结构。so，计算机认为node是树节点的原因其实是！！！！在inorderTraversal函数中，有一句dfs(root)，这使得dfs这个递归函数的第一个输入是已知的root！而root是声明过的树的根节点！也就是说，dfs()内的数据结构已经是“树的节点”的形状了！（并且以后都是！）
