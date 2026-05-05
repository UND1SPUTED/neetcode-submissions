# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(a, b):
            stack = [(a, b)]

            while stack:
                x, y = stack.pop()

                if not x and not y:
                    continue
                
                if not x or not y or x.val != y.val:
                    return False

                stack.append((x.left, y.left))
                stack.append((x.right, y.right))
            return True

            
        stack = [root]

        while stack:
                node = stack.pop()

                if node:
                    if node.val == subRoot.val and isSameTree(node, subRoot):
                        return True
                    stack.append(node.left)
                    stack.append(node.right)
        return False
        