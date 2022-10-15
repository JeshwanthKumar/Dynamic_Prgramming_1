#Time_Complexity: O(n) 
#Space_Complexity : O(n) - For every element inserted into the hashset 

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freqHset = [0]*(max(nums)+1)    #Initialize an array with 0s for maximum+1 element in the given array
        dpArr = [0] * len(freqHset) #Initialize a dpArr with 0s for the length of the array
        
        for i in nums:  #For every element in nums add those into the freqHset
            freqHset[i] += i
        
        dpArr[0] = 0    #Initialize 0 as the first element in the dpArr
        dpArr[1] = freqHset[1]  #Initialize the second element in dpArr as the element in freqHset
        
        for i in range(2, len(dpArr)):  #Continue the loop from 2 to length of the dpArr
            dpArr[i] = max((freqHset[i]+dpArr[i-2]), dpArr[i-1])    #Set maximum value between the sum of freqHset[i] and dpArr[i-2] and dpArr[i-1]
        return dpArr[-1]    #Return the last element in the dpArr that has the maximum earn