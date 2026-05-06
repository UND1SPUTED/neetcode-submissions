# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {}
        for i in range(len(inorder)):
            idx_map[inorder[i]] = i
        
        self.pre_idx = 0

        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            idx = idx_map[root_val]
            root.left = helper(in_left, idx - 1)
            root.right = helper(idx + 1, in_right)
            return root

        return helper(0, len(inorder) - 1)