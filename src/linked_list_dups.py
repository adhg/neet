
# remove duplicates from sorted linked list

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution(object):
    def deleteDuplicates(self, head):                

        dummy = head
        ptr = head        
        while ptr and ptr.next:
            v = ptr.val
            nxt_v = ptr.next.val
            
            if v==nxt_v:
                ptr.next=ptr.next.next
            else:
                ptr=ptr.next    
        
        return dummy
        
    
if __name__=='__main__':
    print ("start...")
    
    n1a = ListNode(1)
    n1b = ListNode(1)
    n2 = ListNode(2)
    n3a = ListNode(3)
    n3b = ListNode(3)
    
    n1a.next=n1b
    n1b.next=n2
    n2.next=n3a
    n3a.next=n3b
    
    
    s = Solution()
    p = s.deleteDuplicates(n1a)
    
    while p:
        print (p.val,end='-->')
        p=p.next
        
    print ("\nEND")