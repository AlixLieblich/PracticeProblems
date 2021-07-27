def anagrams(str1, str2):
  if sorted(str1) == sorted(str2):
    return True
  else:
    return False
print(anagrams("aas", "saa"))
