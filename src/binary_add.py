

class Solution:
    
    def add_binary_strings(self, s1,s2):
        
        s1 = list(s1)
        s2 = list(s2)
        
        ptr_s1 = len(s1)-1
        ptr_s2 = len(s2)-1
        
        res = []
        remainder = 0 
        while ptr_s1>=0 or ptr_s2>=0 or remainder>0:
            vs1 = int(s1[ptr_s1]) if ptr_s1>=0 else 0
            vs2 = int(s2[ptr_s2]) if ptr_s2>=0 else 0
            
            r = vs1 + vs2 + remainder                
            if r==2:
                r=0
                remainder=1
            elif r==3:
                r=1
                remainder=1
            else:
                remainder=0
            
            ptr_s1 -=1
            ptr_s2 -=1
            
            res.append(r)
        
        res = list(reversed(res))
        return str(res)
                
                         
if __name__=='__main__':

    print ("Start...")

    s1 =   '1011'
    s2 = '100011'
    '''
        ---------
               0
    '''
    
    s = Solution()
    res = s.add_binary_strings(s1,s2)
    print ("RES:=", res)
    
    print ("END")