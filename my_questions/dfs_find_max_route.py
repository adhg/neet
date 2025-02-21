'''
    from root, how can I get the max values
             3
       8               4
   16           2             1
             7    6         9   12                                 
                    20
                    
 max-->3+4+2+6+20=35
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def find_max_route(self, root):
         
        def dfs(n):
            
            if not n:
                return 0
            
            val_left = dfs(n.left)
            val_rigth = dfs(n.right)         
            
            curr_route = max(val_left, val_rigth)  #decision get the max 
            
            return curr_route+n.val #important, return the curr_route
        
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
    n20 = TreeNode(20) 
    
    n3.left=n8
    n3.right=n4
    n8.left=n16
    n4.left=n2
    n4.right=n1
    n1.left=n9
    n1.right=n12
    n2.left=n7
    n2.right=n6  
    n6.right=n20
    
    s = Solution()
    res = s.find_max_route(root=n3)
    print ("res:=",res)
    
    print ("END")