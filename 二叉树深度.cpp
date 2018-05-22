// 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/

class Solution {
public:
    int Max(int a, int b){
        if(a > b){
            return a;
        }
        else return b;
    }
    
    int TreeDepth(TreeNode* pRoot)
    {
        if(pRoot == 0){
            return 0;
        }
        int leftDepth = TreeDepth(pRoot -> left);
        int rightDepth = TreeDepth(pRoot -> right);
        return 1 + Max(leftDepth, rightDepth);
    }
};

