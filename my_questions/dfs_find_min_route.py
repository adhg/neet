'''
    from root, how can I get the min values
             3
       8               4
   16           2             1
             7    6         9   12                                 
                    
                    
 min-->3+4+2+6=15
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def find_min_route(self, root):
         
        def dfs(n):
            
            if not n:
                return float('inf')
            
            if not n.left and not n.right:
                return n.val
            
            val_left = dfs(n.left)
            val_rigth = dfs(n.right)
                             
            return min(val_left, val_rigth) + n.val
             
        
        res = dfs(root)
        
        return res



if __name__=='__main__':
    print ("start...")
         
    n3 = TreeNode(3)
    n8 = TreeNode(8)
    n4 = TreeNode(4)
    n16 = TreeNode(16)
    n1 = TreeNode(1)
    n2 = TreeNode(2)    
    n7 = TreeNode(7)
    n6 = TreeNode(6)
    n9 = TreeNode(9)
    n12 = TreeNode(12)  
    
    n3.left=n8
    n3.right=n4
    n8.left=n16
    n4.left=n2
    n4.right=n1
    n1.left=n9
    n1.right=n12
    n2.left=n7
    n2.right=n6   
    
    s = Solution()
    res = s.find_min_route(root=n3)
    print ("res:=",res)
    
    print ("END")