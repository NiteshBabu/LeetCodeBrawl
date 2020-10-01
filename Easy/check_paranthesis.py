def check_paranthesis(s: str) -> bool:
  if len(s) < 2:
    return False
  pair = {
    ')' : '(',
    '}' : '{',
    ']' : '[',
  }

  stack = []

  for b in s:
    if b in pair :
      top_element = stack.pop() if stack else '#'
      if pair[b] != top_element:
        return False
    else:
      stack.append(b)

  return not stack

print(check_paranthesis('()}}'))

# if-else shorthand
# print('True') if conditon else print('False')
# print('XYZ') if conditon else print(f'f + {chr(67)}')


class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None






