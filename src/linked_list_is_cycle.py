
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def hasCycle(self, head):
        
        fast = head
        slow = head
        
        while fast and fast.next: #if there's a cycle the slow and fast will meet at one point
            fast = fast.next.next
            slow = slow.next
            
            if fast==slow:
                return True
        
        return False
        
    
if __name__=='__main__':
    print ("start...")
    
    n10 = ListNode(10)
    n5 = ListNode(5)
    n21 = ListNode(21)
    n7 = ListNode(7)
    n4 = ListNode(4)
    n3 = ListNode(3)
    

    n10.next=n5
    n5.next=n21
    n21.next=n3
    n21.next=n7
    n7.next=n4
    n4.next=n3
    #n3.next=n5
    

    s = Solution()
    f = s.hasCycle(n10)
    print ("\nfound cycle? ",f)
    
    
    print ("END")