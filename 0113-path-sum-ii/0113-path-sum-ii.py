# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def help(root, targetSum, temp):
            if root is None:
                return

            targetSum -= root.val
            temp.append(root.val)

            # Check if it's a leaf and the sum matches
            if root.left is None and root.right is None and targetSum == 0:
                result.append(temp.copy())

            if root.left:
                help(root.left, targetSum, temp)

            if root.right:
                help(root.right, targetSum, temp)

            # Backtrack
            temp.pop()

        help(root, targetSum, [])
        return result

