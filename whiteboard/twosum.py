"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # create dictionary to store the numbers in the array as keys.
        dic = {}
        

        for i, v in enumerate(nums):
            # traverse each number inside the keys of the dic to complete the sum, then 
            # obtain the 2nd number by 'target - v' which is the difference.
            if target - v in dic:
                # now return the position of the past number 'dic[target - v]' and the index
                # of tbe current number.
                return dic[target - v], i
            
            else:
                dic[v] = i
        
        return -1

"""Runtime: 40 ms, faster than 78.66% of Python online submissions for Two Sum.
Memory Usage: 14 MB, less than 41.23% of Python online submissions for Two Sum."""
