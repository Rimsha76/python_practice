def function(parameter, parameter2):
  if (parameter != 2 and parameter2 != 2):
    return True
  else:
    return False

words = ["apple", "banana", "pear", "banana"]
for word in words:
  print(word)

print(words[1:4])
print(len(words))
print(min(range(4)))
print(words.count("banana"))