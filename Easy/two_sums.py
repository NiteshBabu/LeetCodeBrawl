'''
  List of integers nums and an integer target, 
  return indices of the two numbers such that they add up to target.
    
    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

    Constraints:

        2 <= nums.length <= 105
        -109 <= nums[i] <= 109
        -109 <= target <= 109
        Only one valid answer exists.
'''

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
      # Method 1 (fast)
      hmap = {}
      for i in range(len(nums)):
          if nums[i] not in hmap:
              hmap[target-nums[i]] = i
          else:
              return [hmap[nums[i]],i]

      # Method 2 (faster)
      hmap = {num:i for i, num in enumerate(nums)}
      for i, num in enumerate(nums):
        if target - num in hmap and hmap[target-num] != i:
          return [i, hmap[target-num]]

            
      # Method 3 (slow) but uses less memory, using the built-in index method
      for i in range(len(nums)):
          if target - nums[i] in nums and nums.index(target - nums[i]) != i:
              return [i, nums.index(target-nums[i])]

solution = Solution()
print(solution.twoSum([2,3,4,1,23,13], 14))


class Solution:
  def addTwoNumbers(self, l1, l2):
    # num1 = num2 = 0
    
    # i = 0
    # while l1:
    #     num1 += l1.val * 10**i
    #     i+=1
    #     l1 = l1.next
    # i = 0
    # while l2:
    #     num2 += l2.val * 10**i
    #     i+=1
    #     l2 = l2.next
    temp = l1 + l2
    result = 0

    while temp > 0:
      result = result*10 + temp%10 
      temp //= 10
    return result

solution = Solution()
print(solution.addTwoNumbers(123, 456))