def LineAnalysis(line):
  sort = []
  j = 0
  b = False
  l = list(line)
  s = 0
  for  i in range(len(l)):
    if l[i] == '*':
      sort.append(i)
  if len(sort) <= 2:
    b = True
    return b
  for i in range(len(sort)):
    while j is not (len(sort)-1):
      if s + sort[1] == sort[j + 1]:
        s +=sort[1]
        b = True
      else:
        s +=sort[1]
        b = False
      j += 1
  return b


print(LineAnalysis('*..*..*..*..*..*..*'))