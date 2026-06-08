def sorted_string(n):
  return "".join(sorted(str(n)))

def check(n, max_multiplier):
  compare_against = sorted_string(n)
  for i in range(2, max_multiplier + 1):
    if sorted_string(i * n) != compare_against:
      return False
  
  return True

def search(n, max_multiplier):
  for i in range(2, n + 1):
    if check(i, max_multiplier):
      return i
  
  return -1

print(search(1_000_000_000, 6))
