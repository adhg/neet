from collections import defaultdict

'''
            1
    2               3
4               2       4
            4    

note above 2 and 4 and 4 are duplicates! 

'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def find_duplicates(self, root):
        subtrees = defaultdict(list)
        res = []
        
        def dfs(node):
            if not node:
                return 'null'
            
            left  = dfs(node.left)
            right = dfs(node.right)
            node_val = str(node.val)
            s = ",".join([node_val,left, right]) # the magic is here. We take a signature of the current node AND below
             
            if len(subtrees[s])==1:
                res.append(s) # change to node or node.val 
            subtrees[s].append(node)
            return s #<----------------------------- dont forget to return the signature 
                
        
        dfs(root)
        return res


if __name__=='__main__':
    print ("start...")
    
    n1 = TreeNode(1)
    n2a = TreeNode(2)
    n2b = TreeNode(2)
    n3 = TreeNode(3)
    n4a = TreeNode(4)
    n4b = TreeNode(4)
    n4c = TreeNode(4)

    n1.left=n2a
    n1.right=n3
    n2a.left=n4a
    n3.left=n2b
    n3.right=n4c
    n2b.left=n4b
    
    s = Solution()
    res = s.find_duplicates(n1)
    print (res)
    
    print ("END")