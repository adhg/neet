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
         
        def dfs(n, path):
            
            if not n:
                return (0,path)
                        
            val_left, path_left = dfs(n.left, path  + "-->L")
            val_right, path_right = dfs(n.right, path  + "-->R")         
                          
            if val_left>val_right:
                return (val_left+n.val, path_left) #important, return the curr_route
            else:
               return (val_right+n.val, path_right)
            
            
        
        res ,moves = dfs(root,'ROOT')        
        return res, moves



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
    res,moves = s.find_max_route(root=n3)
    print ("res:=",res)
    print ("moves:=",moves)
    
    print ("END")