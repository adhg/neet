
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
  
        left_ptr = 0
        right_ptr = len(nums)-1
        
        res = []
        while left_ptr<=right_ptr:
            #whos bigger? leftV or rightV 
            #res should be [desending]
            
            left_value = nums[left_ptr]**2
            right_value = nums[right_ptr]**2
            
            #choose the lower value!
            if left_value>right_value:
                res.append(left_value)
                left_ptr+=1
            else:#right value is bigger
                res.append(right_value)
                right_ptr-=1
        
        return list(reversed(res))
            
        
                    
if __name__=='__main__':
    print ("start...")
                
    nums = [-4,-1,0,3,10]
    
    s = Solution()
    res = s.sortedSquares(nums)
    print (res)
    
    print ("END")