# Find max_sum subarray which is continuous

# Naive method O(n^2) time coplexity
def max_sub(LIST):
  max_sum = float('-inf')

  for i in range(len(LIST)):
    current_sum = LIST[i]
    for j in range(i+1, len(LIST)):
      current_sum += LIST[j]
      max_sum = max(current_sum, max_sum)

  return max_sum


# O(n) time complexity
def kadanes_algo(LIST):
  max_sum = float('-inf')
  current_sum = 0 

  for num in LIST:
    current_sum = max(current_sum + num, num)
    max_sum = max(max_sum, current_sum)

  return max_sum


LIST = [2,10,-10,4,8,-1,2,1,-5]  # 16

print(max_sub(LIST))
print(kadanes_algo(LIST))

s = "()"
stack = [s[0]]
pair = {
          '(' : ')',
          '{' : '}',
          '[' : ']',
        }   
for b in s[1:]:
  print(pair[stack[-1]], b)
  if pair[stack[-1]] == b:
    stack.pop()
  else:
    stack.append(b)
x = []
print(bool(1))

