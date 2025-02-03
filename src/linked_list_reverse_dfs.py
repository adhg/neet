
# reverse the entire linked list

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution(object):
    def reverse(self, head):                
         
        def dfs(head):
            
            if not head:
                return None

            new_head = head
            if head.next:
                new_head = dfs(head.next)
                head.next.next = head
            head.next = None
            return new_head
        
        return dfs(head)
        
    
if __name__=='__main__':
    print ("start...")
    
    '''
    [8]-->[12]-->[3]-->[17]-->[25]
    '''
    
    n8 = ListNode(8)
    n12 = ListNode(12)
    n3 = ListNode(3)
    n17 = ListNode(17)
    n25 = ListNode(25)
    
    n8.next=n12
    n12.next=n3
    n3.next=n17
    n17.next=n25
        
    s = Solution()
    p = s.reverse(n8)
    
    while p:
        print (p.val,end='-->')
        p=p.next
        
    print ("\nEND")