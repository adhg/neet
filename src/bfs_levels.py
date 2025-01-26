from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        
        res = []
        q = deque()
        q.append(root)
        
        while q:
            levels = []
            len_q = len(q) #important! iterate over current elements
            for _ in range(len_q):                
                n = q.popleft()
                if n:
                    levels.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
                
            res.append(levels)

        return res


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