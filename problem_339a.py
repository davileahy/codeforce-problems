sum = input() # string

sum_ordered = []

for i in sum:
  try:
    int(i)
    sum_ordered.append(i)
  except:
    pass

sum_ordered.sort()

print('+'.join(sum_ordered))
