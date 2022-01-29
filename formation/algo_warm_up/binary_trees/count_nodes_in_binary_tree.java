// https://leetcode.com/problems/count-complete-tree-nodes/
class Solution {
    public int countNodes(TreeNode root) {
        if (root != null)
            return 1 + countNodes(root.left) + countNodes(root.right);
        else
            return 0;
        
    }
}
