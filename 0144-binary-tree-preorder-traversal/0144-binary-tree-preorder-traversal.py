# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre(self,ans,root):
        if root:
            ans.append(root.val)
            self.pre(ans,root.left)
            self.pre(ans,root.right)
        return ans
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        return self.pre(ans,root)