# Given 2 strings, a and b, return the number of the positions
# where they contain the same length 2 substring. So "xxcaazz"
# and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings
# appear in the same place in both strings.
# 
# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0

def string_match(a, b):
  sum = 0
  shorter = len(a)
  if len(a) > len(b):
    shorter = len(b)
  for x in range(shorter-1):
    if a[x] + a[x+1] == b[x] + b[x+1]:
      sum = sum + 1
  return sum