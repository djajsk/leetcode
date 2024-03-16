/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int height(TreeNode* root){
        
        if(root == NULL){
return 0;}
        int left = height(root -> left);
        int right = height(root -> right);
        
        int res = max(left, right) + 1;
        
        return res;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        
        if(root == NULL){
            return 0;
        }
        
        int case1 = diameterOfBinaryTree(root -> left);
        int case2 = diameterOfBinaryTree(root -> right);
        int case3 = height(root -> left) + height(root -> right) ;
        
        int sol = max(case1 , max(case2,case3)) ;
        
        return sol;
    }
};