
class Solution(object):
    def singleNumber_2(self, nums):

        counter = {} 
        for n in nums:
            counter[n] = counter.get(n,0)+1
            
        for k,v in counter.items():
            if v==1:
                return k
        
        return -1
    
    def singleNumber(self, nums): #XOR will win!
        
        t = 0
        for n in nums:
            t = t ^ n 
        
        return t
        
if __name__=='__main__':
    print("Start...")
    
    nums = [4,1,2,1,2]
     
    s = Solution()
    res = s.singleNumber(nums)
    print (res)
    
    print ("END")