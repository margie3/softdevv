# Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6
# and extending to the next 7 (every 6 will be followed by at least one 7).
# Return 0 for no numbers.
# 
# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

def sum67(nums):
  sum = 0
  add = True
  for x in range(len(nums)):
    if nums[x] == 6:
      add = False
    if add:
      sum = sum + nums[x]
    if nums[x] == 7:
      add = True
  return sum