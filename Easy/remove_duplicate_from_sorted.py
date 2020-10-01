# shorthand to remove duplicate from list
# nums = list(dict.fromkeys(nums))
nums = [1,1,2,3,3,4,9]


def remove_duplicate(nums: list) -> int:
  # _nums = list(dict.fromkeys(nums))
  # for i in range(len(_nums)):        
  #   nums[i] = _nums[i]
  # return len(_nums)

  slow = 0
  fast = slow + 1
  while fast < len(nums):
    if nums[fast] != nums[slow]:
      slow += 1
      nums[slow] = nums[fast]
    fast += 1
  return nums[:slow+1]


print(remove_duplicate(nums))
