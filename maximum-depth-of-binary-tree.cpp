/*
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
*/

//我的思路8ms,872k
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxNum(int x, int y){
        if(x >= y)
            return x;
        else 
            return y;
    }
    
    int maxDepth(TreeNode *root) {
        if(root==NULL){
            return 0;
        }
        int leftDepth = maxDepth(root -> left);
        int rightDepth = maxDepth(root -> right);
        return maxNum(leftDepth, rightDepth) + 1;
    }
};

//路人思路<1ms,8816k

class Solution {
public:
    int maxDepth(TreeNode *root) {
        if(root==NULL) return 0;
        int left = maxDepth(root->left);
        int right = maxDepth(root->right);
        return max(left,right)+1;
    }
};


