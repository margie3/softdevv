# Given a non-empty string like "Code" return a string like "CCoCodCode".
# 
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(str):
  each = ""
  for x in range(len(str)):
    each = each + str[:x+1]
  return each