import java.util.ArrayList;
import java.util.List;
public class PostOrder {
     int val;
      PostOrder left;
      PostOrder right;
      PostOrder() {}
      PostOrder(int val) { this.val = val; }
      PostOrder(int val, PostOrder left, PostOrder right) {
          this.val = val;
         this.left = left;
          this.right = right;
      }
  }
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        if (root==null){
            return new ArrayList<Integer>();
        }
        List<Integer> result=new ArrayList<Integer>();
        result.addAll(postorderTraversal(root.left));
        result.addAll(postorderTraversal(root.right));
        result.add(root.val);
        return result;
    }
}
