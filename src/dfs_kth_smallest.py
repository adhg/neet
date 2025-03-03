'''
Given a BST!!! what is the kth smallest element
to do so - you need to traverse inline!
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
                
    def kthSmallest(self, root, k):
        
        self.counter = 0    
        self.res = None     
        def dfs(node):
            if not node:
                return
                        
            dfs(node.left)                                    
            
            self.counter+=1
            if k==self.counter:
                self.res=node.val
                        
            dfs(node.right)
                 
        dfs(root)
        return self.res


if __name__=='__main__':
    print ("start...")
    
    n5 = TreeNode(5)
    n3 = TreeNode(3)
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n4 = TreeNode(4)
    n1 = TreeNode(1)
    
    n5.left=n3
    n5.right=n6    
    n3.left=n2
    n3.right=n4
    n2.left=n1
    
    s = Solution()
    res = s.kthSmallest(n5,k=3)
    print (res)
    
    print ("END")