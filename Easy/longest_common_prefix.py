strs = ['flower','flow', 'fly']
print(list(zip(*strs)))

def longestCommonPrefix(strs):
  result = set()
  for c in set(zip(*strs)):

  # result = ''
  # if len(strs) < 1:
  #   return result

  # comparison_word = strs[0]
  # comparison_index = 0

  # for comparison_letter in comparison_word:
  #   for i in range(1, len(strs)):
  #     current_word = strs[i]
  #     current_letter = current_word[comparison_index]
  #     if comparison_letter != current_letter or comparison_index > len(current_word): return result
  #   comparison_index +=1
  #   result += comparison_letter

  # return result 

print(longestCommonPrefix(strs))





