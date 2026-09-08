# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return 0
            leftheight = height(root.left)
            if leftheight == -2:
                return -2
            rightheight = height(root.right)
            if rightheight == -2:
                return -2
            if abs(leftheight - rightheight)>1:
                return -2
            return 1 + max(leftheight, rightheight)
        return height(root)!=-2
        