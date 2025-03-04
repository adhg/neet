#https://leetcode.com/problems/next-permutation/submissions/1562746324/

class Solution:
    def nextPermutation(self, nums):
        
        #find pivot
        pivot_idx = None        
        for i in range(len(nums)-1,0,-1):
            val = nums[i]
            nxt_val = nums[i-1]
            if nxt_val<val: #order is ascending -- GREAT!                 
                pivot_idx=i-1
                break
        
        #if we didnt find the pivot - that's the last premutation
        if pivot_idx==None:
            nums.sort()
            return 
                
        #Swap values if pivot_indx and the first larger value in the sub_array
        prefix = []
        pivot_val = nums[pivot_idx]
        for i in range(len(nums)-1,-1,-1):
            val = nums[i]
            if pivot_val<val:
                swap_idx=i
                break
                            
        swap_val = nums[swap_idx]
        temp = swap_val
        nums[swap_idx] = pivot_val
        nums[pivot_idx] = temp    
        
        #ensure sorted prefix
        prefix = sorted(nums[pivot_idx+1:])   
        #nums = nums[0:pivot_idx+1] + prefix  # <--- This creates a new list and assigns it LOCALLY!!!!     
        nums[:] = nums[0:pivot_idx+1]+prefix  #Why nums[:] - becuase we can only modify the values in the nums; so in this case we need to create a new copy of the array.


# Test
if __name__ == '__main__':
    print("Start...")
    
    #nums = [6,2,1,5,4,3,0]
    nums = [1,3,2]
    nums = [1,5,1]
    
    s = Solution()
    s.nextPermutation(nums)
    
    print("next Permutation:=", nums)
    print("END")
