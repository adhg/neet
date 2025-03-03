'''
using sliding win technic, you have a left_pointer and a right_pointer, 
if you can add an element -> add to the set and push right pointer to the right
if you can't you need to remove the duplicated item starting from the left
When you find the diplicated item - do not remove it but get the right_pointer to the right
'''

class Solution:
    
    def lengthOfLongestSubstring(self,s):
        
        my_set = set()
        longest_substring = 0
        
        left_ptr = 0
        right_ptr = 0
        
        for n in s:
            if n not in my_set:
                my_set.add(n)
                right_ptr+=1
            else:                 
                while left_ptr<right_ptr:
                    v = s[left_ptr]
                    left_ptr+=1
                    if v==n:
                        right_ptr+=1
                        break
                    my_set.remove(v)                    

            longest_substring = max(longest_substring,len(my_set))
                                        
        return longest_substring
    
if __name__=='__main__':
    print ("START...")
    
    s = "abcabcbb" #-->3 #amqpcsrumjjufpu-->8
    so = Solution()    
    res = so.lengthOfLongestSubstring(s)
    print(res)
    
    print("END")