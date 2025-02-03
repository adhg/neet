
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
                
        dummy = ListNode()   
        dummy.next = head          
        nth_ptr = dummy
        
        nth_counter = n
        
        while head:            
            head=head.next
            if nth_counter>0:
                nth_counter-=1
            else:
                nth_ptr=nth_ptr.next 
                
             
        #at the nth pointer -1 
        if nth_ptr and nth_ptr.next:
            nth_ptr.next = nth_ptr.next.next
        else:
            return None #in the event to remove itself 
                
        return dummy.next
        
    
if __name__=='__main__':
    print ("start...")
     
    n1 = ListNode(1) 
    n2 = ListNode(2) 
    n3 = ListNode(3) 
    n4 = ListNode(4) 
    n5 = ListNode(5) 
    
    n1.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5
    

    s = Solution()
    p = s.removeNthFromEnd(n1,2)
    
    while p:
        print (p.val,end='-->')    
        p=p.next
        
    print ("\nEND")