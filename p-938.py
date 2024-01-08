class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            current_val = 0
            if not node:
                return 0
            if low <= node.val:
                    if node.val<= high:
                        current_val = node.val
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            return current_val + left_sum + right_sum
        return dfs(root)
