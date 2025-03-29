//Preorder Traversal of Tree..

import java.util.ArrayList;
import java.util.List;
 public class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
         this.right = right;
      }
  }
 
class PreorderTraversal{
    public List<Integer> preorderTraversal(TreeNode root) {
        if (root==null){
            return new ArrayList<Integer>();
        }
        List<Integer> result=new ArrayList<Integer>();
        result.add(root.val);
        result.addAll(preorderTraversal(root.left));
        result.addAll(preorderTraversal(root.right));
        return result;
    }
    
    }
