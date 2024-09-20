# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
# 
# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

def has22(nums):
  for x in range(len(nums)):
    if (x > 0) and nums[x-1] == 2 and nums[x] == 2:
      return True
  return False