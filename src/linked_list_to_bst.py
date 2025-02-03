
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sortedListToBST(self, head):                
        
        res = []
        while head:
            res.append(head.val)
            head=head.next
        
        def dfs (left_index, right_index):
            
            if left_index>=right_index:
                return 
            
            mid_index = (left_index + right_index)//2
            mid_value = res[mid_index]
            
            n = TreeNode(mid_value)
            n.left  = dfs(left_index, mid_index)
            n.right = dfs(mid_index+1, right_index)
                        
            return n
        
        return dfs(0,len(res))
        
    
if __name__=='__main__':
    print ("start...")
    
    n10 = ListNode(-10) 
    n3 = ListNode(-3) 
    n0 = ListNode(0) 
    n5 = ListNode(5) 
    n9 = ListNode(9) 
    
    n10.next = n3
    n3.next = n0
    n0.next = n5
    n5.next = n9
    
    s = Solution()
    p = s.sortedListToBST(n10)
    
    def print_node(n):
        if not n:
            return
        print (n.val)
        print_node (n.left)
        print_node (n.right)
    
    print_node(p)
        
    print ("\nEND")