# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None:
            if targetSum == root.val:
                return True
            else:
                return False 
        remaining = targetSum - root.val
        LEFTresult = self.hasPathSum (root.left,remaining)
        RIGHTresult = self.hasPathSum(root.right,remaining)

        return LEFTresult or RIGHTresult        