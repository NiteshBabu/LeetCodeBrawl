def num_reverse(num):
  result = 0
  isNegative = False
  
  if num < 0:
    isNegative = True
    num = -num

  while num != 0:

    # mod = num % 10
    # result = (result * 10) + mod
    # num //= 10

    result = result * 10 + num % 10
    num //= 10

  if isNegative: return -(result)
  return result 


print(num_reverse(-103))
print(num_reverse(103))
