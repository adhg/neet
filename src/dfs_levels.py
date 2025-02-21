from collections import defaultdict
'''
result would be: defaultdict(<class 'list'>, {0: [3], 1: [9, 20], 2: [15, 7]})
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        
        d = defaultdict(list)

        def dfs(node, level):
            if not node:
                return
            
            d[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)                
        
        dfs(root, 0)
        return d


if __name__=='__main__':
    print ("start...")
    
    n3 = TreeNode(3)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n15 = TreeNode(15)
    n7 = TreeNode(7)
    
    n3.left=n9
    n3.right=n20
    n20.left=n15
    n20.right=n7
    
    s = Solution()
    res = s.levelOrder(n3)
    print (res)
    
    print ("END")