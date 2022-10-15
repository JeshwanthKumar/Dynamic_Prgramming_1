#Time_Complexity : O(n)
#Space_Complexity : O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
# Array solution
        dp = []     #Initializing and emoty array as dp
        if(len(nums) == 1): #If the lenght of nums is 1 then return the first element in nums
            return nums[0]
        dp.append(nums[0])  #Append the first element into the dp array
            
        dp.append(max(nums[0],nums[1])) #Append the max value between the first and the second element in nums
        
        for i in range(2, len(nums)):   #Continue the loop from 2 index to the length of nums
            dp.append(max(nums[i]+dp[i-2], dp[i-1]))    #Append the max value between the sum of nums[i] and dp[i-2] and dp[i-1]
        
        return dp[-1]   #Return the last element in the dp array
            
#---------------------------------------------------------------------------------------------#
# Two variable solution        
        
#         if len(nums) == 1:
#             return nums[0]
#         prev_profit = nums[0]
#         curr_profit = max(nums[0], nums[1])
        
#         for i in range(2, len(nums)):
#             if ((nums[i]+prev_profit) > curr_profit):
#                
#                 temp = curr_profit
#                 curr_profit = nums[i]+prev_profit
#                 prev_profit = temp
                
#             else:
#                 prev_profit = curr_profit
                
#         return curr_profit

                
            
        