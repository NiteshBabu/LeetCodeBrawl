def min_edit_distance(s1, s2):
  '''
  Min edit distance is defined as the min no. of operations done to convert one string to other with :
    1. INSERT
    2. REPLACE
    3. DELETE

    [    '' e n e m y
     '' [0  1 2 3 4 5 ],
      n [1  1 1 2 3 4 ],
      e [2  1 2 1 2 3 ],
      m [3  3 2 3 1 2 ],
      o [4  4 3 3 2 2 ],
    ]

  '''
  if s1 == s2:
    return 0
  elif len(s1) == 0: return len(s2)
  elif len(s2) == 0: return len(s1)
  memoize = [ [float('inf') for x in range(len(s2) + 1)] for x in range(len(s1) + 1)]

  for i in range(len(memoize)):
    for j in range(len(memoize[0])):
      # first row & column are empty string so we set the distance as the actual length of the string upto there
      if i*j == 0:  # i or j = 0
        memoize[i][j] = i+j
      else:
        if s1[i-1] == s2[j-1]:
          memoize[i][j] = memoize[i-1][j-1]
        else:
          memoize[i][j] = min(memoize[i][j-1], memoize[i-1][j], memoize[i-1][j-1]) + 1

  for row in memoize:
    print(row)

  return memoize[-1][-1]





print(min_edit_distance('cocool', 'cooc'))

