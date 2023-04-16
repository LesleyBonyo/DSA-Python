# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        heightDif = 0
        if root == None:
            return True
        # if root != None:

        heightDif = abs(self.height(root.left) - self.height(root.right))
        if heightDif > 1:
            return False
        checkLeft = self.isBalanced(root.left)
        checkRight = self.isBalanced(root.right)
        if checkLeft == True and checkRight == True and heightDif <= 1:
            return True

    def height(self, root):
        if root == None:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        return max(leftHeight, rightHeight) + 1
