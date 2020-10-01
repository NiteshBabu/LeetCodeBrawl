def romanToInt(s: str) -> int:
  hmap = {
        'I' :    1,
        'V' :    5,
        'X' :    10,
        'L' :    50,
        'C' :    100,
        'D' :    500,
        'M' :    1000,
    }
  ans = 0
  # for i in range(len(s)-1):
  #   if hmap[s[i]] >= hmap[s[i+1]]:
  #     ans += hmap[s[i]]
  #   elif hmap[s[i]] < hmap[s[i+1]]:
  #     ans -= hmap[s[i]]
  #   # s = s.replace(_, str(hmap[_]))
  # ans += hmap[s[-1]]

  s.replace('IV', 'IIII', -1).replace('IX', 'VIIII', -1).replace('XL', 'XXXX', -1 )
  s.replace('XC', 'LXXXX', -1 ).replace('CD', 'CCCC', -1 ).replace('CM', 'DCCCC', -1 )
  print(s)
  for _ in s:
    ans += hmap[_]
      

  return ans

print(romanToInt('IV'))


l = '1234'
print(l)