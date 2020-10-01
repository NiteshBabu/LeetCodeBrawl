def count_say(n:int) -> str:
  result = '1'

  if n == 1:
    return result

  char_pointer = 0
  count = 0
  current_string = ''  
  
  while n > 1:
    while count < len(result):
      try:
        while result[char_pointer] == result[count]:
          count += 1
      except IndexError:
        pass
      current_string += str(count - char_pointer) + result[char_pointer]
      char_pointer = count

    result = current_string
    current_string = ''
    char_pointer = 0
    count = 0
    n -= 1

  return result


print(count_say(5))

