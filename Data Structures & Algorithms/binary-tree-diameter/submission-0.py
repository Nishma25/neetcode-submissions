# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        # left_height = self.maxHeight(root.left)
        # right_height = self.maxHeight(root.right)
        # diameter  = left_height + right_height

        # sub = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))

        # return max(diameter,sub)

        # def maxHeight(self, root: Optional[TreeNode])-> int:
        #     if not root:
        #         return 0
            
        # return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))


        def dfs(root):
            if not root:
                return 0,0
            
            left_height, left_diameter = dfs(root.left)
            right_height, right_diameter = dfs(root.right)

            height = 1+ max(left_height, right_height)

            diameter = max(right_height+left_height, right_diameter, left_diameter)

            return height, diameter
        _, diameter = dfs(root)
        return diameter