def remove_element(nums:list, item:int):
# swapping with the slow pointer
  # slow = 0  
  # fast = 0
  # while fast < len(nums):
  #   if nums[fast] != item:
  #     nums[slow] = nums[fast]
  #     slow += 1
  #   fast += 1
  # return nums[:slow]
  
# swapping with the last element
  start = 0
  end = len(nums)
  while start < end:
    if nums[start] == item:
      nums[start] = nums[end-1]
      end -= 1
    else:
      start += 1
  return nums[:end]
      


nums = [1,2,3,4,2,2,2,5]
print(remove_element(nums, 2))
