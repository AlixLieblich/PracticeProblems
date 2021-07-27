def sameFrequency(first, second):
  num_counts = {}
  for num in str(second):
    num_counts[num] = num_counts.get(num, 0) + 1
  for num in str(first):
    num_counts[num] = num_counts.get(num, 0) - 1
  return all(value == 0 for value in num_counts.values())
print(sameFrequency(182, 218))
