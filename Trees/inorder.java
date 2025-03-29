import java.util.ArrayList;
import java.util.List;
  public class inorder {
     int val;
     inorder left;
     inorder right;
     inorder() {}
     inorder(int val) { this.val = val; }
     inorder(int val, inorder left, inorder right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
  }
 
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        if (root==null){
            return new ArrayList<Integer>();
        }
        List<Integer> result=new ArrayList<Integer>();
        result.addAll(inorderTraversal(root.left));
        result.add(root.val);
        result.addAll(inorderTraversal(root.right));
        return result;
    }
    
}
